from flask import Flask
from flask_restful import Api

from resources import WeatherResources, AirportResources

app = Flask(__name__)
api = Api(app)

api.add_resource(WeatherResources, '/weatherData')
api.add_resource(AirportResources, '/airportInfo')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
