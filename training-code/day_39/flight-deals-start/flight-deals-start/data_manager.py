import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = ""

class DataManager:

    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")  # Corrected method call
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.session = requests.Session()  # Create a session object
        self.session.auth = self._authorization  # Set the session's auth attribute

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = self.session.get(url=SHEETY_PRICES_ENDPOINT)  # Use session.get
        if response.status_code == 200:
            data = response.json()
            self.destination_data = data["Lowest Price"]
            # Try importing pretty print and printing the data out again using pprint() to see it formatted.
            pprint(data)
            return self.destination_data
        else:
            response.raise_for_status()  # Raise an exception for HTTP errors

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = self.session.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            if response.status_code == 200:
                print(response.text)
            else:
                response.raise_for_status()  # Raise an exception for HTTP errors

#)



