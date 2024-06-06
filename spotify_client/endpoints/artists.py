from typing import Any

from .generic_endpoint import GenericSpotifyEndpoint


class ArtistsEntity(GenericSpotifyEndpoint):
    """Actions for the Artists endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="artists", **kwargs)
