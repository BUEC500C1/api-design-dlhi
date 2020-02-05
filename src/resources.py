from flask import jsonify
from flask_restful import Resource

from webargs import fields
from webargs.flaskparser import use_args

from weather import AirportWeather


class WeatherResources(Resource):
    @use_args({"gpscode": fields.Str(required=True)})
    def get(self, args):
        airport = AirportWeather(args["gpscode"])
        result = airport.getWeather()
        return jsonify(result)


class AirportResources(Resource):
    @use_args({"gpscode": fields.Str(required=True)})
    def get(self, args):
        airport = AirportWeather(args["gpscode"])
        result = airport.getAirportInfo()
        return jsonify(result)
