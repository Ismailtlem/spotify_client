# spotify-client

[![PyPI](https://img.shields.io/pypi/v/spotify-client.svg)](https://pypi.org/project/spotify-client/)
[![Changelog](https://img.shields.io/github/v/release/Ismailtlem/spotify-client?include_prereleases&label=changelog)](https://github.com/Ismailtlem/spotify-client/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Ismailtlem/spotify-client/blob/main/LICENSE)

Python wrapper around spotify api. This is still an ongoing work

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd spotify-client
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install requirements/requirements.txt requirements-dev.txt
```

Create a new .env file following the structure of the file sample.env

```bash
cp sample.env .env
```

## Usage

Tha main class is `SpotifyClient` in `spotify_client/client`. Just import it and use it like in the following example

```python
from spotify_client.client import SpotifyClient
spotify_py_client = SpotifyClient(
    client_id="your-client-id",
    client_secret="your-client-secret",
)
## Get the album 4aawyAB9vmqN3uQ7FjRGTy
print(spotify_py_client.albums.get_by_id("4aawyAB9vmqN3uQ7FjRGTy"))
```

The available endpoints are in `spotify_client/endpoints`.

## Testing

To run the tests (No tests yet ...)

```bash
pytest
```
