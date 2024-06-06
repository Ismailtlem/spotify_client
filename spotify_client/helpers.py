from itertools import chain
from typing import Any
from urllib.parse import parse_qsl, urlparse

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import AuthenticationError


RETRY_COUNT = 5


class RetryAdapter(HTTPAdapter):
    """Retry adapter."""

    def __init__(self, *args, **kwargs) -> None:
        super(RetryAdapter, self).__init__(*args, **kwargs)
        self.max_retries = Retry(total=RETRY_COUNT)


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
