from typing import Any

from spotify_client.generic_endpoint import GenericEndpoint


class AlbumsEntity(GenericEndpoint):
    """
    Actions for the Albums endpoint.
    """

    def __init__(self, client, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(client)
        self.client = client
        self.endpoint = "shows"
        # self.workflow_id = None

    def get_by_id(self, entity_id: str) -> None:
        """Get a playlist"""

        return self.client.get(self.build_path(entity_id))

    def get_by_ids(self, entity_ids: str) -> None:
        """Get many shows"""

        return self.client.get_by_ids(self.build_path(self.endpoint), entity_ids)

    def get_entity_object(self, entity_id: str, entity_object: str) -> None:
        """Get a show entity"""

        print(self.build_path(entity_id, entity_object))
        return self.client.get(self.build_path(entity_id, entity_object))
