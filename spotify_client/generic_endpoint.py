from itertools import chain
from typing import Any

# from requests import Request, Session


class GenericEndpoint(object):
    """
    Simple class to buid path for entities
    """

    def __init__(self, client: Any):
        """
        Initialize the class with the client_id client_secret

        :param mc_client: The spotify client connection
        :param endpoint: The entity endpoint
        """

        # self.session = Session()
        self.client = client
        # self.base_url = base_url
        self.endpoint = ""

    def build_path(self, *args: Any):
        """
        Build path with endpoint and args

        :param args: Tokens in the endpoint URL
        :type args: :py:class:`unicode`
        """
        return "/".join(chain((self.endpoint,), map(str, args)))
