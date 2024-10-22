from abc import ABC, abstractmethod


class EventExtractionStrategy(ABC):
    def extract_event_id(self, event_data):
        return event_data.get("id")

    def extract_repo_name(self, event_data):
        return event_data["repo"]["name"]

    @abstractmethod
    def extract_title(self, event_data):
        pass

    @abstractmethod
    def extract_action(self, event_data):
        pass

    @abstractmethod
    def extract_recipient(self, event_data):
        pass

    def extract_created_date(self, event_data):
        return event_data.get("created_at")


class IssueCommentStrategy(EventExtractionStrategy):
    def extract_title(self, event_data):
        return event_data["payload"]["issue"]["title"]

    def extract_action(self, event_data):
        return event_data["payload"]["action"]

    def extract_recipient(self, event_data):
        return event_data["payload"]["issue"]["user"]["login"]


class IssueStrategy(EventExtractionStrategy):
    def extract_title(self, event_data) -> str:
        return event_data["payload"]["issue"]["title"]

    def extract_action(self, event_data) -> str:
        return event_data["payload"]["action"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["issue"]["user"]["login"]


class PullRequestStrategy(EventExtractionStrategy):
    def extract_title(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["title"]

    def extract_action(self, event_data) -> str:
        return event_data["payload"]["action"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["user"]["login"]


class PullRequestReviewStrategy(EventExtractionStrategy):
    def extract_title(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["title"]

    def extract_action(self, event_data) -> str:
        return event_data["payload"]["action"]

    def extract_recipient(self, event_data) -> str:
        return event_data["payload"]["pull_request"]["user"]["login"]


class PushStrategy(EventExtractionStrategy):
    def extract_title(self, event_data) -> str:
        return event_data["payload"]["commits"][0]["message"]

    def extract_action(self, event_data) -> str:
        return "--"

    def extract_recipient(self, event_data) -> str:
        return "--"


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
        return self.extraction_strategy.extract_title(self.event_data)

    def get_recipient(self):
        return self.extraction_strategy.extract_recipient(self.event_data)

    def get_recipient(self):
        return self.extraction_strategy.extract_created_date(self.event_data)
