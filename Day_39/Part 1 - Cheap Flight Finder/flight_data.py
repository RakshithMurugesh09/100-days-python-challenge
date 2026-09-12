import airportsdata

class FlightData():
    def __init__(self):
        self.airports = airportsdata.load()

    def get_iata_code(self, city_name):
        for code, info in self.airports.items():
            if info["city"].lower() == city_name.lower() and info["iata"]:
                return info["iata"]

        return None


