from serpapi import GoogleSearch
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

class FlightSearch:

    def search_flight(self,departure_id,arrival_id):

        tomorrow = datetime.now() + timedelta(days=1)


        params = {
            "engine": "google_flights",
            "departure_id": departure_id,
            "arrival_id": arrival_id,
            "outbound_date": tomorrow.strftime("%Y-%m-%d"),
            "return_date": (tomorrow + timedelta(days=7)).strftime("%Y-%m-%d"),
            "currency": "INR",
            "hl": "en",
            "api_key": os.getenv("SERPAPI_API_KEY")
        }

        search = GoogleSearch(params)

        results = search.get_dict()

        flights = results.get("best_flights", [])

        if not flights:
            return None

        cheapest = flights[0]

        return FlightData(
            price=cheapest["price"],
            origin_city=departure_id,
            destination_city=arrival_id,
            departure_date=params["outbound_date"],
            return_date=params["return_date"]
        )