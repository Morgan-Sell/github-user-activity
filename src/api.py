import json
import os
from typing import Any, Dict, List
from urllib import error, parse, request

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
    """
    Fetch the recent public events for a GitHub user.

    Args:
        username (str): GitHub username whose events are being fetched.
        github_token (str): GitHub API token for authentication.

    Returns:
        List[Dict]: A list of dictionaries containing the user's recent events.

    Raises:
        UnauthorizedError: If the GitHub token is invalid or unauthorized.
        UsernameNotFoundError: If the username does not exist on GitHub.
        GitHubAPIError: For other HTTP errors returned by the GitHub API.
        APIConnectionError: If there is a connection issue with the GitHub API.
        JSONParseError: If there is an error parsing the JSON response.
        UnhandledError: For any other unexpected errors.
    """
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
) -> List[Dict[Any, Any]]:
    """
    Fetch and filter GitHub user events by event type.

    Args:
        username (str): GitHub username whose events are being fetched.
        github_token (str): GitHub API token for authentication.
        event_type (str): The type of event to filter by.

    Returns:
        List[Dict[Any, Any]]: A list of dictionaries containing events of the
                              specified type.
    """
    events = get_user_events(username, github_token)
    filtered_events = [event for event in events if event["type"] == event_type]
    return filtered_events
