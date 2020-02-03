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
        self.airport_data = AirportData()

    def setAirport(self, airportName, latitude, longitude):
        self.name = airportName
        self.latit = latitude
        self.longit = longitude

    def setAirportData(self, gps_code):
        name, lati, longi = self.airport_data.get_code_data(gps_code)
        self.setAirport(name, lati, longi)
    
    def getAirportConditions(self):
        #url = "https://api.openweathermap.org/data/2.5/weather?"
        #api_url = f"appid={weather_api_key}&"
        #coord = f"lat={self.latit}&lon={self.longit}&"

        #airport_request = requests.get(url + api_url + coord).json()

        # Extract current weather
        # condition can be clear, rain, foggy, etc.
        condition = airport_request["weather"][0]["main"]
        desc_conditon = airport_request["weather"][0]["description"]
        # Convert Kelvin to Farenheit and round to two decimal places
        temp = f'{((airport_request["main"]["temp"] - 273.15) * (9/5) + 32):.2f}'
        humidity = airport_request["main"]['humidity']
        pressure = airport_request["main"]['pressure']

        # Extract location info
        city = airport_request["name"]
        country = airport_request["sys"]["country"]

        

if __name__ == "__main__":
    air = AirportWeather()
    air.setAirportData('00A')
    air.getAirportConditions()