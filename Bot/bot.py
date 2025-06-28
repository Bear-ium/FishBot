import os
import threading
import queue
from dotenv import load_dotenv

from Modules.Twitch import GetUsername
from Modules.Network import connect
from Modules.Commands import CommandHandler

# Load environment variables
load_dotenv()

BOTNAME = os.getenv("BOTNAME")
TOKEN = os.getenv("OAUTH_ID")
CHANNEL = os.getenv("LIVE_CHANNEL")

# Establish an IRC connection
irc = connect(TOKEN, BOTNAME, CHANNEL)

# Initialize the command queue
command_queue = queue.Queue()

def worker():
    while True:
        data = command_queue.get()
        if data is None:
            break
        irc, channel, command_info = data
        try:
            CommandHandler(irc, channel, command_info)
        except Exception as e:
            print(f"Error handling command: {e}")
        command_queue.task_done()

# Start the worker thread
threading.Thread(target=worker, daemon=True).start()

def HandleMessage(response: str) -> bool:
    """Process an incoming IRC message."""
    print(response.strip())

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

    # Queue the command for processing
    command_queue.put((irc, CHANNEL, (command, args, user)))
    return False

def main():
    """Main event loop."""
    while True:
        try:
            response = irc.recv(2048).decode("utf-8")
        except Exception as e:
            print(f"Error receiving message: {e}")
            continue

        if response.startswith("PING"):
            irc.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            continue

        if HandleMessage(response):
            break

if __name__ == "__main__":
    main()
