import json
from datetime import datetime
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
        wind = airport_request["wind"]['speed']

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
                        'pres': pressure,
                        'wind': wind

                    },
                    'loc_info': {
                        'city': city,
                        'country': country
                    }
            }       
        }
        return airport_info

    def getAirportForecast(self):
        # time_now = int(datetime.utcnow().timestamp())
        # start_time = time_now - 86400
        
        url = "https://api.openweathermap.org/data/2.5/forecast?"
        api_url = f"appid={weather_api_key}&"
        
        # Test using coordinates Boston with (42.3601, 71.0589)
        ### coord = f"lat={self.latit}&lon={self.longit}&"
        coord = f"lat=42.3601&lon=-71.0589&"
        
        forecast_request = requests.get(url + coord + api_url).json()
    
        temp_list= []
        humid_list = []
        time_list = []

        for i in range(0, 23):
            kelvin = forecast_request['list'][i]['main']['temp']
            humidity = forecast_request['list'][i]['main']['humidity']
            farenheit = round((kelvinforecast - 273.15) * (9/5) + 32)
            
            temp_list.append(farenheit)
            humid_list.append(humidity)
            time_list.append(forecast_request['list'][i]['dt'] - 255600)

        return time_list, humid_list, time_list

if __name__ == "__main__":
    air = AirportWeather('00A')
    air.setAirportData()
    info = air.getAirportInfo()
    air.getAirportForecast()
    # info2 = air.getAirportConditions()

    # print(info)
    # print(info2)
    

