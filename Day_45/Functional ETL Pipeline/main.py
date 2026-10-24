from functools import partial, reduce


transactions = [
    {"id": 1, "customer": " alice ", "amount": 1000, "status": "SUCCESS"},
    {"id": 2, "customer": " bob ", "amount": 300, "status": "FAILED"},
    {"id": 3, "customer": " charlie ", "amount": 700, "status": "SUCCESS"},
    {"id": 4, "customer": " david ", "amount": 200, "status": "SUCCESS"},
    {"id": 5, "customer": " eve ", "amount": 1500, "status": "SUCCESS"}
]


def validate_transaction(record, min_amount):
    # Check status and minimum amount
    return record["status"] == "SUCCESS" and record["amount"] >= min_amount


def normalize_customer(record):
    # Strip whitespace and uppercase customer name
    # Return a NEW dictionary
    return {
        **record,
        "customer": record["customer"].strip().upper()
    }


def add_metadata(record):
    # Add processed metadata
    # Return a NEW dictionary
    return {
        **record,
        "is_processed": True
    }


def transform_transaction(record):
    # Normalize customer first
    normalized_record = normalize_customer(record)

    # Then add metadata
    return add_metadata(normalized_record)


def calculate_total(acc, record):
    # Add record amount to accumulator
    return acc + record["amount"]


def run_pipeline(records, min_amount):

    # 1. Configure validation using partial()
    validator = partial(validate_transaction, min_amount=min_amount)

    # 2. Filter valid records using filter()
    valid_records = filter(validator, records)

    # 3. Transform records using map()
    processed_records = list(map(transform_transaction, valid_records))

    # 4. Calculate total using reduce()
    total = reduce(calculate_total, processed_records, 0)

    # 5. Return processed records and total
    return processed_records, total


# Execute the pipeline
processed, total = run_pipeline(transactions, 500)

print("Processed transactions:")

for record in processed:
    print(record)

print("Total amount:", total)