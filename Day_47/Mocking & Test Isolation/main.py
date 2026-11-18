# Mocking multiple API responses

def ingest(api_client):
    first_batch = api_client.fetch_transactions(page=1)
    second_batch = api_client.fetch_transactions(page=2)

    return first_batch + second_batch

# Creates a mock API client.

from unittest.mock import Mock, call
api_client = Mock()

# Uses side_effect to return two different batches:
# - First call: [{"id": 1}, {"id": 2}]
# - Second call: [{"id": 3}, {"id": 4}]
first_batch = [
    {"id": 1},
    {"id": 2}
]

second_batch = [
    {"id": 3},
    {"id": 4}
]

api_client.fetch_transactions.side_effect = [
    first_batch,
    second_batch
]


# Calls ingest(api_client).
result = ingest(api_client)
print(result)

# Asserts that the final result contains four records.
assert result == [{"id": 1},{"id": 2},{"id": 3},{"id": 4}]


# Verifies the API was called exactly twice.
assert api_client.fetch_transactions.call_count == 2


# Verifies the first call used page=1 and the second used page=2.
api_client.fetch_transactions.assert_has_calls([
    call(page=1),
    call(page=2)
])