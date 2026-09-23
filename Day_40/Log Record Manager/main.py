from dataclasses import dataclass


@dataclass
class LogRecord:
    timestamp: str
    status: str
    service: str
    details: str
    duration: float


# Sample logs
logs = [
    LogRecord("10:30", "ERROR", "payment-service", "Database connection failed", 10.5),
    LogRecord("11:30", "INFO", "payment-service", "User login successful", 1.2),
    LogRecord("12:30", "WARNING", "payment-service", "High response time", 5.8),
    LogRecord("13:30", "DEBUG", "payment-service", "CPU working", 1.5),
]

# Statistics
longest_duration = max(log.duration for log in logs)
error_count = sum(1 for log in logs if log.status == "ERROR")

# Display all logs
print("===== ALL LOGS =====")
for log in logs:
    print(log)

# Display error logs
print("\n===== ERROR LOGS =====")
for log in logs:
    if log.status == "ERROR":
        print(log)

# Display statistics
print("\n===== STATISTICS =====")
print(f"Total Logs      : {len(logs)}")
print(f"Error Logs      : {error_count}")
print(f"Longest Duration: {longest_duration} seconds")