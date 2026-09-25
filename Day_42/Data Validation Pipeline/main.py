from dataclasses import dataclass
from typing import Literal, Union, Dict, Any, Optional

# =========================
# LOG RECORD
# =========================

@dataclass
class LogRecord:
    service: str
    status: Literal["INFO", "WARNING", "ERROR"]
    duration: float
    metadata: Dict[str, Any]
    error_code: Optional[int]
    request_id: Union[str, int]

    def __post_init__(self):
        if not isinstance(self.duration, (int, float)):
            raise TypeError("Duration must be a number")

        if self.duration < 0:
            raise ValueError("Duration must be positive")

        if self.status not in ["INFO", "WARNING", "ERROR"]:
            raise ValueError(
                "Status must be one of 'INFO', 'WARNING', 'ERROR'"
            )

        if not isinstance(self.metadata, dict):
            raise TypeError("Metadata must be a dictionary")

        if not isinstance(self.request_id, (str, int)):
            raise TypeError("Request ID must be str or int")

# =========================
# RAW LOG DATA
# =========================

raw_logs = [
    {
        "service": "UserAPI",
        "status": "INFO",
        "duration": 0.145,
        "metadata": {
            "endpoint": "/users",
            "method": "GET",
            "user_id": 101
        },
        "error_code": None,
        "request_id": "REQ-1001"
    },
    {
        "service": "PaymentService",
        "status": "WARNING",
        "duration": 1.827,
        "metadata": {
            "transaction_id": "TXN-5678",
            "retry_count": 1,
            "reason": "Slow response"
        },
        "error_code": None,
        "request_id": "REQ-1002"
    },
    {
        "service": "AuthService",
        "status": "ERROR",
        "duration": 0.532,
        "metadata": {
            "username": "john.doe",
            "ip": "192.168.1.10"
        },
        "error_code": 401,
        "request_id": "REQ-1003"
    },
    {
        "service": "InventoryService",
        "status": "INFO",
        "duration": 0.089,
        "metadata": {
            "product_id": "P12345",
            "action": "stock_check"
        },
        "error_code": None,
        "request_id": 1004
    },
    {
        "service": "NotificationService",
        "status": "ERROR",
        "duration": 2.104,
        "metadata": {
            "channel": "email",
            "recipient": "user@example.com"
        },
        "error_code": 503,
        "request_id": "REQ-1005"
    },
# INVALID LOGS

    # Invalid status
    {
        "service": "AuthService",
        "status": "SUCCESS",  # should be INFO/WARNING/ERROR
        "duration": 0.45,
        "metadata": {"user": "rakshith"},
        "error_code": None,
        "request_id": "REQ-2001"
    },

    # Invalid duration type
    {
        "service": "PaymentService",
        "status": "INFO",
        "duration": "1.25",  # should be float
        "metadata": {"amount": 500},
        "error_code": None,
        "request_id": 2002
    },

    # Invalid metadata and request_id
    {
        "service": "InventoryService",
        "status": "ERROR",
        "duration": 0.78,
        "metadata": "item not found",  # should be dict
        "error_code": 404,
        "request_id": ["REQ-2003"]  # should be str or int
    }

]

# =========================
# PROCESS LOGS
# =========================

valid_logs = []
invalid_logs = []

for log in raw_logs:
    try:
        record = LogRecord(**log)
        valid_logs.append(record)
    except (ValueError, TypeError) as e:
        invalid_logs.append(f"{log} --> {e}")

# =========================
# STATISTICS
# =========================

total_valid_logs = len(valid_logs)
total_invalid_logs = len(invalid_logs)

error_logs_count = 0
for log in valid_logs:
    if log.status == "ERROR":
        error_logs_count += 1

longest_duration = max(valid_logs, key=lambda log: log.duration)

# =========================
# OUTPUT
# =========================

print("===== VALID LOGS =====")

for log in valid_logs:
    print(log)

print("\n===== INVALID LOGS =====")

for log in invalid_logs:
    print(log)

print("\n===== STATISTICS =====")

print(f"Total Valid Logs: {total_valid_logs}")
print(f"Total Invalid Logs: {total_invalid_logs}")
print(f"ERROR Logs: {error_logs_count}")
print(f"Longest Duration: {longest_duration.duration} and \n"
      f"log is {longest_duration}")