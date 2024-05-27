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
        super().__init__(client, *args, **kwargs)
        self.client = client
        self.endpoint = "albums"
        # self.workflow_id = None

    def get_by_id(self, entity_id: str) -> None:
        """Get an album"""

        return self.client.get(self.build_path(entity_id))

    def get_by_ids(self, entity_ids: str) -> None:
        """Get many albums"""

        return self.client.get_by_ids(self.build_path(self.endpoint), entity_ids)

    def get_entity_object(self, entity_id: str, entity_object: str) -> None:
        """Get an album object"""

        # print(self.build_path(entity_id, entity_object))
        return self.client.get(self.build_path(entity_id, entity_object))

    def get_user_saved_albums(self) -> None:
        """Get an album object"""

        return self.client.get("me/" + self.endpoint)

    def save_albums_for_current_user(self, album_ids: list[str]) -> None:

        albums = {"ids": album_ids}
        return self.client.put("me/" + self.endpoint, albums)

    def delete_user_saved_albums(self, album_ids: list[str]) -> None:

        albums = {"ids": album_ids}
        return self.client.delete("me/" + self.endpoint, albums)
