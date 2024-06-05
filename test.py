from typing import Any

from spotify_client.client import SpotifyClient
from spotify_client.endpoints import AlbumsEntity, MarketsEntity, UsersEntity


# from spotify_client.endpoints.artists import ArtistsEntity


class SpotifyTestClient(SpotifyClient):
    """Main class to communicate with the Spotify API."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the class with your api_key and user_id and attach all of
        the endpoints
        """

        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    spotify_py_client = SpotifyTestClient(
        scope="user-library-read",
        client_id="60a09940b21c4eb680eb27104c98abb7",
        client_secret="72756de6e43f48109d98f0fd648c561f",
        redirect_uri="https://localhost:3000/callback",
    )
    print(spotify_py_client.artists.get_entity_feature("2aZPgvcYQD2z4NIoO8x8Gi", "related-artists"))
