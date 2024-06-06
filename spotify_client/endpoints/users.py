from typing import Any

from .generic_endpoint import GenericSpotifyEndpoint


class UsersEntity(GenericSpotifyEndpoint):
    """Actions for the Albums endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="users", **kwargs)

    def get_current_user_info(self) -> None:
        """Get all elements."""
        return self.client.get(
            "me",
            headers=self.client.connection.headers,
        )
