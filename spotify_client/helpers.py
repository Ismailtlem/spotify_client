from itertools import chain
from typing import Any
from urllib.parse import parse_qsl, urlparse

from requests.adapters import HTTPAdapter
from urllib3 import Retry

from .exceptions import AuthenticationError


MAX_RETRIES = 5


class RetryAdapter(HTTPAdapter):
    """Retry adapter."""

    def __init__(
        self, max_retries: int = MAX_RETRIES, backoff_factor: float = 0.1, **kwargs: Any
    ) -> None:
        """Retry adapter constructor method."""
        retry_adapter = Retry(
            total=max_retries,
            allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE"]),
            backoff_factor=backoff_factor,
            status_forcelist=[400, 429, 500, 502, 503, 504],
        )
        super().__init__(max_retries=retry_adapter, **kwargs)


def build_path(base_url: str, endpoint: str, *args: Any) -> str:
    """Build path with endpoint and args."""
    return "/".join(chain((base_url + endpoint,), map(str, args)))


def parse_auth_response_url(url: str) -> str:
    """Parse the auth url to extract the code."""
    query_s = urlparse(url).query
    form = dict(parse_qsl(query_s))

    if "error" in form:
        raise AuthenticationError(
            "Received error from auth server: " "{}".format(form["error"]), error=form["error"]
        )
    return form.get("code", "")
