import pytest



@pytest.fixture(scope="function")
def github_events():
    return [
        {"type": "PushEvent", "created_at": "2024-01-01T00:00:00Z"},
        {"type": "PullRequestEvent", "created_at": "2024-01-02T00:00:00Z"},
        {"type": "IssuesEvent", "created_at": "2024-01-03T00:00:00Z"},
        {"type": "PushEvent", "created_at": "2024-01-04T00:00:00Z"},
        {"type": "PullRequestEvent", "created_at": "2024-01-05T00:00:00Z"},
        {"type": "IssuesEvent", "created_at": "2024-01-06T00:00:00Z"},
        {"type": "PushEvent", "created_at": "2024-01-07T00:00:00Z"},
        {"type": "PullRequestEvent", "created_at": "2024-01-08T00:00:00Z"},
        {"type": "IssuesEvent", "created_at": "2024-01-09T00:00:00Z"},
        {"type": "PushEvent", "created_at": "2024-01-10T00:00:00Z"},
    ]