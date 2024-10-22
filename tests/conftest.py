from datetime import datetime, timedelta

import pytest


@pytest.fixture(scope="function")
def github_events_simple():
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


@pytest.fixture(scope="function")
def github_events_complex():
    return [
        {
            "id": "101",
            "type": "ForkEvent",
            "actor": {
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "avatar_url": "https://simpsons-avatar.com/homer.png",
            },
            "repo": {
                "name": "homer-simpson/donut-inventory",
                "url": "https://github.com/homer-simpson/donut-inventory",
            },
            "payload": {"forkee": {"full_name": "homer-simpson/donut-inventory-fork"}},
            "public": True,
            "created_at": "2024-10-20T08:30:00Z",
        },
        {
            "id": "102",
            "type": "PushEvent",
            "actor": {
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "avatar_url": "https://simpsons-avatar.com/bart.png",
            },
            "repo": {
                "name": "bart-simpson/skateboard-tricks",
                "url": "https://github.com/bart-simpson/skateboard-tricks",
            },
            "payload": {
                "size": 2,
                "commits": [
                    {
                        "sha": "abc123",
                        "message": "Added 'Cowabunga!' to the README",
                        "url": "https://github.com/bart-simpson/skateboard-tricks/commit/abc123",
                    }
                ],
            },
            "public": True,
            "created_at": "2024-10-20T09:00:00Z",
        },
        {
            "id": "103",
            "type": "PullRequestEvent",
            "actor": {
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "avatar_url": "https://simpsons-avatar.com/homer.png",
            },
            "repo": {
                "name": "homer-simpson/donut-inventory",
                "url": "https://github.com/homer-simpson/donut-inventory",
            },
            "payload": {
                "action": "opened",
                "pull_request": {
                    "url": "https://github.com/homer-simpson/donut-inventory/pull/1",
                    "title": "Added 'Mmm... Donuts' feature",
                    "state": "open",
                    "merged": False,
                },
            },
            "public": True,
            "created_at": "2024-10-20T10:00:00Z",
        },
        {
            "id": "104",
            "type": "PushEvent",
            "actor": {
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "avatar_url": "https://simpsons-avatar.com/bart.png",
            },
            "repo": {
                "name": "bart-simpson/prank-code",
                "url": "https://github.com/bart-simpson/prank-code",
            },
            "payload": {
                "size": 1,
                "commits": [
                    {
                        "sha": "xyz789",
                        "message": "Implemented prank: Replace 'Principal Skinner's coffee with cola'",
                        "url": "https://github.com/bart-simpson/prank-code/commit/xyz789",
                    }
                ],
            },
            "public": True,
            "created_at": "2024-10-20T11:00:00Z",
        },
        {
            "id": "105",
            "type": "PullRequestEvent",
            "actor": {
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "avatar_url": "https://simpsons-avatar.com/bart.png",
            },
            "repo": {
                "name": "bart-simpson/slingshot",
                "url": "https://github.com/bart-simpson/slingshot",
            },
            "payload": {
                "action": "closed",
                "pull_request": {
                    "url": "https://github.com/bart-simpson/slingshot/pull/42",
                    "title": "Upgrade slingshot to fire tomatoes",
                    "state": "closed",
                    "merged": True,
                },
            },
            "public": True,
            "created_at": "2024-10-20T12:00:00Z",
        },
        {
            "id": "106",
            "type": "ForkEvent",
            "actor": {
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "avatar_url": "https://simpsons-avatar.com/bart.png",
            },
            "repo": {
                "name": "bart-simpson/chalkboard-gags",
                "url": "https://github.com/bart-simpson/chalkboard-gags",
            },
            "payload": {"forkee": {"full_name": "bart-simpson/chalkboard-gags-fork"}},
            "public": True,
            "created_at": "2024-10-20T13:00:00Z",
        },
        {
            "id": "107",
            "type": "PushEvent",
            "actor": {
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "avatar_url": "https://simpsons-avatar.com/homer.png",
            },
            "repo": {
                "name": "homer-simpson/sofa-snacks",
                "url": "https://github.com/homer-simpson/sofa-snacks",
            },
            "payload": {
                "size": 1,
                "commits": [
                    {
                        "sha": "456def",
                        "message": "Added 'TV remote holder next to the sofa' feature",
                        "url": "https://github.com/homer-simpson/sofa-snacks/commit/456def",
                    }
                ],
            },
            "public": True,
            "created_at": "2024-10-20T14:00:00Z",
        },
    ]
