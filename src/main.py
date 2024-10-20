import os
from pprint import pprint
import json

from dotenv import load_dotenv

from src.api import get_user_events
from src.operations import convert_event_counter_to_descriptions, count_events_by_type

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


def main():
    
    while True:
        github_user = input(
            "Which GitHub user's activity would you like to see? "
        )
        
        # obtain and process data
        events = get_user_events(github_user, github_token)
        event_types_counter = count_events_by_type(events)
        descriptions = convert_event_counter_to_descriptions(
            event_types_counter
        )

        for desc in descriptions:
            print(desc)
    
    # payload_events = {}

    # for event in data:
    #     payload_events[event["type"]] = list(event["payload"].keys())

    # with open("payload_events.json", "w") as json_file:
    #     json.dump(payload_events, json_file, indent=4)


if __name__ == "__main__":
    main()
