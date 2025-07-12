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


# Setup Info
### 📦 Database
1. Go to FishBot/Bot/
2. Create `Storage.db`
3. Run `CreateDatabase.py`

### 🔐 Env
1. Go to FishBot/
2. Create `.env`
3. Format it like above in the `README.md`
4. Put in your `CLIENT_ID` and `CLIENT_SECRET`
5. Go to FishBot/Auth
6. Run `app.py`
7. Log in with your BOT account!
8. Save your refresh token in the `.env` under `TWITCH_REFRESH_TOKEN`
9. Fill in the rest as per their descriptions

### 🚀 Run the Bot
1. Go to FishBot/
2. Double click on `RUN.bat`
3. Wait for `venv` & `requirements.txt` setup
4. Type `cd Bot` in the command line which appeared after running `RUN.bat`
5. Then run the `bot.py` by either typing `python3.12 bot.py` OR `python bot.py` OR `bot.py`
6. If it is running to go the channel you specified it wanting to be active in and type in chat `-hello`, it should respond if no errors occured.
7. If you want to stop it type in chat `-quit`