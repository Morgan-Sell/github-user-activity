import os
from pprint import pprint
import json

from dotenv import load_dotenv

from src.api import get_user_events

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


def main():
    events = get_user_events("arjancodes", github_token)

    with open("events.json", "w") as json_file:
        json.dump(events, json_file, indent=4)


if __name__ == "__main__":
    main()
