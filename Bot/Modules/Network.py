import socket

class TwitchIRCClient:
    def __init__(self, token: str, nickname: str, channel: str, server: str = "irc.chat.twitch.tv", port: int = 6667):
        """
        Creates an IRC client configuration.
        
        @param token (str): The OAuth token (must start with 'oauth:')
        @param nickname (str): The bot's Twitch username
        @param channel (str): The channel to join (must start with '#')
        @param server (str): IRC server hostname
        @param port (int): IRC port
        
        @return None
        """
        if not token.startswith("oauth:"):
            raise ValueError("OAuth token must start with 'oauth:'")
        if not nickname:
            raise ValueError("Nickname cannot be empty.")
        if not channel.startswith("#"):
            raise ValueError("Channel must start with '#'")

        self.token = token
        self.nickname = nickname
        self.channel = channel
        self.server = server
        self.port = port
        self.irc = None

    def connect(self):
        """
        Connects to the IRC server and joins the specified channel.
        
        @return None
        """
        self.irc = socket.socket()
        self.irc.connect((self.server, self.port))
        self.irc.settimeout(1)

        self.send_raw(f"PASS {self.token}")
        self.send_raw(f"NICK {self.nickname}")
        self.send_raw(f"JOIN {self.channel}")

    def send_raw(self, message: str):
        """
        Sends a raw message to the IRC server.
        
        @param message (str): The raw IRC message to send
        
        @return None
        """
        if not self.irc:
            raise ConnectionError("IRC connection not established.")
        self.irc.send((message + "\r\n").encode("utf-8"))

    def recv(self, buffer_size: int = 2048) -> str:
        """
        Receives data from the IRC server.
        
        @param buffer_size (int): The buffer size for receiving data
        
        @return str: The decoded IRC message
        """
        if not self.irc:
            raise ConnectionError("IRC connection not established.")
        return self.irc.recv(buffer_size).decode("utf-8")

    def close(self):
        """
        Closes the IRC connection.
        
        @return None
        """
        if self.irc:
            self.irc.close()
            self.irc = None
