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
        # TODO
        pass

    def read(self):
        # TODO
        pass

    def close(self):
        # TODO
        pass


class CSVDataSource(DataSource):

    def connect(self):
        # TODO
        pass

    def read(self):
        # TODO
        pass

    def close(self):
        # TODO
        pass


class JSONDataSource(DataSource):

    def connect(self):
        # TODO
        pass

    def read(self):
        # TODO
        pass

    def close(self):
        # TODO
        pass


def ingest(source):
    # TODO
    pass


# Test your implementation
# ingest(CSVDataSource())
# ingest(APIDataSource())
# ingest(JSONDataSource())