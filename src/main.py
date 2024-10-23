import json
import os
from pprint import pprint

from dotenv import load_dotenv

from src.api import get_user_events
from src.operations import (
    convert_event_counter_to_descriptions,
    count_events_by_type,
    is_valid_event_type_to_review,
)

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


def main():

    while True:
        github_user = input("Which GitHub user's activity would you like to see? ")

        # obtain and process data
        events = get_user_events(github_user, github_token)
        event_types_counter = count_events_by_type(events)
        descriptions = convert_event_counter_to_descriptions(event_types_counter)

        with open("events.json", "w") as json_file:
            json.dump(events, json_file, indent=4)

        # for desc in descriptions:
        #     print(desc)

        # ensure user submitted a valid event type
        valid_event_type = False
        while valid_event_type == False:
            user_event_type = input(
                f"\nWant to hear details of a specific event {github_user}'s"
            )

            valid_event_type = is_valid_event_type_to_review(user_event_type)

        # generate details of GitHub's user events for the selected event type


if __name__ == "__main__":
    main()
