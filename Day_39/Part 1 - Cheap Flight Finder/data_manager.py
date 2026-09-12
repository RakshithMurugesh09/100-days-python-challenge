import gspread
from google.oauth2.service_account import Credentials


SPREADSHEET_NAME = "Flight Deals"
SERVICE_ACCOUNT_FILE = "service_account.json"
WORKSHEET_INDEX = 0

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


class Spreadsheet:
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

        records = self.sheet.get_all_records()

        self.destination_data = []

        for row_num, row in enumerate(records, start=2):
            self.destination_data.append({
                "id": row_num,
                "city": row["City"],
                "iataCode": row["IATA Code"],
                "lowestPrice": row["Lowest Price"]
            })

        return self.destination_data

    def update_iata_code(self, **kwargs):
        """
        Update the IATA Code column for one destination.

        Args:
            row_number: Actual Google Sheets row number.
            iata_code: Airport or city IATA code, such as BLR.
        """

        row_id = kwargs["row_id"]
        iata_code = kwargs["iata_code"]

        self.sheet.update_cell(
            row_id,
            2,
            iata_code
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