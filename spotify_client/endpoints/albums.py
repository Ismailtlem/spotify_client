from typing import Any

# from spotify_client.base_client import BaseClient
# from spotify_client.client import SpotifyClient
# clfrom spotify_client.helpers import build_path
from .generic_endpoint import GenericSpotifyEndpoint


class AlbumsEntity(GenericSpotifyEndpoint):
    """Actions for the Albums endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="albums", **kwargs)

    def get_new_releases(self, query_params: Any = None):
        """Get a list of new album releases featured in Spotify."""
        return self.client.get(
            "browse/new-releases",
            headers=self.client.connection.headers,
            query_params=query_params,
        )
