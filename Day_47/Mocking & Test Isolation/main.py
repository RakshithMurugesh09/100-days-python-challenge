import pytest
from unittest.mock import Mock

def test_fetch_transactions():
    api_client = Mock()

    api_client.fetch_transactions.return_value = []

    result = fetch_transactions(
        api_client,
        start_date="2026-11-01",
        end_date="2026-11-18"
    )

    assert result == []

    api_client.fetch_transactions.assert_called_once_with(
        start_date="2026-11-01",
        end_date="2026-11-18"
    )