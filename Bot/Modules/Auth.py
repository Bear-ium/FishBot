import os
import requests

from dotenv import load_dotenv

class TwitchAuth:
    def __init__(self, env_path=None):
        if env_path is None:
            env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
        
        load_dotenv(env_path)
        self.env_path = env_path

        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.refresh_token = os.getenv('TWITCH_REFRESH_TOKEN')
        self.oauth_token = None

        self.refresh_access_token()

    
    def refresh_access_token(self):
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token'
        }

        response = requests.post('https://id.twitch.tv/oauth2/token', data=payload)
        if response.status_code != 200:
            raise Exception(f'Failed to refresh token: {response.text}')

        data = response.json()
        self.oauth_token = f"oauth:{data['access_token']}"
        self.refresh_token = data['refresh_token']

        self._update_env_file()
        self._update_runtime_env()

    def _update_env_file(self):
        with open(self.env_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(self.env_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.startswith('TWITCH_OAUTH='):
                    file.write(f'TWITCH_OAUTH={self.oauth_token}\n')
                elif line.startswith('TWITCH_REFRESH_TOKEN='):
                    file.write(f'TWITCH_REFRESH_TOKEN={self.refresh_token}\n')
                else:
                    file.write(line)

    def _update_runtime_env(self):
        if self.oauth_token is not None:
            os.environ['TWITCH_OAUTH'] = self.oauth_token
        if self.refresh_token is not None:
            os.environ['TWITCH_REFRESH_TOKEN'] = self.refresh_token

    def get_oauth_token(self):
        return self.oauth_token