import os
from typing import Dict, List

import requests
from dotenv import load_dotenv

from src.config import GITHUB_API_URL


def get_github_user_events(username: str, github_token: str) -> List[Dict]:

    headers = {"Authorization": f"token {github_token}"}
    url = f"{GITHUB_API_URL}{username}/events"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        raise Exception(f"API request failed with status code {response.status_code}.")
