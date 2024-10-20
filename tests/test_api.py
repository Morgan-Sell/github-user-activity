import json
from unittest.mock import MagicMock, patch
import urllib
import pytest

from src.api import get_user_events, get_user_events_by_type
from src.custom_errors import UnauthorizedError, UsernameNotFoundError


@patch("urllib.request.urlopen")
def test_get_user_events_success(mock_urlopen, github_events):
    # Arrange: mock a successful response
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(github_events).encode("utf-8")
    # To support 'with' statement
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.return_value = mock_response

    username = "da-vinci"
    github_token = "mona_lisa"

    # Act
    events = get_user_events(username, github_token)

    # Assert
    assert isinstance(events, list)
    assert len(events) == 10

    # Verify first 3 events
    assert events[0]["type"] == "PushEvent"
    assert events[0]["created_at"] == "2024-01-01T00:00:00Z"

    assert events[1]["type"] == "PullRequestEvent"
    assert events[1]["created_at"] == "2024-01-02T00:00:00Z"

    assert events[2]["type"] == "IssuesEvent"
    assert events[2]["created_at"] == "2024-01-03T00:00:00Z"


@patch("urllib.request.urlopen")
def test_get_user_events_raises_404_exception(mock_urlopen):
    # Arrange: mock a failed response
    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="https://api.github.com/users/internet_troll/events",
        code=404,
        msg="Not Found",
        hdrs=None,
        fp=None
    )

    username = "internet_troll"
    github_token = "scam_token"

    # Action & Assert
    # expected_result = f"API request failed with status code 404."
    with pytest.raises(UsernameNotFoundError):
        get_user_events(username, github_token)


@patch("urllib.request.urlopen")
def test_get_user_events_by_type_success(mock_urlopen, github_events):
    # Arrange: mock a successful response
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(github_events).encode("utf-8")
    # To support 'with' statement
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.return_value = mock_response

    username = "van-gogh"
    github_token = "missing_ear"
    event_type = "IssuesEvent"

    # Action
    events = get_user_events_by_type(username, github_token, event_type)

    # Assert
    assert isinstance(events, list)
    assert len(events) == 3

    # Verify the events
    assert events[0]["type"] == "IssuesEvent"
    assert events[0]["created_at"] == "2024-01-03T00:00:00Z"

    assert events[1]["type"] == "IssuesEvent"
    assert events[1]["created_at"] == "2024-01-06T00:00:00Z"

    assert events[2]["type"] == "IssuesEvent"
    assert events[2]["created_at"] == "2024-01-09T00:00:00Z"


@patch("urllib.request.urlopen")
def test_get_user_events_by_type_raises_401_exception(mock_urlopen):
    # Arrange: mock an invalid token response
    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="https://api.github.com/users/ai_bot/events",
        code=401,
        msg="Unauthorized",
        hdrs=None,
        fp=None
    )

    username = "ai_bot"
    github_token = "fake_token"
    event_type = "PullRequestEvent"

    # Action & Assert
    # expected_result = "GitHub token is invalid or has expired."
    with pytest.raises(UnauthorizedError):
        get_user_events_by_type(username, github_token, event_type)
