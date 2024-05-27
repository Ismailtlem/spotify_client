from typing import Any

from spotify_client.generic_endpoint import GenericEndpoint


class UsersEntity(GenericEndpoint):
    """
    Actions for the Tracks endpoint.
    """

    def __init__(self, client: Any, *args: Any, **kwargs: Any) -> Any:
        """
        Initialize the endpoint
        """
        super().__init__(client, *args, **kwargs)
        self.client = client
        self.endpoint = "me"
        # self.workflow_id = None

    def get_current_user(self) -> None:
        """Get info of the current user"""

        return self.client.get(self.build_path())

    def get_user_top_items(self, entity_type: str) -> None:
        """Get user top items"""

        return self.client.get(self.build_path("top", entity_type))
