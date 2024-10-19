from unittest.mock import patch

import pytest

from src.api import get_user_events, get_user_events_by_type


@patch("requests.get")
def test_get_user_events_success(mock_get, github_events):
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


@patch("requests.get")
def test_get_user_events_raises_exception(mock_get):
    # Arrange: mock a failed response
    mock_response = {"status_code": 404, "json": lambda: {"message": "Not Found"}}
    mock_get.return_value = type("MockResponse", (object,), mock_response)

    username = "internet_troll"
    github_token = "scam_token"

    # Action & Assert
    expected_result = f"API request failed with status code 404."
    with pytest.raises(Exception, match=expected_result):
        get_user_events(username, github_token)


@patch("requests.get")
def test_get_user_events_by_type_success(mock_get, github_events):
    # Arrange: mock a successful response
    mock_response = {
        "status_code": 200,
        "json": lambda: github_events,
    }
    mock_get.return_value = type("MockResponse", (object,), mock_response)
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


@patch("requests.get")
def test_get_user_events_by_type_raises_401_exception(mock_get):
    # Arrange: mock an invalid token response
    mock_response = {
        "status_code": 401,
        "json": lambda: {"message": "Not Authorized"},
    }
    mock_get.return_value = type("MockResponse", (object,), mock_response)
    username = "ai_bot"
    github_token = "fake_token"
    event_type = "PullRequestEvent"

    # Action & Assert
    expected_result = "GitHub token is invalid or has expired."
    with pytest.raises(Exception, match=expected_result):
        get_user_events_by_type(username, github_token, event_type)
