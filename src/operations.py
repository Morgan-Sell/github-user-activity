from typing import Dict, List

from src.config import (
    EVENT_TYPE_ACTION_COUNT_CROSSWALK,
    EVENT_TYPES,
    EVENT_TYPES_TO_REVIEW,
)


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
