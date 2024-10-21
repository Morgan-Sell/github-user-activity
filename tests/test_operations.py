import pytest

from src.operations import (
    convert_event_counter_to_descriptions,
    count_events_by_type,
    is_valid_event_type_to_review,
)


def test_count_events_by_type(github_events_complex):
    # Arrange
    data = github_events_complex

    # Action
    events_counted = count_events_by_type(data)

    # Assert
    expected_results = {
        "ForkEvent": 2,
        "PushEvent": 3,
        "PullRequestEvent": 2,
    }
    assert events_counted == expected_results


def test_convert_event_counter_to_descriptions():
    # Arrange
    event_types = {
        "ForkEvent": 2,
        "PushEvent": 3,
        "PullRequestEvent": 2,
    }

    # Action
    descriptions = convert_event_counter_to_descriptions(event_types)

    # Assert
    assert isinstance(descriptions, list)
    assert len(descriptions) == 3
    assert descriptions[0] == "Forked 2 repos."
    assert descriptions[1] == "Pushed 3 times."
    assert descriptions[2] == "Opened, closed, or merged 2 PRs."


@pytest.mark.parametrize(
    argnames="event_type, is_valid",
    argvalues=[
        ("PushEvent", True),
        ("ScratchHeadEvent", False),
        ("ForkEvent", False),
        ("PullRequestReviewEvent", True),
        (369, False),
    ],
)
def test_is_valid_event_type_to_review(event_type, is_valid):
    assert is_valid_event_type_to_review(event_type) == is_valid
