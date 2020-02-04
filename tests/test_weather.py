import sys

sys.path.append('../src')

from weather import AirportWeather

weatherObj = AirportWeather('KBOS')
weatherObj.setAirportData()

# Define functions to test file weather.py
def test_weather_obj():
    assert weatherObj is not None

def test_getAirportInfo():
    test_info = weatherObj.getAirportInfo()
    expected = {
        'airport': {
            'gps_code': 'KBOS',
            'name': 'General Edward Lawrence Logan International Airport',
            'lat': '42.36429977',
            'long': '-71.00520325'
        }
    }
    assert test_info == expected

# These tests work locally, do not want to put API keys onto Github

# def test_getAirportConditions():
#     test_info = weatherObj.getAirportConditions()
#     assert test_info['airport_data']['loc_info']['city'] == 'Winthrop'

# def test_getAirportForecast():
#     test_info = weatherObj.getAirportForecast()
#     assert len(test_info['airport_forecast']['time_list']) == 24