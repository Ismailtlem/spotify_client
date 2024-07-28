# spotify-client

[![PyPI](https://img.shields.io/pypi/v/spotify-client.svg)](https://pypi.org/project/spotify-client/)
[![Changelog](https://img.shields.io/github/v/release/Ismailtlem/spotify-client?include_prereleases&label=changelog)](https://github.com/Ismailtlem/spotify-client/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Ismailtlem/spotify-client/blob/main/LICENSE)

wrapper api around spotify api

## Installation

Install this library using `pip`:

```bash
pip install spotify-client
```

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd spotify-client
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

Create a new .env file following the structure of the file sample.env

```bash
cp sample.env .env
```

To run the tests (No tests yet ...)

```bash
pytest
```
