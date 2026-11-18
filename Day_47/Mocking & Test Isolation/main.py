# patch() (Important)
import requests

def fetch_data():
    response = requests.get("https://api.example.com/data")
    return response.json()


# Write a pytest test in test_main.py that:
import pytest
# 2. Imports patch from unittest.mock.
from unittest.mock import patch

from main import fetch_data


def test_fetch_data():

    # Patch requests.get where it is used: main.requests.get
    with patch("main.requests.get") as mock_get:

        # Configure response.json()
        mock_get.return_value.json.return_value = [
            {"id": 1},
            {"id": 2}
        ]

        # Call fetch_data()
        result = fetch_data()

        # Verify two records were returned
        assert len(result) == 2

        # Verify requests.get() was called exactly once
        mock_get.assert_called_once()