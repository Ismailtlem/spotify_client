class APIClientError(Exception):
    """General exception to denote that something went wrong when using the client.

    All other exceptions *must* inherit from this.
    """


class CustomError(APIClientError):
    """Some error happened while trying to connect to the API."""


class AuthenticationError(APIClientError):
    """Something went wrong when trying to auth to the API."""


class UserError(APIClientError):
    """Something went wrong when trying to auth to the API."""


class ResponseParseError(APIClientError):
    """Something went wrong when trying to parse the response."""
