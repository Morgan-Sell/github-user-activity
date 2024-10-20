class GitHubAPIError(Exception):
    """Base class for GitHub API errors."""

    pass


class UnauthorizedError(GitHubAPIError):
    """Exception raised for 401 unauthorized errors."""

    pass


class UsernameNotFoundError(GitHubAPIError):
    """Exception raised when a GitHub username does not exist, a 404 error."""

    pass


class OtherHTTPError(GitHubAPIError):
    """Exception raised for HTTP errors other than 401 or 404."""

    pass


class APIConnectionError(GitHubAPIError):
    """
    Exception raised for network or connection-related errors when
    communicating with the GitHub API.
    """

    pass


class JSONParseError(GitHubAPIError):
    """
    Exception raised for errors in parsing JSON responses
    from the GitHub API.
    """

    pass


class UnhandledError(GitHubAPIError):
    """
    Generic exception raised for any other errors not covered by
    specific GitHub API exceptions.
    """

    pass
