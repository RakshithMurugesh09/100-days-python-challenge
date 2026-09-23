import requests
import os
from dotenv import load_dotenv

load_dotenv()
class DataManager:

    def __init__(self):
        self.endpoint = os.getenv("SHEETY_ENDPOINT")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")

    def get_destination_data(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        return response.json()["prices"]

    def update_iata_code(self, row_id, code):
        body = {"price": {"iataCode": code}}
        requests.put(url=f"{self.endpoint}/{row_id}",json=body)

    def add_user(self, first_name, last_name, email):
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(url=self.users_endpoint, json=body)
        response.raise_for_status()

    def get_customers(self):
        response = requests.get(self.users_endpoint)
        response.raise_for_status()
        return response.json()["users"]
