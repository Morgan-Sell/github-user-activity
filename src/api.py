import os
from typing import Dict, List

import json
from urllib import request, error, parse

from src.config import GITHUB_API_URL
from src.custom_errors import (
    APIConnectionError,
    GitHubAPIError,
    JSONParseError,
    UnauthorizedError,
    UnhandledError,
    UsernameNotFoundError,
)


def get_user_events(username: str, github_token: str) -> List[Dict]:
    # create request object with token
    base_url = f"{GITHUB_API_URL}{username}/events"
    params = {"per_page": 100}
    query_string = parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    req = request.Request(url)
    req.add_header("Authorization", f"token {github_token}")

    try:
        with request.urlopen(req) as response:
            data = response.read()
            events = json.loads(data)

        return events

    except error.HTTPError as e:
        print("Error code: ", e.code)
        if e.code == 401:
            raise UnauthorizedError("Unauthorized: Check your GitHub token.")
        elif e.code == 404:
            raise UsernameNotFoundError(f"Username {username} does not exist.")
        else:
            raise GitHubAPIError(f"HTTP error: {e.code} {e.reason}")

    except error.URLError as e:
        print("Error code: ", e.code)
        raise APIConnectionError(f"Connection error: {e.reason}")

    except error.JSONDecodeError as e:
        print("Error code: ", e.code)
        raise JSONParseError(f"JSON parsing error: {e}")

    except Exception as e:
        print("Error code: ", e.code)
        raise UnhandledError(f"An unexpected error occured: {e}")


def get_user_events_by_type(
    username: str, github_token: str, event_type: str
) -> List[Dict]:

    events = get_user_events(username, github_token)
    filtered_events = [event for event in events if event["type"] == event_type]
    return filtered_events
