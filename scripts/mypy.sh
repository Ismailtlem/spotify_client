#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=.

mypy --show-error-codes spotify_client --disable-recursive-aliases
