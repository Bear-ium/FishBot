import time

from Modules.Twitch import Send
from Modules.Fish import Reel
from Modules.Configurations import COOLDOWN_SECONDS, ADMINS, COMMAND_HANDLE

# Tracks user cooldowns for rate-limiting
cooldowns = {}

def CommandHandler(irc, channel: str, info: tuple) -> bool:
    command, args, user = info
    user = user.lower()

    if not command.starswith(COMMAND_HANDLE):
        return False
    
    cmd = command[len(COMMAND_HANDLE):]

    match cmd:
        case "hello":
            Send(irc, channel, f"Hello {user}!")
        
        case "user":
            msg = f"{user}, you passed arguments: {' '.join(args)}" if args else f"{user}"
            Send(irc, channel, msg)
        
        case "fish":
            now = time.time()
            last_used = cooldowns.get(user, 0)

            if now - last_used < COOLDOWN_SECONDS:
                return False
            
            fish = Reel(user)
            Send(irc, channel, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")
            cooldowns[user] = now
        
        case "quit":
            if user in ADMINS:
                Send(irc, channel, "Goodbye World!")
                print("[QUIT] Quit command accepted")
                return True
            else:
                print("[QUIT] Unauthorized user tried to quit.")
        
        case _:
            # Unkown Command
            pass


    return False