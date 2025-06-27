from Modules.Twitch import Send
from Modules.Admins import admins

def CommandHandler(irc, CHANNEL, info: tuple):
    command, args, user = info
    user = user.lower()

    # Normal Commands
    if command == "-hello":
        Send(irc, CHANNEL, "Hello World!")
    elif command == "-user":
        if args:
            Send(irc, CHANNEL, f"{user}, you passed arguments: {' '.join(args)}")
        else:
            Send(irc, CHANNEL, f"{user}")
    elif command in ("-shoutout", "-so"):
        if user in admins and args:
            arg = args[0].strip('@')
            Send(irc, CHANNEL, f"You should follow @{arg} on twitch.tv/{arg}")
        else:
            Send(irc, CHANNEL, "You either need to be an Admin, or you forgot to add the channel!")



    # Quit Command
    elif command == "-quit":
        Send(irc, CHANNEL, "Goodbye World!")
        return True
    
    return False 