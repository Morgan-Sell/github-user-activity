# Global Variables
from src.event_strategy import (
    IssueCommentStrategy,
    IssueStrategy,
    PullRequestReviewStrategy,
    PullRequestStrategy,
    PushStrategy,
)

GITHUB_API_URL = "https://api.github.com/users/"
EVENT_TYPES = github_event_types = [
    "CommitCommentEvent",
    "CreateEvent",
    "DeleteEvent",
    "ForkEvent",
    "GollumEvent",
    "IssueCommentEvent",
    "IssuesEvent",
    "MemberEvent",
    "PublicEvent",
    "PullRequestEvent",
    "PullRequestReviewEvent",
    "PullRequestReviewCommentEvent",
    "PushEvent",
    "ReleaseEvent",
    "SponsorshipEvent",
    "WatchEvent",
]

EVENT_TYPE_ACTION_CROSSWALK = {
    "CommitCommentEvent": "Commented on ",
    "CreateEvent": "Created ",
    "DeleteEvent": "Deleted ",
    "ForkEvent": "Forked ",
    "GollumEvent": "Created or updated ",
    "IssueCommentEvent": "Commented on ",
    "IssuesEvent": "Open or closed ",
    "MemberEvent": "Added or removed ",
    "PublicEvent": "Changed a private repo to public",
    "PullRequestEvent": "Opened, closed, or merged: ",
    "PullRequestReviewEvent": "Reviewed ",
    "PullRequestReviewCommentEvent": "Commented on",
    "PushEvent": "Pushed ",
    "ReleaseEvent": "Released ",
    "SponsorshipEvent": "Sponsored ",
    "WatchEvent": "Starred ",
}

EVENT_TYPE_ACTION_COUNT_CROSSWALK = {
    "CommitCommentEvent": lambda num: f"Commented on {num} commits.",
    "CreateEvent": lambda num: f"Created {num} repos, branches, or tags.",
    "DeleteEvent": lambda num: f"Deleted {num} branches or tags.",
    "ForkEvent": lambda num: f"Forked {num} repos.",
    "GollumEvent": lambda num: f"Created or updated {num} wiki pages.",
    "IssueCommentEvent": lambda num: f"Commented on {num} issues or PRs.",
    "IssuesEvent": lambda num: f"Open or closed {num} issues.",
    "MemberEvent": (lambda num: f"Added or removed {num} times as a collaborator."),
    "PublicEvent": lambda num: f"Changed {num} repos from private to public.",
    "PullRequestEvent": lambda num: f"Opened, closed, or merged {num} PRs.",
    "PullRequestReviewEvent": lambda num: f"Reviewed {num} PRs.",
    "PullRequestReviewCommentEvent": (lambda num: f"Commented on {num} PR reviews."),
    "PushEvent": lambda num: f"Pushed {num} times.",
    "ReleaseEvent": lambda num: f"Created {num} new releases.",
    "SponsorshipEvent": lambda num: f"Sponsored {num} developers or projects.",
    "WatchEvent": lambda num: f"Starred {num} repos.",
}


EVENT_TYPES_TO_REVIEW = [
    "IssueCommentEvent",
    "IssuesEvent",
    "PullRequestEvent",
    "PullRequestReviewEvent",
    "PushEvent",
]


EVENT_TYPE_TO_EXTRACTION_STRATEGY_CROSSWALK = {
    "IssueCommentEvent": IssueStrategy(),
    "IssuesEvent": IssueCommentStrategy(),
    "PullRequestEvent": PullRequestStrategy(),
    "PullRequestReviewEvent": PullRequestReviewStrategy(),
    "PushEvent": PushStrategy(),
}
