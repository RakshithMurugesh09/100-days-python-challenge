from dataclasses import dataclass


# =========================
# LOG RECORD
# =========================

@dataclass
class LogRecord:
    # TODO: define fields
    pass

    def __post_init__(self):
        # TODO: normalize status
        # TODO: normalize service

        # TODO: validate status

        # TODO: validate duration
        pass


# =========================
# RAW LOG DATA
# =========================

raw_logs = [
    # TODO: create at least 7 LogRecord objects
]


# =========================
# PROCESS LOGS
# =========================

valid_logs = []
invalid_logs = []


# TODO:
# Process each log
# Catch ValueError
# Store valid logs
# Store invalid logs


# =========================
# STATISTICS
# =========================

# TODO: total valid logs

# TODO: total invalid logs

# TODO: count ERROR logs

# TODO: find longest duration


# =========================
# OUTPUT
# =========================

print("===== VALID LOGS =====")

# TODO


print("\n===== INVALID LOGS =====")

# TODO


print("\n===== STATISTICS =====")

# TODO