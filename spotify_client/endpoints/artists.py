from typing import Any

from spotify_client.generic_endpoint import GenericEndpoint


class ArtistsEntity(GenericEndpoint):
    """
    Actions for the Artists endpoint.
    """

    def __init__(self, client, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(client)
        self.client = client
        self.endpoint = "artists"
        # self.workflow_id = None

    def get_by_id(self, entity_id: str) -> None:
        """Get an artist"""

        print(self.endpoint)
        print(entity_id)
        print(self.build_path(entity_id))
        return self.client.get(self.build_path(entity_id))

    def get_by_ids(self, entity_ids: str) -> None:
        """Get many artists"""

        print(self.build_path(self.endpoint))
        return self.client.get_by_ids(self.build_path(), entity_ids)

    def get_entity_objects(self, entity_id: str, entity_object: str) -> None:
        """Get an artist entity objects"""

        print(self.build_path(entity_id, entity_object))
        return self.client.get(self.build_path(entity_id, entity_object))
