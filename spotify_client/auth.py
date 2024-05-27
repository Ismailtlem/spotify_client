import base64
import webbrowser
from urllib.parse import parse_qsl, urlparse

import requests
import six.moves.urllib.parse as urllibparse
from dotenv import dotenv_values
from requests import Session, exceptions
from requests.auth import AuthBase

from .exceptions import AuthenticationError, ResponseParseError

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


class SpotifyAuth:
    """Spotify Base object for authentication"""

    OAUTH_AUTHORIZE_URL = config.get("spotify_auth_url", "")
    TOKEN_URL = config.get("spotify_token_url", "https://accounts.spotify.com/api/token")

    def __init__(
        self,
        session: Session,
        client_id: str = "",
        client_secret: str = "",
        redirect_uri: str = "",
        scope: str = "",
        show_dialog: bool = False,
    ) -> None:
        """
        Initialize the OAuth and save the access token

        """
        self.session = session
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.show_dialog = show_dialog

        self._access_token = ""

    def request_access_token(self, access_code: str = "") -> str:
        """Get client credentials access token"""

        auth_string = f"{config.get('client_id', '')}:{config.get('client_secret', '')}"
        base64_auth_string = base64.b64encode(auth_string.encode()).decode()
        self.session.headers.update({"Authorization": f"Basic {base64_auth_string}"})
        print("payyyloaaad", self.redirect_uri)
        print("scooope", self.scope)
        if self.redirect_uri and self.scope:
            payload = {
                "grant_type": "authorization_code",
                "redirect_uri": self.redirect_uri,
            }
            if access_code:
                payload["code"] = access_code
            try:
                response = self.session.post(self.TOKEN_URL, data=payload, headers=self.session.headers)  # type: ignore
                response.raise_for_status()
                return response.json().get("access_token")

                # return response.json()
            except exceptions.RequestException as e:
                raise AuthenticationError(f"Could not get the token {e}")

        else:
            payload = {"grant_type": "client_credentials"}
            # payload.update({"client_id": self.client_id, "client_secret": self.client_secret})
            try:
                response = self.session.post(self.TOKEN_URL, data=payload, headers=self.session.headers)  # type: ignore
                response.raise_for_status()
                self._access_token = response.json().get("access_token")
                self.session.headers.update({"Authorization": f"Bearer {self._access_token}"})

                return response.json()
            except exceptions.RequestException as e:
                raise AuthenticationError(f"Could not get the token {e}")

    def build_authorize_url(self) -> str:
        """Gets the URL to use to authorize this app"""

        payload = {
            "response_type": "code",
            "client_id": self.client_id,
            "scope": self.scope,
            "redirect_uri": self.redirect_uri,
        }

        if self.show_dialog:
            payload["show_dialog"] = True

        urlparams = urllibparse.urlencode(payload)

        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, urlparams)

    @staticmethod
    def parse_auth_response_url(url: str) -> str:
        """Parse the auth url to extract the code"""

        query_s = urlparse(url).query
        form = dict(parse_qsl(query_s))

        if "error" in form:
            raise AuthenticationError(
                "Received error from auth server: " "{}".format(form["error"]), error=form["error"]
            )
        return form.get("code", "")

    def get_auth_code(self) -> None | str:
        """Open auth url to auth the current user"""

        auth_url = self.build_authorize_url()
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser", auth_url)
            redirect_url = input("Enter the url you have been redirected to :")
            return self.parse_auth_response_url(redirect_url)
        except webbrowser.Error:
            print("Please navigate here: %s", auth_url)

    # the url is https://accounts.spotify.com/authorize?client_id=60a09940b21c4eb680eb27104c98abb7&response_type=code&redirect_uri=https://localhost:3000/redirect_uri&scope=user-read-private user-read-email
