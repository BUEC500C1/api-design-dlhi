import csv
import json

# class Airport():
#     def __init__(self, gpsCode, airport_name, latitude, longitude):
#         self.gps_code = gpsCode
#         self.name = airport_name
#         self.latit = latitude
#         self.longi = longitude

#     def __repr__(self):
#         return f'{{"gps_code": {self.gps_code}, "name": {self.name}, "lat": {self.latit}, "long": {self.longi}}}'

#     def __str__(self):
#         return f"Airport: {self.name}\nGPS Code: {self.gps_code}\nCoordinates: ({self.latit}, {self.longi})"

class AirportData():
    def __init__(self, file):
        self.airport_data = {}

        with open(file, 'r', encoding='utf-8') as f:
            parser = csv.reader(f)
            skiprow = next(parser)
            for row in parser:
                # dict(gpscode) : (name, latitude, longitude)
                self.airport_data[row[12]] = (row[3], row[4], row[5])

    def get_code_data(self, gps_code):
        return self.airport_data[gps_code]

if __name__ == "__main__":
    airobj = AirportData('airports.csv')
    name, lat, longi = airobj.get_code_data('00A')
    print(name, lat, longi)


