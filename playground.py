record = {
    "id": 101,
    "name": "  alice  ",
    "source": "api"
}

def normalize_name(record):
    return {**record, "name": record["name"].strip()}


def add_metadata(record):
    return {**record, "processed": True}


def process_record(record):
    record = normalize_name(record)
    record = add_metadata(record)
    return record

result = process_record(record)
print(result)
print(record)
