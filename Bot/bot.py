import os
import threading
import queue
import sys
import socket
from dotenv import load_dotenv

from Modules.Twitch import GetUsername
from Modules.Network import connect
from Modules.Commands import CommandHandler

# Load environment variables
load_dotenv()

BOTNAME = os.getenv("BOTNAME")
TOKEN = os.getenv("OAUTH_ID")
CHANNEL = os.getenv("LIVE_CHANNEL")

# Global shutdown flag
shutdown_requested = False

# Establish IRC connection
irc = connect(TOKEN, BOTNAME, CHANNEL)

# Initialize the command queue
command_queue = queue.Queue()

def worker():
    while True:
        data = command_queue.get()
        if data is None:
            print("[WORKER] Shutdown signal received")
            command_queue.task_done()
            break

        irc, channel, command_info = data

        try:
            print(f"[WORKER] Handling command: {command_info}")
            should_quit = CommandHandler(irc, channel, command_info)

            if should_quit:
                global shutdown_requested
                shutdown_requested = True
                print("[WORKER] Shutdown requested by command")
        except Exception as e:
            print(f"[WORKER] Error handling command: {e}")

        command_queue.task_done()

def HandleMessage(response: str) -> bool:
    """Process an incoming IRC message."""
    global shutdown_requested

    if shutdown_requested:
        print("[HANDLE] Ignored message due to shutdown")
        return False

    print(f"[RAW] {response.strip()}")

    if "PRIVMSG" not in response:
        return False

    parts = response.split(":", 2)
    if len(parts) < 3:
        return False

    full_message = parts[2].strip()
    user = GetUsername(response)

    words = full_message.split()
    if not words:
        return False

    command = words[0].lower()
    args = words[1:]

    print(f"[PARSED] {user}: {command} {args}")
    command_queue.put((irc, CHANNEL, (command, args, user)))
    print(f"[QUEUED] {command} from {user}")
    return False

def main():
    while True:
        try:
            response = irc.recv(2048).decode("utf-8")
        except socket.timeout:
            if shutdown_requested:
                break
            continue
        except Exception as e:
            print(f"[MAIN] Error receiving message: {e}")
            continue

        if response.startswith("PING"):
            irc.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            continue

        HandleMessage(response)

    print("[MAIN] Exiting main loop...")
    command_queue.put(None)
    command_queue.join()
    irc.close()
    print("[MAIN] IRC connection closed. Exiting.")
    sys.exit(0)

if __name__ == "__main__":
    threading.Thread(target=worker, daemon=True).start()
    main()
