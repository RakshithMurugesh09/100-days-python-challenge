from typing import Any, Callable


records = [
    {"id": 1, "status": "SUCCESS"},
    {"id": 2, "status": "FAILED"},
    {"id": 3, "status": "SUCCESS"},
    {"id": 4, "status": "PENDING"}
]


# 1. Create a configurable status filter
def create_status_filter(expected_status: str):

    def filter_record(record: dict) -> bool:
        return record.get("status") == expected_status

    return filter_record


# 2. Create a configurable transformer
def create_transformer(field: str, value: Any):

    def transform_record(record: dict) -> dict:
        # Return a new dictionary, preserving the original
        return {**record, field: value}

    return transform_record


# 3. Create a stateful record counter
def create_counter():

    count = 0

    def increment_counter() -> int:
        nonlocal count
        count += 1
        return count

    return increment_counter


# 4. Generic ETL processing pipeline
def process_pipeline(records: list[dict],filter_fn: Callable,transform_fn: Callable,counter_fn: Callable) -> list[dict]:

    processed_records = []

    for record in records:

        # Step 1: Validate/filter the record
        if not filter_fn(record):
            continue

        # Step 2: Transform successfully filtered data
        transformed_record = transform_fn(record)

        # Step 3: Store processed data
        processed_records.append(transformed_record)

        # Step 4: Increment count after successful processing
        count = counter_fn()

        print(f"Processed count: {count}")

    return processed_records


# 5. Configure the pipeline
status_filter = create_status_filter("SUCCESS")
transformer = create_transformer("processed", True)
counter = create_counter()


# 6. Execute the pipeline
result = process_pipeline(records,status_filter,transformer,counter)


# 7. Display results
print("\nProcessed Records:")
for record in result:
    print(record)

print("\nOriginal Records:")
for record in records:
    print(record)
