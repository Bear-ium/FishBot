import time

from Modules.Twitch import Send
from Modules.Configurations import COOLDOWN_SECONDS, ADMINS, COMMAND_HANDLE

# Command Modules
from Modules.Commands.Fish import Reel
from Modules.Commands.User import GetFishingRodLevel, GetFishingBoatLevel, UpgradeFishingBoatLevel, UpgradeFishingRodLevel, Balance

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
                catches = Reel(user)
                fish_summaries = [
                    f"{fish.name}, {fish.weight:.2f}Kg, {fish.value}c"
                    for fish in catches
                ]
                all_fish = " | ".join(fish_summaries)
                Send(irc, channel, f"{user} caught: {all_fish}")
                cooldowns[user] = now
                return False

            if now - last_used < COOLDOWN_SECONDS:
                return False
            else:
                catches = Reel(user)
                fish_summaries = [
                    f"{fish.name}, {fish.weight:.2f}Kg, {fish.value:,}c"
                    for fish in catches
                ]
                all_fish = " | ".join(fish_summaries)
                Send(irc, channel, f"{user} caught: {all_fish}")
                cooldowns[user] = now
                return False
        
        case "balance" | "bal":
            requestedUser = args[0].lstrip("@").lower() if args else user
            coins = Balance(requestedUser)
            
            if requestedUser == user:
                Send(irc, channel, f"{user}, you have {coins}c.")
            else:
                Send(irc, channel, f"{user}, {requestedUser} has {coins}c.")
            
            return False

        # case "multi-fish":
        #     if user not in ADMINS or not args or not _IsTesting:
        #         return False

        #     try:
        #         num = int(args[0])
        #     except ValueError as e:
        #         print(f"[DEBUG] Invalid number provided: {e}")
        #         return False

        #     for i in range(1, num + 1):
        #         fish = Reel(user)
        #         Send(irc, channel, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")

        #     Send(irc, channel, f"Fished x{num} times!")
            
        case "upgrade":
            upgrade_type = args[0].strip()[0].lower() if len(args) > 0 and args[0].strip() else None
            confirm = args[1].strip()[0].lower() if len(args) > 1 and args[1].strip() else None

            
            match upgrade_type:
                case "b":
                    request, info = UpgradeFishingBoatLevel(user, confirm)
                    
                    # 1   = Module Error
                    # 100 = Info
                    # 200 = Successful
                    # 400 = Unsuccessful
                    if request == 1:
                        Send(irc, channel, "Something went wrong NotLikeThis")
                    elif request == 100:
                        Send(irc, channel, f"@{user}, to upgrade your Boat it costs {info}, type '-upgrade Boat confirm' to upgrade!")
                    elif request == 200:
                        Send(irc, channel, f"@{user}, you have successfully upgraded your Boat to level {info}!")
                    elif request == 400:
                        Send(irc, channel, f"@{user}, you don't have enough money to upgrade your Boat. You need {info}.")
                    
                    return False
            
                case "r":
                    request, info = UpgradeFishingRodLevel(user, confirm)
                    
                    # 1   = Module Error
                    # 100 = Info
                    # 200 = Successful
                    # 400 = Unsuccessful
                    if request == 1:
                        Send(irc, channel, "Something went wrong NotLikeThis")
                    elif request == 100:
                        Send(irc, channel, f"@{user}, to upgrade your Fishing Rod it costs {info}, type '-upgrade rod confirm' to upgrade!")
                    elif request == 200:
                        Send(irc, channel, f"@{user}, you have successfully upgraded your Fishing Rod to level {info}!")
                    elif request == 400:
                        Send(irc, channel, f"@{user}, you don't have enough money to upgrade your Fishing Rod. You need {info}.")
                        
                    return False
                
                case _:
                    Send(irc, channel, "Types of upgrades: boat, rod")
                
            return False
        
        case "boat":
            pass
        
        case "rod":
            pass

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