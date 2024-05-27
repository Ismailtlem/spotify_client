from typing import Any

from spotify_client.generic_endpoint import GenericEndpoint


class PlaylistsEntity(GenericEndpoint):
    """
    Actions for the Playlists endpoint.
    """

    def __init__(self, client, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(client)
        self.client = client
        self.endpoint = "playlists"
        # self.workflow_id = None

    def get_by_id(self, entity_id: str) -> None:
        """Get a playlist"""

        return self.client.get(self.build_path(entity_id))

    def get_by_ids(self, entity_ids: str) -> None:
        """Get many playlists"""

        return self.client.get_by_ids(self.build_path(self.endpoint), entity_ids)
