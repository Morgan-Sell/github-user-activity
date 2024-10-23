import pytest

from src.operations import (
    collect_events_based_on_event_type,
    convert_event_counter_to_descriptions,
    count_events_by_type,
    is_valid_event_type_to_review,
    prepare_data_for_tabulate,
    print_table,
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


def test_collect_event_type_details_for_review(github_events_complex):
    # Arrange
    events_data = github_events_complex

    # Action
    results = collect_events_based_on_event_type(events_data, "ForkEvent")

    # Assert
    expected_results = [events_data[0], events_data[5]]
    assert results == expected_results


def test_prepare_data_for_tabulate(github_events_complex):
    # Arrange
    all_events = github_events_complex
    event_type = "PullRequestEvent"
    event_data = [event for event in all_events if event["type"] == event_type]

    # Action
    results = prepare_data_for_tabulate(event_data, event_type)

    # Assert
    expected_results = [
        [
            "103",
            "homer-simpson/donut-inventory",
            "Added 'Mmm... Donuts' feature",
            "opened",
            "n/a",
            "2024-10-20T10:00:00Z",
        ],
        [
            "105",
            "bart-simpson/slingshot",
            "Upgrade slingshot to fire tomatoes",
            "closed",
            "n/a",
            "2024-10-20T12:00:00Z",
        ],
    ]
    assert results == expected_results


from typing import List

import pytest
from tabulate import tabulate

# Assuming print_table is already defined or imported


@pytest.mark.parametrize(
    "data, headers, expected_error_message",
    [
        # Test case 1: No data provided (empty list)
        ([], ["ID", "Name", "Age"], "No data was provided to generate table."),
        # Test case 2: Mismatch between number of attributes and headers
        (
            [["1", "Alice"]],
            ["ID", "Name", "Age"],
            "Number of attributes does not equal the number of column headers. "
            "There are 2 attributes and 3 column headers.",
        ),
    ],
)
def test_print_table_errors(data, headers, expected_error_message):
    # Action & Assert
    with pytest.raises(ValueError, match=expected_error_message):
        print_table(data, headers)
