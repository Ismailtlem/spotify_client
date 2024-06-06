from typing import Any

from .generic_endpoint import GenericSpotifyEndpoint


class PlaylistsEntity(GenericSpotifyEndpoint):
    """Actions for the Albums endpoint."""

    def __init__(self, client: Any, **kwargs: Any) -> None:
        """Initialize the endpoint."""
        self.client = client
        super().__init__(client=self.client, endpoint="playlists", **kwargs)

    def add_items(
        self,
        playlist_id: str,
        playlist_item: str,
        items_ids: str,
        query_params: Any = None,
        **kwargs: Any,
    ):
        """Add items to a playlist."""
        body = {"uris": items_ids.split(",")}
        if kwargs:
            body.update(kwargs)
        return self.client.post(
            self.build_path(playlist_id, playlist_item),
            headers=self.client.connection.headers,
            query_params=query_params,
            body=body,
        )

    def remove_items(
        self,
        playlist_id: str,
        playlist_item: str,
        items_ids: str,
        query_params: Any = None,
        **kwargs: Any,
    ):
        """Remove items from a playlist."""
        body = {"tracks": [{"uri": item_id} for item_id in items_ids.split(",")]}
        if kwargs:
            body.update(kwargs)
        return self.client.delete(
            self.build_path(playlist_id, playlist_item),
            headers=self.client.connection.headers,
            query_params=query_params,
            body=body,
        )

    def get_user_playlists(self, user_id: str, query_params: Any = None) -> None:
        """Get the playlists of the user_id."""
        return self.client.get(
            self.build_path(user_id, self.endpoint),
            headers=self.client.connection.headers,
            query_params=query_params,
        )

    def create(self, user_id: str, name: str, query_params: Any = None, **kwargs: Any) -> None:
        """Get the playlists of the user_id."""
        body = {"name": name}
        if kwargs:
            body.update(kwargs)
        return self.client.post(
            f"users/{user_id}/" + self.endpoint,
            headers=self.client.connection.headers,
            query_params=query_params,
            body=body,
        )
