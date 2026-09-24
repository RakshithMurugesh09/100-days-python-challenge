from dataclasses import dataclass

# =========================
# LOG RECORD
# =========================

@dataclass
class LogRecord:
    timestamp: str
    status: str
    service: str
    details: str
    duration: float

    def __post_init__(self):
        self.status = self.status.strip().upper()
        self.service = self.service.strip().upper()

        if self.status not in ("WARNING", "ERROR", "INFO", "DEBUG"):
            raise ValueError(f"Invalid status: {self.status}")

        if self.duration < 0:
            raise ValueError(f"Invalid duration: {self.duration}")


# =========================
# RAW LOG DATA
# =========================

raw_logs = [
    {
        "timestamp": "2026-09-24 09:00:00",
        "status": "info",
        "service": "Authentication",
        "details": "User login successful",
        "duration": 0.25,
    },
    {
        "timestamp": "2026-09-24 09:05:12",
        "status": "warning",
        "service": "Database",
        "details": "Query execution slower than expected",
        "duration": 1.85,
    },
    {
        "timestamp": "2026-09-24 09:10:45",
        "status": "error",
        "service": "Payment",
        "details": "Payment gateway timeout",
        "duration": 3.42,
    },
    {
        "timestamp": "2026-09-24 09:15:30",
        "status": "info",
        "service": "API",
        "details": "Customer data retrieved",
        "duration": 0.72,
    },
    {
        "timestamp": "2026-09-24 09:20:18",
        "status": "warning",
        "service": "Cache",
        "details": "Cache miss threshold exceeded",
        "duration": 1.10,
    },
    {
        "timestamp": "2026-09-24 09:25:00",
        "status": "error",
        "service": "Email",
        "details": "SMTP connection failed",
        "duration": 2.95,
    },
    {
        "timestamp": "2026-09-24 09:30:40",
        "status": "info",
        "service": "Reporting",
        "details": "Daily report generated",
        "duration": 4.50,
    },
    {
        "timestamp": "2026-09-24 09:35:00",
        "status": "critical",
        "service": "Server",
        "details": "Unexpected shutdown",
        "duration": 5.00,
    },
    {
        "timestamp": "2026-09-24 09:40:00",
        "status": "error",
        "service": "Network",
        "details": "Packet loss detected",
        "duration": -1.25,
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
    except ValueError as e:
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

longest_duration = max([log.duration, log] for log in valid_logs)

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
print(f"Longest Duration: {longest_duration[0]} and \n"
      f"log is {longest_duration[1]}")