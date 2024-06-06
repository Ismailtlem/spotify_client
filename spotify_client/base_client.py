from typing import Any, ClassVar
from urllib import parse as urlparse

from requests import Request, Session, codes, exceptions, utils

from spotify_client.helpers import RetryAdapter

from .exceptions import AuthenticationError, ResponseParseError


class BaseClient(object):
    """Simple class to buid path for entities."""

    default_headers: ClassVar[dict[str, str | bytes]] = {
        "User-Agent": utils.default_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    def __init__(self, base_url: str) -> None:
        """Init the class."""
        self.base_url = base_url
        self.connection = Session()
        self.connection.mount("https", RetryAdapter())
        self.connection.headers = self.default_headers
        parsed_url = urlparse.urlparse(self.base_url)
        if parsed_url.scheme not in ["http", "https"]:
            raise ValueError("API URL is incorrect")

    def _make_request(
        self, endpoint: str, method: str, headers: Any, query_params: Any, body: Any
    ) -> None:
        """Make a request to the endpoint."""
        print(
            "enddpoint",
            self.base_url + endpoint,
        )
        print("queeery paaraaams", query_params)
        print("booody", body)
        req = Request(
            method=method,
            url=self.base_url + endpoint,
            headers=headers,
            params=query_params,
            json=body,
        )
        prepped = self.connection.prepare_request(req)
        res = self.connection.send(prepped)
        #     # Log response immediately upon return

        #     # Handle all response codes as elegantly as needed in a single spot
        if res.status_code == codes.ok:
            print("requuuest successful")
            if method == "GET":
                try:
                    resp_json = res.json()
                    return resp_json
                except exceptions.JSONDecodeError as e:
                    raise ResponseParseError(f"Error raised by the API: {e}.\nResponse: {res.text}")

        elif res.status_code == codes.bad_request or codes.unauthorized:
            try:
                resp_json = res.json()
                print("Details: " + str(resp_json))
                raise AuthenticationError(resp_json)

            except exceptions.JSONDecodeError as e:
                raise ResponseParseError(f"Error raised by the API: {e}.\nResponse: {res.text}")

    def make_request(
        self,
        endpoint: str,
        method: str,
        headers: Any = None,
        query_params: Any = None,
        body: Any = None,
    ) -> None:
        """Make a request."""
        return self._make_request(
            endpoint=endpoint, method=method, headers=headers, query_params=query_params, body=body
        )

    def get(self, endpoint: str, headers: Any, query_params: Any = None, body: Any = None) -> None:
        """Get an url."""
        return self.make_request(
            endpoint=endpoint, method="GET", headers=headers, query_params=query_params, body=body
        )

    def post(self, endpoint: str, headers: Any, query_params: Any = None, body: Any = None) -> None:
        """Make a Post request."""
        return self.make_request(
            endpoint=endpoint, method="POST", headers=headers, query_params=query_params, body=body
        )

    def put(self, endpoint: str, headers: Any, query_params: Any = None, body: Any = None) -> None:
        """Make a put request an url."""
        return self.make_request(
            endpoint=endpoint, method="PUT", headers=headers, query_params=query_params, body=body
        )

    def delete(
        self, endpoint: str, headers: Any, query_params: Any = None, body: Any = None
    ) -> None:
        """Make a delete request to the url."""
        return self.make_request(
            endpoint=endpoint,
            method="DELETE",
            headers=headers,
            query_params=query_params,
            body=body,
        )
