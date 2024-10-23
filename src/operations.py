from typing import Dict, List

from tabulate import tabulate

from src.config import (
    EVENT_TYPE_ACTION_COUNT_CROSSWALK,
    EVENT_TYPE_TO_EXTRACTION_STRATEGY_CROSSWALK,
    EVENT_TYPES,
    EVENT_TYPES_TO_REVIEW,
)
from src.event_strategy import EventType


def count_events_by_type(events: List[Dict]) -> Dict:
    counter = {}

    for event in events:
        current_event_type = event["type"]
        if current_event_type in counter.keys():
            counter[current_event_type] += 1
        else:
            counter[current_event_type] = 1

    return counter


def convert_event_counter_to_descriptions(event_type_counter: Dict) -> List[str]:
    descriptions = []

    for event_type, count in event_type_counter.items():
        desc = EVENT_TYPE_ACTION_COUNT_CROSSWALK[event_type](count)
        descriptions.append(desc)

    return descriptions


def is_valid_event_type_to_review(event_type: str) -> bool:
    if event_type in EVENT_TYPES_TO_REVIEW:
        return True
    else:
        print("Entered invalid event type. See README for " "acceptable event types.")
        return False


def collect_events_based_on_event_type(event_data: list, event_type: str) -> list:
    events_to_review = []

    for event in event_data:
        if event["type"] == event_type:
            events_to_review.append(event)

    return events_to_review


def prepare_data_for_tabulate(data: List[Dict], event_type: str) -> List[List]:
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


def print_table(data: List[List], headers: List[str]) -> None:
    if len(data) == 0:
        raise ValueError("No data was provided to generate table.")
    
    if len(data[0]) != len(headers):
        raise ValueError(
            "Number of attributes does not equal the number of column headers."
            f"There are f{len(data[0])} attributes and f{len(headers)} column headers."
        )

    table = tabulate(data, headers=headers, tablefmt="pretty")
    print(table)
