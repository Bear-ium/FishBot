import os
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


def handle_message(response: str) -> bool:
    """Process an incoming IRC message."""
    print(response.strip())

    if not "PRIVMSG" in response:
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

    # Run the command and see if it requests termination
    return CommandHandler(irc, CHANNEL, (command, args, user))


def main():
    """Main event loop."""
    while True:
        response = irc.recv(2048).decode("utf-8")

        if response.startswith("PING"):
            irc.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            continue

        if handle_message(response):
            break


if __name__ == "__main__":
    main()