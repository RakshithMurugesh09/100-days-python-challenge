from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def close(self):
        pass


class APIDataSource(DataSource):

    def connect(self):
        print("Connecting to API...")

    def read(self):
        print("Reading data from API...")
        return {"source": "API", "data": ["user1", "user2", "user3"]}

    def close(self):
        print("Closing API connection...")


class CSVDataSource(DataSource):

    def connect(self):
        print("Opening CSV file...")

    def read(self):
        print("Reading data from CSV...")
        return [
            {"id": 1, "name": "Rakshith"},
            {"id": 2, "name": "John"}
        ]

    def close(self):
        print("Closing CSV file...")


class JSONDataSource(DataSource):

    def connect(self):
        print("Opening JSON file...")

    def read(self):
        print("Reading data from JSON...")
        return {
            "employees": [
                {"id": 101, "name": "Alice"},
                {"id": 102, "name": "Bob"}
            ]
        }

    def close(self):
        print("Closing JSON file...")


def ingest(source: DataSource):
    source.connect()
    data = source.read()
    print("Data:", data)
    source.close()
    print("-" * 40)


# Test your implementation
ingest(CSVDataSource())
ingest(APIDataSource())
ingest(JSONDataSource())