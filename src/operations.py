from typing import Any, Dict, List

from tabulate import tabulate

from src.config import (
    EVENT_TYPE_ACTION_COUNT_CROSSWALK,
    EVENT_TYPE_TO_EXTRACTION_STRATEGY_CROSSWALK,
    EVENT_TYPES,
    EVENT_TYPES_TO_REVIEW,
)
from src.event_strategy import EventType


def count_events_by_type(events: List[Dict]) -> Dict[str, int]:
    """
    Count the occurrences of each event type in the given list of events.

    Args:
        events (List[Dict]): List of event dictionaries containing an event type.

    Returns:
        Dict[str, int]: A dictionary where keys are event types and values are their counts.
    """
    counter = {}

    for event in events:
        current_event_type = event["type"]
        if current_event_type in counter.keys():
            counter[current_event_type] += 1
        else:
            counter[current_event_type] = 1

    return counter


def convert_event_counter_to_descriptions(event_type_counter: Dict) -> List[str]:
    """
    Convert the event type counts to human-readable descriptions.

    Args:
        event_type_counter (Dict): A dictionary with event types as keys and their counts as values.

    Returns:
        List[str]: A list of descriptive strings based on the event counts.
    """
    descriptions = []

    for event_type, count in event_type_counter.items():
        desc = EVENT_TYPE_ACTION_COUNT_CROSSWALK[event_type](count)
        descriptions.append(desc)

    return descriptions


def is_valid_event_type_to_review(event_type: str) -> bool:
    """
    Check if the provided event type is valid for review.

    Args:
        event_type (str): The event type to validate.

    Returns:
        bool: True if the event type is valid, False otherwise with a warning message.
    """
    if event_type in EVENT_TYPES_TO_REVIEW:
        return True
    else:
        print("Entered invalid event type. See README for " "acceptable event types.")
        return False


def collect_events_based_on_event_type(
    event_data: list, event_type: str
) -> List[Dict[Any, Any]]:
    """
    Collect events from event_data that match the specified event_type.

    Args:
        event_data (list): List of event dictionaries containing various event details.
        event_type (str): The event type to filter by.

    Returns:
        List[Dict[Any, Any]]: A list of dictionaries where each dictionary represents an event that matches the event_type.
    """
    events_to_review = []

    for event in event_data:
        if event["type"] == event_type:
            events_to_review.append(event)

    return events_to_review


def prepare_data_for_tabulate(data: List[Dict], event_type: str) -> List[List[str]]:
    """
    Prepare event data for tabulation by extracting relevant fields based on event_type.

    Args:
        data (List[Dict]): List of event dictionaries to be prepared for tabulation.
        event_type (str): The event type that determines the extraction strategy.

    Returns:
        List[List[str]]: A list of lists where each inner list contains the string
                         representation of event details (e.g., event ID, repo name,
                         title, etc.) for tabulation.
    """
    strategy = EVENT_TYPE_TO_EXTRACTION_STRATEGY_CROSSWALK[event_type]

    events_to_review = []

    for event in data:
        tmp_event = EventType(event_data=event, extraction_strategy=strategy)

        tmp_event_data = [
            tmp_event.get_event_id(),
            tmp_event.get_repo_name(),
            tmp_event.get_title(),
            tmp_event.get_action(),
            tmp_event.get_recipient(),
            tmp_event.get_created_date(),
        ]

        events_to_review.append(tmp_event_data)

    return events_to_review


def print_table(data: List[List[str]], headers: List[str]) -> None:
    """
    Print a formatted table using the provided data and headers.

    Args:
        data (List[List[str]]): The table data to be printed, where each
                                inner list represents a row of values.
        headers (List[str]): The column headers for the table.

    Raises:
        ValueError: If no data is provided or if the number of attributes
                    does not match the number of headers.
    """
    if len(data) == 0:
        raise ValueError("No data was provided to generate table.")

    if len(data[0]) != len(headers):
        raise ValueError(
            "Number of attributes does not equal the number of column headers. "
            f"There are {len(data[0])} attributes and {len(headers)} column headers."
        )

    table = tabulate(data, headers=headers, tablefmt="pretty")
    print(table)
