from unittest.mock import patch

import pytest

from src.api import get_github_user_events


@patch("requests.get")
def test_get_github_user_events_success(mock_get, github_events):
    # Arrange: mock a successful response
    mock_response = {
        "status_code": 200,
        # use lambda to create a callable function that mimics requests.Response.json()
        "json": lambda: github_events,
    }
    mock_get.return_value = type("MockResponse", (object,), mock_response)

    username = "da-vinci"
    github_token = "mona_lisa"

    # Act
    events = get_github_user_events(username, github_token)

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


@patch("requests.get")
def test_get_github_user_events_raises_exception(mock_get):
    # Arrange: mock a failed response
    mock_response = {"status_code": 404, "json": lambda: {"message": "Not Found"}}
    mock_get.return_value = type("MockResponse", (object,), mock_response)

    username = "internet_troll"
    github_token = "scam_token"

    # Action & Assert
    expected_result = f"API request failed with status code 404."
    with pytest.raises(Exception, match=expected_result):
        get_github_user_events(username, github_token)


@patch("requests.get")
def test_get_github_user_events_by_type_success(mock_get):
    pass