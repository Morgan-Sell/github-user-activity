from abc import ABC, abstractmethod


class EventExtractionStrategy(ABC):
    """
    Abstract base class for extracting event details from event data.
    """

    def extract_event_id(self, event_data) -> str:
        """
        Extract the event ID from the event data.

        Args:
            event_data (dict): The event data containing event details.

        Returns:
            str: The event ID.
        """
        return event_data.get("id")

    def extract_repo_name(self, event_data) -> str:
        """
        Extract the repository name from the event data.

        Args:
            event_data (dict): The event data containing repository details.

        Returns:
            str: The repository name.
        """
        return event_data["repo"]["name"]

    @abstractmethod
    def extract_title(self, event_data) -> str:
        """
        Abstract method to extract the event title.

        Args:
            event_data (dict): The event data containing the event title.

        Returns:
            str: The event title.
        """
        pass

    def extract_action(self, event_data) -> str:
        """
        Abstract method to extract the event action.

        Args:
            event_data (dict): The event data containing the event action.

        Returns:
            str: The event action.
        """
        return event_data["payload"]["action"]

    @abstractmethod
    def extract_recipient(self, event_data) -> str:
        """
        Abstract method to extract the event recipient.

        Args:
            event_data (dict): The event data containing the recipient details.

        Returns:
            str: The recipient of the event.
        """
        pass

    def extract_created_date(self, event_data) -> str:
        """
        Extract the event creation date.

        Args:
            event_data (dict): The event data containing the creation date.

        Returns:
            str: The event creation date in ISO format.
        """
        return event_data.get("created_at")


class IssueCommentStrategy(EventExtractionStrategy):
    """
    Strategy for extracting details from IssueCommentEvent data.
    """

    def extract_title(self, event_data) -> str:
        return event_data["payload"]["issue"]["title"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["issue"]["user"]["login"]


class IssueStrategy(EventExtractionStrategy):
    """
    Strategy for extracting details from IssuesEvent data.
    """

    def extract_title(self, event_data) -> str:
        return event_data["payload"]["issue"]["title"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["issue"]["user"]["login"]


class PullRequestStrategy(EventExtractionStrategy):
    """
    Strategy for extracting details from PullRequestEvent data.
    """

    def extract_title(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["title"]

    def extract_recipient(self, event_data) -> str:
        try:
            return event_data["payload"]["pull_request"]["user"]["login"]
        except:
            return "n/a"


class PullRequestReviewStrategy(EventExtractionStrategy):
    """
    Strategy for extracting details from PullRequestReviewEvent data.
    """

    def extract_title(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["title"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["user"]["login"]


class PushStrategy(EventExtractionStrategy):
    """
    Strategy for extracting details from PushEvent data.
    """

    def extract_title(self, event_data) -> str:
        return event_data["payload"]["commits"][0]["message"]

    def extract_action(self, event_data) -> str:
        return "n/a"

    def extract_recipient(self, event_data) -> str:
        return "n/a"


# -- EventType Class - the "What" --
class EventType:
    def __init__(
        self,
        event_data: dict,
        extraction_strategy: EventExtractionStrategy,
    ):
        self.event_data = event_data
        self.extraction_strategy = extraction_strategy

    def get_event_id(self):
        return self.extraction_strategy.extract_event_id(self.event_data)

    def get_repo_name(self):
        return self.extraction_strategy.extract_repo_name(self.event_data)

    def get_title(self):
        return self.extraction_strategy.extract_title(self.event_data)

    def get_action(self):
        return self.extraction_strategy.extract_action(self.event_data)

    def get_recipient(self):
        return self.extraction_strategy.extract_recipient(self.event_data)

    def get_created_date(self):
        return self.extraction_strategy.extract_created_date(self.event_data)
