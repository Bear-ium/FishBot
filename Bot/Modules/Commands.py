import time

from Modules.Twitch import Send
from Modules.Fish import Reel
from Modules.Configurations import COOLDOWN_SECONDS, ADMINS, COMMAND_HANDLE

# Tracks user cooldowns for rate-limiting
cooldowns = {}
_IsTesting = False

def CommandHandler(irc, channel: str, info: tuple) -> bool:
    global _IsTesting
    
    command, args, user = info
    user = user.lower()

    if not command.startswith(COMMAND_HANDLE):
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
            
            if _IsTesting and user in ADMINS:
                fish = Reel(user)
                Send(irc, channel, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")
                cooldowns[user] = now
                return False

            if now - last_used < COOLDOWN_SECONDS:
                return False
            
            fish = Reel(user)
            Send(irc, channel, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")
            cooldowns[user] = now
        
        case "multi-fish":
            if user not in ADMINS or not args or not _IsTesting:
                return False

            try:
                num = int(args[0])
            except ValueError as e:
                print(f"[DEBUG] Invalid number provided: {e}")
                return False

            for i in range(1, num + 1):
                fish = Reel(user)
                Send(irc, channel, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")

            Send(irc, channel, f"Fished x{num} times!")
            
        case "upgrade":
            upgrade_type = args[0].strip()[0]
            
            match upgrade_type:
                case "b":
                    Send(irc, channel, "Upgrade boat")
            
                case "r":
                    Send(irc, channel, "Upgrade Fishing Rod")
            
                
            return False

        
        case "testing":
            if user in ADMINS:
                _IsTesting = not _IsTesting
                Send(irc, channel, f"Testing mode is now {'ON' if _IsTesting else 'OFF'}.")
            else:
                return False

        
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