import os
import requests
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class Spreadsheet:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()

        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_iata_code(self, row_id, iata_code):
        body = {"price":{"iataCode": iata_code}}

        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=body)
        response.raise_for_status()
        return response.json()


