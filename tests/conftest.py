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


@pytest.fixture(scope="function")
def issue_comment_event():
    return {
        "id": "43034062954",
        "type": "IssueCommentEvent",
        "actor": {
            "id": 11805379,
            "login": "BiggieSmalls",
            "display_login": "BiggieSmalls",
            "gravatar_id": "",
            "url": "https://api.github.com/users/BiggieSmalls",
            "avatar_url": "https://avatars.githubusercontent.com/u/11805379?"
        },
        "repo": {
            "id": 163630824,
            "name": "bad-boy-records/juicy_beats",
            "url": "https://api.github.com/repos/bad-boy-records/juicy_beats"
        },
        "payload": {
            "action": "created",
            "issue": {
                "url": "https://api.github.com/repos/bad-boy-records/juicy_beats/issues/819",
                "repository_url": "https://api.github.com/repos/bad-boy-records/juicy_beats",
                "id": 2598228763,
                "number": 819,
                "title": "Hypnotize flow mismatch with RhymeDocs",
                "user": {
                    "login": "michaelrussell4",
                    "id": 37958894,
                    "node_id": "MDQ6VXNlcjM3OTU4ODk0",
                    "avatar_url": "https://avatars.githubusercontent.com/u/37958894?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/michaelrussell4",
                    "html_url": "https://github.com/michaelrussell4",
                    "followers_url": "https://api.github.com/users/michaelrussell4/followers",
                    "following_url": "https://api.github.com/users/michaelrussell4/following{/other_user}",
                    "gists_url": "https://api.github.com/users/michaelrussell4/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/michaelrussell4/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/michaelrussell4/subscriptions",
                    "organizations_url": "https://api.github.com/users/michaelrussell4/orgs",
                    "repos_url": "https://api.github.com/users/michaelrussell4/repos",
                    "events_url": "https://api.github.com/users/michaelrussell4/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/michaelrussell4/received_events",
                    "type": "User",
                    "user_view_type": "public",
                    "site_admin": False,
                },
                "state": "closed",
                "comments": 1,
                "created_at": datetime(2024, 10, 18, 19, 21, 3),
                "updated_at": datetime(2024, 10, 21, 7, 0, 28),
                "closed_at": datetime(2024, 10, 21, 7, 0, 28),
                "author_association": "CONTRIBUTOR",
                "body": "Yo, yo, check it. The rhyme was off, so I flipped the script. 'Raise' to 'ignore', it’s the real deal now.",
            },
            "comment": {
                "id": 2425785881,
                "user": {
                    "login": "BiggieSmalls",
                    "id": 11805379,
                    "avatar_url": "https://avatars.githubusercontent.com/u/11805379?v=4"
                },
                "created_at": datetime(2024, 10, 21, 7, 0, 28),
                "body": "Much love for spotting that, @BiggieSmalls. We got it locked down, for real!",
            }
        },
        "created_at": datetime(2024, 10, 21, 7, 0, 30)
    }


@pytest.fixture(scope="function")
def issue_event():
    return {
        "id": "43034062212",
        "type": "IssuesEvent",
        "actor": {
            "id": 11805379,
            "login": "BiggieSmalls",
            "display_login": "BiggieSmalls",
            "gravatar_id": "",
            "url": "https://api.github.com/users/BiggieSmalls",
            "avatar_url": "https://avatars.githubusercontent.com/u/11805379?"
        },
        "repo": {
            "id": 163630824,
            "name": "bad-boy-records/juicy_beats",
            "url": "https://api.github.com/repos/bad-boy-records/juicy_beats"
        },
        "payload": {
            "action": "closed",
            "issue": {
                "url": "https://api.github.com/repos/bad-boy-records/juicy_beats/issues/820",
                "repository_url": "https://api.github.com/repos/bad-boy-records/juicy_beats",
                "id": 2598228764,
                "number": 820,
                "title": "Juicy hook needs flow correction",
                "user": {
                    "login": "michaelrussell4",
                    "id": 37958894,
                    "node_id": "MDQ6VXNlcjM3OTU4ODk0",
                    "avatar_url": "https://avatars.githubusercontent.com/u/37958894?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/michaelrussell4",
                    "html_url": "https://github.com/michaelrussell4",
                    "followers_url": "https://api.github.com/users/michaelrussell4/followers",
                    "following_url": "https://api.github.com/users/michaelrussell4/following{/other_user}",
                    "gists_url": "https://api.github.com/users/michaelrussell4/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/michaelrussell4/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/michaelrussell4/subscriptions",
                    "organizations_url": "https://api.github.com/users/michaelrussell4/orgs",
                    "repos_url": "https://api.github.com/users/michaelrussell4/repos",
                    "events_url": "https://api.github.com/users/michaelrussell4/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/michaelrussell4/received_events",
                    "type": "User",
                    "user_view_type": "public",
                    "site_admin": False
                },
                "state": "closed",
                "created_at": datetime(2024, 10, 18, 19, 22, 8),
                "updated_at": datetime(2024, 10, 21, 6, 58, 31),
                "closed_at": datetime(2024, 10, 21, 6, 58, 31),
                "author_association": "CONTRIBUTOR",
                "body": "We had to fix that flow. 'Raise' wasn’t fitting the vibe, so we smoothed it out to 'ignore'. Juicy!",
            }
        },
        "created_at": datetime(2024, 10, 21, 6, 58, 32)
    }

@pytest.fixture(scope="function")
def pull_request_review_event():
    return {
        "id": "43034004711",
        "type": "PullRequestReviewEvent",
        "actor": {
            "id": 18749382,
            "login": "TupacShakur",
            "display_login": "TupacShakur",
            "gravatar_id": "",
            "url": "https://api.github.com/users/TupacShakur",
            "avatar_url": "https://avatars.githubusercontent.com/u/18749382?"
        },
        "repo": {
            "id": 543210987,
            "name": "death-row-records/all_eyez_on_code",
            "url": "https://api.github.com/repos/death-row-records/all_eyez_on_code"
        },
        "payload": {
            "action": "submitted",
            "pull_request": {
                "url": "https://api.github.com/repos/death-row-records/all_eyez_on_code/pulls/96",
                "id": 876543210,
                "node_id": "PR_kwDOCx85nM5z3WIG",
                "html_url": "https://github.com/death-row-records/all_eyez_on_code/pull/96",
                "diff_url": "https://github.com/death-row-records/all_eyez_on_code/pull/96.diff",
                "patch_url": "https://github.com/death-row-records/all_eyez_on_code/pull/96.patch",
                "issue_url": "https://api.github.com/repos/death-row-records/all_eyez_on_code/issues/96",
                "number": 96,
                "state": "open",
                "locked": False,
                "title": "Fix for California Love flow mismatch",
                "user": {
                    "login": "SnoopDogg",
                    "id": 19348283,
                    "avatar_url": "https://avatars.githubusercontent.com/u/19348283?"
                },
                "created_at": datetime(2024, 10, 19, 18, 34, 27),
                "updated_at": datetime(2024, 10, 21, 8, 12, 44),
                "body": "This pull request cleans up the flow to make sure 'California Love' hits harder.",
            },
            "review": {
                "id": 54321987,
                "user": {
                    "login": "TupacShakur",
                    "id": 18749382,
                    "avatar_url": "https://avatars.githubusercontent.com/u/18749382?"
                },
                "body": "Yo, this is tight. Flow’s on point now, let's get it!",
                "submitted_at": datetime(2024, 10, 21, 8, 14, 10),
                "state": "approved"
            }
        },
        "created_at": datetime(2024, 10, 21, 8, 14, 11)
    }
