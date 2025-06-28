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
            if user in admins and args:
                arg = args[0].strip('@')
                Send(irc, CHANNEL, f"You should follow @{arg} on twitch.tv/{arg}")
            else:
                Send(irc, CHANNEL, "You either need to be an Admin, or you forgot to add the channel!")

        case "-fish":
            fish = Reel()
            Send(irc, CHANNEL, f"{user} caught a {fish.name} weighing {fish.weight}kg! (+{fish.value} coins)")

        case "-quit":
            Send(irc, CHANNEL, "Goodbye World!")
            return True

        case _:
            # Unknown or unhandled command
            pass

    return False