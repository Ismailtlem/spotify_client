from typing import Any

from .generic_endpoint import GenericSpotifyEndpoint


class GenresEntity(GenericSpotifyEndpoint):
    """Actions for the Genres endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(
            client=self.client, endpoint="recommendations/available-genre-seeds", **kwargs
        )
