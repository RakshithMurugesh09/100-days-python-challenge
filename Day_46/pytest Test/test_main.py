import pytest

from main import run_pipeline


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "customer": " alice ", "amount": 1000, "status": "SUCCESS"},
        {"id": 2, "customer": " bob ", "amount": 300, "status": "FAILED"},
        {"id": 3, "customer": " charlie ", "amount": 700, "status": "SUCCESS"}
    ]


def test_pipeline_record_count(sample_transactions):
    records, total = run_pipeline(sample_transactions, 500)

    assert len(records) == 2


def test_pipeline_total(sample_transactions):
    records, total = run_pipeline(sample_transactions, 500)

    assert total == 1700


def test_pipeline_normalization(sample_transactions):
    records, total = run_pipeline(sample_transactions, 500)

    assert records[0]["customer"] == "ALICE"


def test_pipeline_metadata(sample_transactions):
    records, total = run_pipeline(sample_transactions, 500)

    assert records[0]["is_processed"] is True


def test_pipeline_empty_input():
    records, total = run_pipeline([], 500)

    assert records == []
    assert total == 0
