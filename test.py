from typing import Any

from spotify_client.client import SpotifyClient
from spotify_client.endpoints import AlbumsEntity, MarketsEntity, UsersEntity

# from spotify_client.endpoints.artists import ArtistsEntity


class SpotifyPyClient(SpotifyClient):
    """
    Main class to communicate with the Spotify API
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the class with your api_key and user_id and attach all of
        the endpoints
        """

        super().__init__(*args, **kwargs)

        self.albums = AlbumsEntity(self)

        self.markets = MarketsEntity(self)
        self.users = UsersEntity(self)


if __name__ == "__main__":
    spotify_py_client = SpotifyPyClient(
        client_id="60a09940b21c4eb680eb27104c98abb7",
        client_secret="72756de6e43f48109d98f0fd648c561f",
        redirect_uri="https://localhost:3000/callback",
        scope="user-library-modify",
    )
    print(spotify_py_client.albums.save_albums_for_current_user(["1aGapZGHBovnmhwqVNI6JZ"]))
