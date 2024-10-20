import pytest
from datetime import datetime, timedelta

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
            "id": "123456789",
            "type": "ForkEvent",
            "actor": {
                "id": 1001,
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "url": "https://api.github.com/users/homer-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1001?"
            },
            "repo": {
                "id": 555,
                "name": "MrBurns/Nuclear-Safety",
                "url": "https://api.github.com/repos/MrBurns/Nuclear-Safety"
            },
            "payload": {
                "forkee": {
                    "id": 12345,
                    "name": "homer-simpson/Nuclear-Safety",
                    "full_name": "homer-simpson/Nuclear-Safety"
                }
            },
            "public": True,
            "created_at": "2024-10-15T03:05:45.835922",
        },
        {
            "id": "987654321",
            "type": "PullRequestEvent",
            "actor": {
                "id": 1002,
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "url": "https://api.github.com/users/bart-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1002?"
            },
            "repo": {
                "id": 777,
                "name": "KrustyBurger/NewMenu",
                "url": "https://api.github.com/repos/KrustyBurger/NewMenu"
            },
            "payload": {
                "action": "opened",
                "pull_request": {
                    "url": "https://api.github.com/repos/KrustyBurger/NewMenu/pulls/1",
                    "number": 1,
                    "state": "open",
                    "title": "Add new prank burger: The Flaming Moe",
                    "created_at": "2024-10-10T03:05:45.835932"
                }
            },
            "public": True,
            "created_at": "2024-10-10T03:05:45.835932",
        },
        {
            "id": "564738291",
            "type": "PushEvent",
            "actor": {
                "id": 1001,
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "url": "https://api.github.com/users/homer-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1001?"
            },
            "repo": {
                "id": 888,
                "name": "DuffBeer/ProductionLine",
                "url": "https://api.github.com/repos/DuffBeer/ProductionLine"
            },
            "payload": {
                "ref": "refs/heads/main",
                "commits": [
                    {
                        "sha": "abcd1234",
                        "message": "Added quality checks for beer cans",
                        "author": {
                            "email": "homer@springfield.com",
                            "name": "Homer Simpson"
                        }
                    }
                ]
            },
            "public": True,
            "created_at": "2024-10-05T03:05:45.835935",
        },
        {
            "id": "234567890",
            "type": "PullRequestEvent",
            "actor": {
                "id": 1002,
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "url": "https://api.github.com/users/bart-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1002?"
            },
            "repo": {
                "id": 999,
                "name": "SpringfieldElementary/PrankManual",
                "url": "https://api.github.com/repos/SpringfieldElementary/PrankManual"
            },
            "payload": {
                "action": "closed",
                "pull_request": {
                    "url": "https://api.github.com/repos/SpringfieldElementary/PrankManual/pulls/5",
                    "number": 5,
                    "state": "closed",
                    "title": "Add prank for glueing principal's chair",
                    "merged": True,
                    "created_at": "2024-09-30T03:05:45.835938"
                }
            },
            "public": True,
            "created_at": "2024-09-30T03:05:45.835938",
        },
        {
            "id": "345678912",
            "type": "PushEvent",
            "actor": {
                "id": 1002,
                "login": "bart-simpson",
                "display_login": "bart-simpson",
                "url": "https://api.github.com/users/bart-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1002?"
            },
            "repo": {
                "id": 444,
                "name": "BartSimpson/SprayPaintArt",
                "url": "https://api.github.com/repos/BartSimpson/SprayPaintArt"
            },
            "payload": {
                "ref": "refs/heads/main",
                "commits": [
                    {
                        "sha": "efgh5678",
                        "message": "Added 'Eat My Shorts' graffiti design",
                        "author": {
                            "email": "bart@springfield.com",
                            "name": "Bart Simpson"
                        }
                    }
                ]
            },
            "public": True,
            "created_at": "2024-09-25T03:05:45.835940",
        },
        {
            "id": "456789012",
            "type": "ForkEvent",
            "actor": {
                "id": 1001,
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "url": "https://api.github.com/users/homer-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1001?"
            },
            "repo": {
                "id": 555,
                "name": "NedFlanders/Leftorium",
                "url": "https://api.github.com/repos/NedFlanders/Leftorium"
            },
            "payload": {
                "forkee": {
                    "id": 67890,
                    "name": "homer-simpson/Leftorium",
                    "full_name": "homer-simpson/Leftorium"
                }
            },
            "public": True,
            "created_at": "2024-09-20T03:05:45.835942",
        },
        {
            "id": "567890123",
            "type": "PushEvent",
            "actor": {
                "id": 1001,
                "login": "homer-simpson",
                "display_login": "homer-simpson",
                "url": "https://api.github.com/users/homer-simpson",
                "avatar_url": "https://avatars.githubusercontent.com/u/1001?"
            },
            "repo": {
                "id": 666,
                "name": "SimpsonHousehold/DIYProjects",
                "url": "https://api.github.com/repos/SimpsonHousehold/DIYProjects"
            },
            "payload": {
                "ref": "refs/heads/main",
                "commits": [
                    {
                        "sha": "ijkl9012",
                        "message": "Repaired the roof after Bart's skateboard stunt",
                        "author": {
                            "email": "homer@springfield.com",
                            "name": "Homer Simpson"
                        }
                    }
                ]
            },
            "public": True,
            "created_at": "2024-09-15T03:05:45.835944",
        }
    ]
