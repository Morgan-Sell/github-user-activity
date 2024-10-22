import pytest
from src.event_strategy import (
    IssueCommentStrategy,
    EventType,
    IssueStrategy,
    PullRequestReviewStrategy,
    PullRequestStrategy,
    PushStrategy,
)


def datetime_to_iso8601(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# -- IssueCommentStrategy Test Cases --
def test_issue_comment_get_event_id(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert event.get_event_id() == "43034062954"


def test_issue_comment_get_repo_name(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert event.get_repo_name() == "bad-boy-records/juicy_beats"


def test_issue_comment_get_title(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert event.get_title() == "Hypnotize flow mismatch with RhymeDocs"


def test_issue_comment_get_action(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert event.get_action() == "created"


def test_issue_comment_get_recipient(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert event.get_recipient() == "michaelrussell4"


def test_issue_comment_get_created_date(issue_comment_event):
    strategy = IssueCommentStrategy()
    event = EventType(issue_comment_event, strategy)
    assert datetime_to_iso8601(event.get_created_date()) == "2024-10-21T07:00:30Z"


# -- IssueStrategy Test Cases --
def test_issue_get_event_id(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert event.get_event_id() == "43034062212"


def test_issue_get_repo_name(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert event.get_repo_name() == "bad-boy-records/juicy_beats"


def test_issue_get_title(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert event.get_title() == "Juicy hook needs flow correction"


def test_issue_get_action(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert event.get_action() == "closed"


def test_issue_get_recipient(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert event.get_recipient() == "michaelrussell4"


def test_issue_get_created_date(issue_event):
    strategy = IssueStrategy()
    event = EventType(issue_event, strategy)
    assert datetime_to_iso8601(event.get_created_date()) == "2024-10-21T06:58:32Z"


# -- PullRequestStrategy Test Cases --
def test_pull_request_get_event_id(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_event_id() == "103"


def test_pull_request_get_repo_name(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_repo_name() == "homer-simpson/donut-inventory"


def test_pull_request_get_title(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_title() == "Added 'Mmm... Donuts' feature"


def test_pull_request_get_action(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_action() == "opened"


def test_pull_request_get_recipient(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_recipient() == "n/a"


def test_pull_request_get_created_date(github_events_complex):
    strategy = PullRequestStrategy()
    event = EventType(github_events_complex[2], strategy)
    assert event.get_created_date() == "2024-10-20T10:00:00Z"


# -- PullRequestReviewStrategy Test Cases --
def test_pull_request_review_get_event_id(pull_request_review_event):
    strategy = PullRequestReviewStrategy()
    event = EventType(pull_request_review_event, strategy)
    assert event.get_event_id() == "43034004711"

def test_pull_request_review_get_repo_name(pull_request_review_event):
    strategy = PullRequestReviewStrategy()
    event = EventType(pull_request_review_event, strategy)
    assert event.get_repo_name() == "death-row-records/all_eyez_on_code"

def test_pull_request_review_get_title(pull_request_review_event):
    strategy = PullRequestReviewStrategy()
    event = EventType(pull_request_review_event, strategy)
    assert event.get_title() == "Fix for California Love flow mismatch"

def test_pull_request_review_get_action(pull_request_review_event):
    strategy = PullRequestReviewStrategy()
    event = EventType(pull_request_review_event, strategy)
    assert event.get_action() == "submitted"

def test_pull_request_review_get_recipient(pull_request_review_event):
    strategy = PullRequestReviewStrategy()
    event = EventType(pull_request_review_event, strategy)
    assert event.get_recipient() == "SnoopDogg"


## -- PushStrategy Test Cases --
def test_push_get_event_id(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_event_id() == "104"

def test_push_get_repo_name(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_repo_name() == "bart-simpson/prank-code"

def test_push_get_title(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_title() == "Implemented prank: Replace 'Principal Skinner's coffee with cola'"

def test_push_get_action(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_action() == "n/a"

def test_push_get_recipient(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_recipient() == "n/a"

def test_push_get_created_date(github_events_complex):
    strategy = PushStrategy()
    event = EventType(github_events_complex[3], strategy)
    assert event.get_created_date() == "2024-10-20T11:00:00Z"