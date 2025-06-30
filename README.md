# FishBot
🎣 A simple Twitch Fishing Bot


## Secure Environment
Create a `.env` file and put these in;
| Variable Name |                 Description                 |
| :-----------: | :-----------------------------------------: |
|    BOTNAME    |            Name of your chat bot            |
|   OAUTH_ID    |    OAuth token you got after logging in     |
|   CLIENT_ID   |           Twitch app's Client ID            |
| CLIENT_SECRET |         Twitch app's Client Secret          |
| LIVE_CHANNEL  |  Twitch channel the bot will join and chat  |
|    WEBHOOK    | A webhook link to your discord text-channel |


```
BOTNAME=your_bot_name
OAUTH_ID=your_oauth_token
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
LIVE_CHANNEL=#your_channel
WEBHOOK=your_discord_webhook
```

> ⚠️ **Important:** Never commit your `.env` file to Git. Add it to `.gitignore` to protect sensitive info.