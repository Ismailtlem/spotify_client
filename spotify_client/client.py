"""Main Spotify API Client."""

import logging

# from dotenv import load_dotenv
from dotenv import dotenv_values

from spotify_client.auth import SpotifyAuth

from .base_client import BaseClient
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


# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

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
        super().__init__(base_url=self.BASE_URL)
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = ""
        self.access_code = ""
        self.scope = scope
        self.redirect_uri = redirect_uri
        if not (self.scope and self.redirect_uri):
            spotify_auth = SpotifyAuth(
                self.connection,
                self.client_id,
                self.client_secret,
            )
            self._access_token = spotify_auth.request_general_token()
        else:
            spotify_auth = SpotifyAuth(
                self.connection, self.scope, self.client_id, self.client_secret, self.redirect_uri
            )
            self.access_code = spotify_auth.auth_code
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
        return True if self.redirect_uri and self.scope else False

