from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RETRY_COUNT = 5


class RetryAdapter(HTTPAdapter):
    """Retry adapter"""

    def __init__(self, *args, **kwargs) -> None:
        super(RetryAdapter, self).__init__(*args, **kwargs)
        self.max_retries = Retry(total=RETRY_COUNT)
