import os
from typing import Dict, List

import requests
from dotenv import load_dotenv

from src.config import GITHUB_API_URL


def get_user_events(username: str, github_token: str) -> List[Dict]:

    headers = {"Authorization": f"token {github_token}"}
    url = f"{GITHUB_API_URL}{username}/events"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise Exception("GitHub token is invalid or has expired.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}.")


def get_user_events_by_type(
    username: str, github_token: str, event_type: str
) -> List[Dict]:

    events = get_user_events(username, github_token)
    filtered_events = [event for event in events if event["type"] == event_type]
    return filtered_events
