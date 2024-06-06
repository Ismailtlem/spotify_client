from typing import Any

from .generic_endpoint import GenericSpotifyEndpoint


class CategoriesEntity(GenericSpotifyEndpoint):
    """Actions for the Categories endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="browse/categories", **kwargs)
