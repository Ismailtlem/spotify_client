from itertools import chain
from typing import Any


class GenericSpotifyEndpoint:
    """Generic class to spotify endpoints."""

    def __init__(self, client: Any, endpoint: str) -> None:
        """Initialize Generic Spotify Endpoint."""
        self.endpoint = endpoint
        self.client = client
        self.current_user_endpoint = "me/" + self.endpoint

    def build_path(self, *args: Any) -> str:
        """Build path with endpoint and args."""
        return "/".join(chain((self.endpoint,), map(str, args)))

    def get_all(self, query_params: Any = None) -> None:
        """Get all elements."""
        return self.client.get(
            self.build_path(),
            headers=self.client.connection.headers,
            query_params=query_params,
        )

    def get_by_id(self, entity_id: str, query_params: Any = None) -> None:
        """Get an entity by id."""
        return self.client.get(
            self.build_path(entity_id),
            headers=self.client.connection.headers,
            query_params=query_params,
        )

    def get_by_ids(self, entity_ids: str, query_params: Any = None) -> None:
        """Get an endpoint relative to the specified entity_ids."""
        params = query_params
        params["ids"] = entity_ids
        return self.client.get(
            self.build_path(),
            headers=self.client.connection.headers,
            query_params=params,
        )

    def get_entity_item(self, entity_id: str, entity_item: str, query_params: Any = None) -> None:
        """Get a specific feature of the specified entity."""
        return self.client.get(
            self.build_path(entity_id, entity_item),
            headers=self.client.connection.headers,
            query_params=query_params,
        )

    def get_user_saved_objects(self, query_params: Any = None) -> None:
        """Get an album object."""
        return self.client.get(
            self.current_user_endpoint,
            headers=self.client.connection.headers,
            query_params=query_params,
        )

    def save_entities_for_current_user(self, entity_ids: str) -> None:
        """Save the specified entities for the current user."""
        return self.client.put(
            self.current_user_endpoint,
            headers=self.client.connection.headers,
            body={"ids": entity_ids.split(",")},
        )

    def remove_entities_from_current_user(self, entity_ids: str) -> None:
        """Remove entities from the current user."""
        return self.client.delete(
            self.current_user_endpoint,
            headers=self.client.connection.headers,
            query_params={"ids": entity_ids.split(",")},
        )

    def check_saved_entities(self, entity_ids: str) -> None:
        """Remove saved entities from the current user."""
        return self.client.get(
            self.current_user_endpoint + "/contains",
            headers=self.client.connection.headers,
            query_params={"ids": entity_ids},
        )
