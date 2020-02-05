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

    def __repr__(self):
        return f'{{"gps_code": {self.gps_code}, "name": {self.name}, "lat": {self.latit}, "long": {self.longi}}}'  # noqa: E501

    def __str__(self):
        return f"Airport: {self.name}\nGPS Code: {self.gps_code}\nCoordinates: ({self.latit}, {self.longi})"  # noqa: E501

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
        # Description condition can be clear, rain, foggy, etc.
        condition = airport_request["weather"][0]["main"]
        desc_conditon = airport_request["weather"][0]["description"]
        # Convert Kelvin to Farenheit and round to two decimal places
        temp = f'{((airport_request["main"]["temp"] - 273.15) * (9/5) + 32):.2f}'  # noqa: E501
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
        url = "https://api.openweathermap.org/data/2.5/forecast?"
        api_url = f"appid={weather_api_key}&"

        # Test using coordinates Boston with (42.3601, 71.0589)
        coord = f"lat={self.latit}&lon={self.longit}&"
        # coord = f"lat=42.3601&lon=-71.0589&"

        forecast_request = requests.get(url + coord + api_url).json()

        temp_list = []
        humid_list = []
        time_list = []

        for i in range(0, 24):
            kelvin = forecast_request['list'][i]['main']['temp']
            humidity = forecast_request['list'][i]['main']['humidity']
            farenheit = round((kelvin - 273.15) * (9/5) + 32)

            temp_list.append(farenheit)
            humid_list.append(humidity)
            time_list.append(forecast_request['list'][i]['dt'] - 255600)

        forecast = {
            "airport_forecast": {
                "time_list": time_list,
                "humid_list": humid_list,
                "temp_list": temp_list
            }
        }

        return forecast

    def getWeather(self):
        self.setAirportData()
        airport_info = self.getAirportInfo()
        airport_conditon = self.getAirportConditions()
        airport_forecast = self.getAirportForecast()

        data = {
            "info": airport_info,
            "condition": airport_conditon,
            "forecast": airport_forecast
        }

        return data


if __name__ == "__main__":
    air = AirportWeather('00A')
    result = air.getWeather()
    print(json.dumps(result, indent=4, sort_keys=True))
