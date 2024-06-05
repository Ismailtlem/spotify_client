from typing import Any

# from shows.base_client import BaseClient
# from spotify_client.client import SpotifyClient
# clfrom spotify_client.helpers import build_path
from .generic_endpoint import GenericSpotifyEndpoint


class ShowsEntity(GenericSpotifyEndpoint):
    """Actions for the Albums endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="shows", **kwargs)
