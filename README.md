# EC500: Homework 2
## Repository api-design-dlhi

### Author: David Li
### For Professor Osama Alshaykh
### Class EC500: Building Software


## Setup
In order to use OpenWeather's API, you need to set the OpenWeather API variable. <br>
```
export OPENWEATHER_API_KEY='################################'
```

## Testing
In order to run the server, go to the base directory and start the Flask server through the following command: <br>
```
flask run
```

You can then test the API by using a curl request. There are two different requests you can make:

1. Grab the airport logistic data from a request GPS code
```
curl http://127.0.0.1:5000/airportInfo?gpscode=KBOS
```
2. Grab the current conditions and 3 day forecast for a specific GPS code
```
curl http://127.0.0.1:5000/weatherData?gpscode=KBOS
```

