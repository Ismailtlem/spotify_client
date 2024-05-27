"""
Main Spotify API Client
"""

import base64
from typing import Any
from urllib import parse as urlparse

# from dotenv import load_dotenv
from dotenv import dotenv_values
from requests import Request, Session, codes, exceptions, utils

from spotify_client.auth import SpotifyAuth

# logger = logging.getLogger("example.exampleClient")
from spotify_client.helpers import RetryAdapter

# from requests import codes as http_status
# from .endpoints.albums import AlbumsEntity
from .exceptions import AuthenticationError, ResponseParseError

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


class SpotifyClient(object):
    """
    Basic api class
    """

    default_headers = {
        "User-Agent": utils.default_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
    }

    BASE_URL = config.get("spotify_base_api_url")
    TOKEN_URL = config.get("spotify_token_url", "https://accounts.spotify.com/api/token")
    DEFAULT_SCOPE = "user-library-read"

    def __init__(
        self, client_id: str, client_secret: str, redirect_uri: str = "", scope: str = ""
    ) -> None:
        self.base_url = self.BASE_URL
        self.client_id = client_id
        self.client_secret = client_secret
        self.connection = Session()
        self.connection.mount("https", RetryAdapter())
        self.connection.headers = self.default_headers
        self._access_token = ""
        self.access_code = ""
        if self._call_user_data(redirect_uri, scope):
            self.redirect_uri = redirect_uri
            self.scope = scope
            spotify_auth = SpotifyAuth(
                self.connection, self.client_id, self.client_secret, self.redirect_uri, self.scope
            )
            self.access_code = spotify_auth.get_auth_code()
            self._access_token = spotify_auth.request_access_token(self.access_code)
            self.connection.headers.update({"Authorization": f"Bearer {self._access_token}"})
        else:
            spotify_auth = SpotifyAuth(
                self.connection,
                self.client_id,
                self.client_secret,
            )
            spotify_auth.request_access_token()
        parsed_url = urlparse.urlparse(self.base_url)
        if parsed_url.scheme not in ["http", "https"]:
            raise ValueError("Spotify API URL is incorrect")

    def _make_request(self, endpoint: Any, method: str, query_params: Any, body: Any) -> None:
        """Handles all requests to the endpoint"""

        url = self.base_url + endpoint
        print("urllllllllll", url)
        print("meeeethod", method)
        print("boooody", body)
        req = Request(method, url, params=query_params, json=body)
        prepped = self.connection.prepare_request(req)

        # Log request prior to sending
        # Actually make request to endpoint
        res = self.connection.send(prepped)

        #     # Log response immediately upon return

        #     # Handle all response codes as elegantly as needed in a single spot
        if res.status_code == codes.ok:
            print("requuuest successful")
            if method == "GET":
                try:
                    resp_json = res.json()
                    print("Response: {}".format(resp_json))
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

    def _call_user_data(self, redirect_uri: str, scope: str) -> bool:
        """Returns true if the user data should be called"""

        return True if redirect_uri and scope else False

    #     # TODO handle rate limiting gracefully

    #     # Raises HTTP error if status_code is 4XX or 5XX
    #     elif r.status_code >= 400:
    #         logger.error("Received a " + str(r.status_code) + " error!")
    #         try:
    #             logger.debug("Details: " + str(r.json()))
    #         except ValueError:
    #             pass

    def make_request(
        self, endpoint: str, method: str, query_params: Any = None, body: Any = None
    ) -> None:
        """Make a request"""

        return self._make_request(
            endpoint=endpoint, method=method, query_params=query_params, body=body
        )

    def get(self, endpoint: str) -> None:
        """
        Get an endpoint
        """
        return self.make_request(endpoint=endpoint, method="GET")

    def get_by_ids(self, endpoint: str, entity_ids: str):
        """
        Get an endpoint relative to the specified entity_ids
        """

        return self.make_request(endpoint, "GET", {"ids": entity_ids})

    def put(self, endpoint: str, body: Any) -> None:
        """
        Make a put request an endpoint
        """
        print("booody", body)
        return self.make_request(endpoint=endpoint, method="PUT", body=body)

    def delete(self, endpoint: str, body: Any) -> None:
        """
        Get an endpoint
        """
        print("booody", body)
        return self.make_request(endpoint=endpoint, method="DELETE", body=body)
