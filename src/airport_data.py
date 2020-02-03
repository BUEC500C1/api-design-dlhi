import os
import csv
import json
from pathlib import Path

directory = os.path.abspath(os.path.dirname(__file__))

class AirportData():
    def __init__(self, file):
        self.airport_data = {}

        if not type(file) is str:
            raise OSError("Enter file name in string format.")

        # The airport csv data must be in the same directory as the rest of the source files
        file_check = Path(f'{directory}/{file}')
        print(file_check)
        if not file_check.is_file():
            raise FileNotFoundError(f'Errors finding airport data file.')

        # Check if file is empty
        if os.stat(file_check).st_size == 0:
            raise IOError("Airport data file is empty.")

        with open(file_check, 'r', encoding='utf-8') as f:
            parser = csv.reader(f)
            skiprow = next(parser)
            for row in parser:
                # Check if in the USA
                if row[8] == "US":
                    # dict(gpscode) : (name, latitude, longitude)
                    self.airport_data[row[12]] = (row[3], row[4], row[5])

    def get_code_data(self, gps_code):
        return self.airport_data[gps_code]

if __name__ == "__main__":
    airobj = AirportData('csv/airports.csv')
    name, lat, longi = airobj.get_code_data('00A')
    print(name, lat, longi)



