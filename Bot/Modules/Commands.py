from Modules.Twitch import Send
from Modules.Tables import admins
from Modules.Fish import Reel

def CommandHandler(irc, CHANNEL, info: tuple) -> bool:
    command, args, user = info
    user = user.lower()

    match command:
        case "-hello":
            Send(irc, CHANNEL, "Hello World!")

        case "-user":
            if args:
                Send(irc, CHANNEL, f"{user}, you passed arguments: {' '.join(args)}")
            else:
                Send(irc, CHANNEL, f"{user}")

        case "-shoutout" | "-so":
            if user not in admins:
                # User isn't an admin so just ignore them
                return False
            
            if not args:
                # Forgot to include channel
                Send(irc, CHANNEL, "You forgot to include the channel! Usage: -so @ChannelName")
                return False
            
            arg = args[0].strip('@')
            Send(irc, CHANNEL, f"You should follow @{arg} on twitch.tv/{arg}")

        case "-fish":
            fish = Reel(user)
            Send(irc, CHANNEL, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")

        case "-quit":
            if user in admins:
                Send(irc, CHANNEL, "Goodbye World!")
                return True
            else:
                pass

        case _:
            # Unknown or unhandled command
            pass

    return False