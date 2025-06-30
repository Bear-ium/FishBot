# FishBot
🎣 A simple Twitch Fishing Bot


## Secure Environment
Create a `.env` file and put these in;
|     Variable Name      |                           Description                           |
| :--------------------: | :-------------------------------------------------------------: |
|       `BOTNAME`        |                    The username of your bot                     |
|       `OAUTH_ID`       |             OAuth token for authenticating the bot              |
|      `CLIENT_ID`       |               Your Twitch application’s Client ID               |
|    `CLIENT_SECRET`     |             Your Twitch application’s Client Secret             |
| `TWITCH_REFRESH_TOKEN` |         Refresh token for generating new access tokens          |
|     `LIVE_CHANNEL`     | Twitch channel the bot should connect to (e.g., `#yourchannel`) |
|       `WEBHOOK`        |          Discord webhook URL for sending notifications          |



```
BOTNAME=your_bot_name
OAUTH_ID=your_oauth_token
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
TWITCH_REFRESH_TOKEN=your_refresh_token
LIVE_CHANNEL=#your_channel
WEBHOOK=your_discord_webhook
```

> ⚠️ **Important:** Never commit your `.env` file to Git. Add it to `.gitignore` to protect sensitive info.