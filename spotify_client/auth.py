import base64
import urllib.parse as urllibparse
import webbrowser

from dotenv import dotenv_values
from requests import Session, exceptions

from spotify_client.helpers import parse_auth_response_url

from .exceptions import AuthenticationError


config = dotenv_values(".env")


class SpotifyAuth:
    """Spotify Base object for authentication."""

    OAUTH_AUTHORIZE_URL = config.get("spotify_auth_url", "https://accounts.spotify.com/authorize")
    TOKEN_URL = config.get("spotify_token_url", "https://accounts.spotify.com/api/token")

    def __init__(
        self,
        session: Session,
        scope: str,
        client_id: str = "",
        client_secret: str = "",
        redirect_uri: str = "",
        show_dialog: bool = False,
    ) -> None:
        self.session = session
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.show_dialog = show_dialog

        self._access_token = ""  #

    def request_general_token(self) -> str:
        """Request a general token for general data."""
        auth_string = f"{config.get('client_id', '')}:{config.get('client_secret', '')}"
        base64_auth_string = base64.b64encode(auth_string.encode()).decode()
        self.session.headers.update({"Authorization": f"Basic {base64_auth_string}"})
        payload = {"grant_type": "client_credentials"}
        try:
            response = self.session.post(self.TOKEN_URL, data=payload, headers=self.session.headers)  # type: ignore
            response.raise_for_status()

            return response.json().get("access_token")
        except exceptions.RequestException as e:
            raise AuthenticationError(f"Could not get the token {e}")

    def request_user_access_token(self, access_code: str) -> str:
        """Get client credentials access token."""
        auth_string = f"{config.get('client_id', '')}:{config.get('client_secret', '')}"
        base64_auth_string = base64.b64encode(auth_string.encode()).decode()
        self.session.headers.update({"Authorization": f"Basic {base64_auth_string}"})

        payload = {
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
        }
        if access_code:
            payload["code"] = access_code
        try:
            response = self.session.post(self.TOKEN_URL, data=payload, headers=self.session.headers)  # type: ignore
            response.raise_for_status()
            print("eeeend access token 1", response.json().get("access_token"))
            return response.json().get("access_token")

            # return response.json()
        except exceptions.RequestException as e:
            raise AuthenticationError(f"Could not get the token {e}")

    def _build_authorize_url(self) -> str:
        """Get the URL to use to authorize this app."""
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

    @property
    def auth_code(self) -> None | str:
        """Get the authorization code to access user data."""
        auth_url = self._build_authorize_url()
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser", auth_url)
            redirect_url = input("Enter the url you have been redirected to : ")
            return parse_auth_response_url(redirect_url)
        except webbrowser.Error:
            print("Please navigate here: %s", auth_url)
