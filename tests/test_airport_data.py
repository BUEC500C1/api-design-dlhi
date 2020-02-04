import sys
import csv
import pytest

sys.path.append('../src')

from airport_data import AirportData

# Define functions to test file airport_data.py
def test_file_integrity():
    airportObj = AirportData('../src/csv/airports.csv')
    
    with open('../src/csv/airports.csv', 'r', encoding='utf-8') as f:
        parser = csv.reader(f)
        next(parser)
        row = next(parser)
        gpscode, name, lat, lon = row[12], row[3], row[4], row[5]

    objname, objlat, objlon = airportObj.get_code_data(gpscode)

    assert airportObj is not None
    assert objname == name
    assert objlat == lat
    assert objlon == lon

def test_file_handler():
    with pytest.raises(OSError):
       AirportData(100)

    with pytest.raises(FileNotFoundError):
       AirportData('../src/csv/file_not_here.csv')

    with pytest.raises(IOError):
       AirportData('../src/csv/empty_airports.csv')

def test_get_code_data():
    airportObj = AirportData('../src/csv/airports.csv')
    airport = airportObj.get_code_data('KBOS')
    assert airport[0] == 'General Edward Lawrence Logan International Airport'
