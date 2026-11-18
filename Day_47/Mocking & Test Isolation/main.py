# Mocking API failures with patch

import requests

def fetch_data():
    response = requests.get("https://api.example.com/data")
    return response.json()
import pytest
from unittest.mock import patch

from main import fetch_data


def test_fetch_data_timeout():

    # Patch requests.get where main.py uses it
    with patch("main.requests.get") as mock_get:

        # Make requests.get() raise TimeoutError
        mock_get.side_effect = TimeoutError("API timeout")

        # Verify fetch_data() raises TimeoutError
        with pytest.raises(TimeoutError, match="API timeout"):
            fetch_data()

        # Verify API was called exactly once
        mock_get.assert_called_once()