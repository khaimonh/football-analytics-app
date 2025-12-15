import os
import yaml
from dotenv import load_dotenv
from pathlib import Path

# Load the secret .env file immediately
load_dotenv()

class Config:
    def __init__(self):
        self._config = self._load_yaml()

    def _load_yaml(self):
        # Assumes config.yml is in the root directory
        config_path = Path("config.yml")
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def get(self, key_path):
        """
        Allows you to do config.get('api.base_url')
        """
        keys = key_path.split('.')
        value = self._config
        for key in keys:
            value = value.get(key)
            if value is None:
                return None
        return value

    def get_api_key(self):
        key = os.getenv("API_FOOTBALL_KEY")
        if not key:
            raise ValueError("API Key not found! Check your .env file.")
        return key