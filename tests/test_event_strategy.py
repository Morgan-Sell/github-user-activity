import pytest
from src.event_strategy import IssueCommentStrategy, EventType, IssueStrategy


def datetime_to_iso8601(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

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