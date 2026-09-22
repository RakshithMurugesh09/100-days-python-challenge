from data import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

import airportsdata

ORIGIN_CITY_IATA = "BLR"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

airports = airportsdata.load("IATA")

# STEP 1
for row in sheet_data:

    if row["iataCode"] == "":

        city = row["city"]

        for code, details in airports.items():

            if details["city"].lower() == city.lower():
                row["iataCode"] = code
                data_manager.update_iata_code(row["id"],code)
                break

# STEP 2
for destination in sheet_data:

    flight = flight_search.search_flight(departure_id=ORIGIN_CITY_IATA,arrival_id=destination["iataCode"])

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        message = (
            f"Low price alert!\n\n"
            f"{flight.origin_city} -> "
            f"{flight.destination_city}\n"
            f"₹{flight.price}\n"
            f"{flight.departure_date}\n"
            f"{flight.return_date}"
        )

        notification_manager.send_email(message)

        print("Email Sent")