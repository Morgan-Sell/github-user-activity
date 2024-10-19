import os
from pprint import pprint

from dotenv import load_dotenv

from src.api import get_user_events

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


def main():
    events = get_user_events("angelabauer", github_token)

    pprint(events[:2])


if __name__ == "__main__":
    main()
