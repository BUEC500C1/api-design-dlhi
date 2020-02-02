import json
import requests

from config import Config
from airport_data import AirportData

weather_api_key = Config.OPENWEATHER_API_KEY

class AirportWeather():
    def __init__(self):
        self.name = ""
        self.latit = 0
        self.longit = 0

    def setAirport(self, airportName, latitude, longitude):
        self.name = airportName
        self.latit = latitude
        self.longit = longitude

    def getAirportData(self, gps_code):
        airport = AirportData('airports.csv')
        name, lati, longi = airport.get_code_data(gps_code)
        self.setAirport(name, lati, longi)

air = AirportWeather()
air.getAirportData('00A')
print(air.name)