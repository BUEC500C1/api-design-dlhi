import json
import requests

from config import Config
from airport_data import AirportData

weather_api_key = Config.OPENWEATHER_API_KEY

class AirportWeather():
    def __init__(self, gpscode):
        self.gps_code = gpscode
        self.name = ""
        self.latit = 0
        self.longit = 0
        self.airport_data = AirportData('csv/airports.csv')

    def getAirportInfo(self):
        airport = {
            'airport': {
                'gps_code': self.gps_code,
                'name': self.name,
                'lat': self.latit,
                'long': self.longit
            }
        }
        return airport

    def setAirport(self, airportName, latitude, longitude):
        self.name = airportName
        self.latit = latitude
        self.longit = longitude

    def setAirportData(self):
        name, lati, longi = self.airport_data.get_code_data(self.gps_code)
        self.setAirport(name, lati, longi)
    
    def getAirportConditions(self):
        url = "https://api.openweathermap.org/data/2.5/weather?"
        api_url = f"appid={weather_api_key}&"
        coord = f"lat={self.latit}&lon={self.longit}&"

        airport_request = requests.get(url + api_url + coord).json()

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

        airport_info = {
            'airport_data': {
                
                    'conditions': {
                        'cond': condition,
                        'desc_cond': desc_conditon,
                        'temp': temp,
                        'humid': humidity,
                        'pres': pressure
                    },
                    'loc_info': {
                        'city': city,
                        'country': country
                    }
            }       
        }
        return airport_info

if __name__ == "__main__":
    air = AirportWeather('00A')
    air.setAirportData()
    info = air.getAirportInfo()
    info2 = air.getAirportConditions()

    print(info)
    print(info2)