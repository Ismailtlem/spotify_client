from typing import Any

from spotify_client.generic_endpoint import GenericEndpoint


class GenresEntity(GenericEndpoint):
    """
    Actions for the Genres endpoint.
    """

    def __init__(self, client, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super().__init__(client)
        self.client = client
        self.endpoint = "recommendations/available-genre-seeds"
        # self.workflow_id = None

    def all(self) -> None:
        """Get all elements"""

        return self.client.get(self.build_path())
