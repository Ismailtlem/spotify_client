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
from spotify_client.helpers import RetryAdapter, build_path

from .base_client import BaseClient

# from requests import codes as http_status
from .endpoints import (
    AlbumsEntity,
    ArtistsEntity,
    AudioBooksEntity,
    CategoriesEntity,
    ChaptersEntity,
    EpisodesEntity,
    GenresEntity,
    MarketsEntity,
    PlaylistsEntity,
    ShowsEntity,
    TracksEntity,
    UsersEntity,
)
from .exceptions import AuthenticationError, ResponseParseError


config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}


class SpotifyClient(BaseClient):
    """Basic api class."""

    BASE_URL = config.get("spotify_base_api_url", "")
    TOKEN_URL = config.get("spotify_token_url", "https://accounts.spotify.com/api/token")
    DEFAULT_SCOPE = "user-library-read"

    def __init__(
        self,
        scope: str = "",
        client_id: str = "",
        client_secret: str = "",
        redirect_uri: str = "",
    ) -> None:
        super().__init__(base_url=self.BASE_URL)  # Call the BaseClient's __init__ method
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = ""
        self.access_code = ""
        self.scope = scope
        self.redirect_uri = redirect_uri
        print(self.is_calling_user_data)
        if not (self.scope and self.redirect_uri):
            spotify_auth = SpotifyAuth(
                self.connection,
                self.client_id,
                self.client_secret,
            )
            self._access_token = spotify_auth.request_general_token()
        else:
            print("insiiiiide user data")
            spotify_auth = SpotifyAuth(
                self.connection, self.scope, self.client_id, self.client_secret, self.redirect_uri
            )
            self.access_code = spotify_auth.get_auth_code()
            self._access_token = spotify_auth.request_user_access_token(self.access_code)
        self.connection.headers.update({"Authorization": f"Bearer {self._access_token}"})

        self.albums = AlbumsEntity(client=self)
        self.artists = ArtistsEntity(client=self)
        self.audiobooks = AudioBooksEntity(client=self)
        self.categories = CategoriesEntity(client=self)
        self.chapters = ChaptersEntity(client=self)
        self.episodes = EpisodesEntity(client=self)
        self.genres = GenresEntity(client=self)
        self.markets = MarketsEntity(client=self)
        self.playlists = PlaylistsEntity(client=self)
        self.shows = ShowsEntity(client=self)
        self.tracks = TracksEntity(client=self)
        self.users = UsersEntity(client=self)

    @property
    def is_calling_user_data(self) -> bool:
        """Return true if the user data should be called."""
        # if self.scope or self.redirect_uri:
        #     return False
        # if self.scope and self.redirect_uri:
        #     return True
        return True if self.redirect_uri and self.scope else False

    #     # TODO handle rate limiting gracefully
    # if scope==True or redirect uri==True
    # returns false
