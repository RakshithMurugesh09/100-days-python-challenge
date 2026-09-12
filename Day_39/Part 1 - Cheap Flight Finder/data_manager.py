import gspread
from google.oauth2.service_account import Credentials


SPREADSHEET_NAME = "Flight Deals"
SERVICE_ACCOUNT_FILE = "service_account.json"
WORKSHEET_INDEX = 0

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class GoogleSheet:
    """Read and update destination data in Google Sheets."""

    def __init__(self):
        self.destination_data = []

        credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )

        client = gspread.authorize(credentials)

        self.sheet = (
            client
            .open(SPREADSHEET_NAME)
            .get_worksheet(WORKSHEET_INDEX)
        )

    def get_destination_data(self):
        """
        Retrieve all destination records from the worksheet.

        The first row must contain headers:
        City | IATA Code | Lowest Price
        """
        self.destination_data = self.sheet.get_all_records()
        return self.destination_data

    def update_iata_code(self, row_number, iata_code):
        """
        Update the IATA Code column for one destination.

        Args:
            row_number: Actual Google Sheets row number.
            iata_code: Airport or city IATA code, such as BLR.
        """
        if not iata_code:
            raise ValueError("IATA code cannot be empty.")

        iata_code = iata_code.strip().upper()

        # Column 2 represents column B: IATA Code
        self.sheet.update_cell(
            row=row_number,
            col=2,
            value=iata_code
        )

    def update_all_iata_codes(self, flight_data):
        """
        Find and update missing IATA codes.

        The flight_data object must contain:
        get_iata_code(city_name)
        """
        if not self.destination_data:
            self.get_destination_data()

        for row_number, destination in enumerate(
            self.destination_data,
            start=2
        ):
            city = str(destination.get("City", "")).strip()
            current_code = str(
                destination.get("IATA Code", "")
            ).strip()

            if not city:
                print(
                    f"Skipping row {row_number}: "
                    "city name is empty."
                )
                continue

            if current_code:
                print(
                    f"Skipping {city}: "
                    f"IATA code already exists ({current_code})."
                )
                continue

            iata_code = flight_data.get_iata_code(city)

            if not iata_code:
                print(f"No IATA code found for {city}.")
                continue

            self.update_iata_code(
                row_number=row_number,
                iata_code=iata_code
            )

            # Keep the locally stored data synchronized.
            destination["IATA Code"] = iata_code

            print(f"Updated {city} -> {iata_code}")

    def print_destination_data(self):
        """Print all destination records."""
        if not self.destination_data:
            print("No destination data loaded.")
            return

        for destination in self.destination_data:
            print(destination)