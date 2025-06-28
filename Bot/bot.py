import os
import threading
import queue
import sys
import socket
from dotenv import load_dotenv
from typing import cast

from Modules.Twitch import GetUsername
from Modules.Network import TwitchIRCClient
from Modules.Commands import CommandHandler

class TwitchBot:
    def __init__(self):
        load_dotenv()
        self.botname =  cast(str, os.getenv("BOTNAME"))
        self.token =    cast(str, os.getenv("OAUTH_ID"))
        self.channel =  cast(str, os.getenv("LIVE_CHANNEL"))

        self.shutdown_requested = threading.Event()
        self.command_queue = queue.Queue()

        if not all([self.botname, self.token, self.channel]):
            raise ValueError("Missing one or more required environment variables: BOTNAME, OAUTH_ID, LIVE_CHANNEL")

        self.irc = TwitchIRCClient(self.token, self.botname, self.channel)
        self.irc.connect()

    def start(self):
        threading.Thread(target=self.worker, daemon=True).start()
        self.main_loop()

    def worker(self):
        while True:
            data = self.command_queue.get()
            if data is None:
                print("[WORKER] Shutdown signal received!")
                break

            irc, channel, command_info = data

            try:
                print(f"[WORKER] Handling command: {command_info}")
                if CommandHandler(irc, channel, command_info):
                    self.shutdown_requested.set()
            except Exception as e:
                print(f"[WORKER] Error: {e}")
            finally:
                self.command_queue.task_done()

    def handle_message(self, response: str):
        if "PRIVMSG" not in response:
            return
        
        parts = response.split(":", 2)
        if len(parts) < 3:
            return

        full_msg = parts[2].strip()
        user = GetUsername(response)
        words = full_msg.split()

        if not words:
            return
        
        command = words[0].lower()
        args = words[1:]

        print(f"[PARSED] {user}: {command} {args}")
        self.command_queue.put((self.irc, self.channel, (command, args, user)))

    def main_loop(self):
        print("[BOT] Starting main loop...")

        try:
            while not self.shutdown_requested.is_set():
                try:
                    response = self.irc.recv()
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"[MAIN LOOP] Error: {e}")
                    continue

                if response.startswith("PING"):
                    self.irc.send_raw("PONG :tmi.twitch.tv")
                else:
                    self.handle_message(response)
        finally:
            print("[BOT] Cleaning up...")
            self.command_queue.put(None)
            self.command_queue.join()
            self.irc.close()
            print("[BOT] Shutdown complete.")
            sys.exit(0)

if __name__ == "__main__":
    bot = TwitchBot()
    bot.start()
