import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)


class Timer:
    def __init__(self, task_name):
        self.task_name = task_name
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        logging.info(f"{self.task_name} started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        duration = self.end_time - self.start_time

        if exc_type is None:
            logging.info(f"{self.task_name} completed successfully")
        else:
            logging.error(
                f"{self.task_name} failed | {exc_type.__name__}: {exc_value}"
            )

        logging.info(f"Execution Time: {duration:.4f} seconds")

        # Return False so exceptions are propagated
        return False


# Successful execution
with Timer("API Request"):
    time.sleep(2)

print("-" * 40)

# Failed execution
try:
    with Timer("Database Query"):
        time.sleep(1)
        raise ValueError("Connection timeout")
except ValueError:
    pass