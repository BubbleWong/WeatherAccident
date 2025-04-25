# WeatherAccident

An AI model that predicts traffic accidents based on weather information.

We used a dataset of `traffic accidents` in Ottawa, Canada and a dataset of `climate/weather` information. We preproccessed the datasets and alligned by months as a training dataset. We fit the dataset to a `Ridge Regression` model. It can predict the number of accidents based on the weather information like temperature, snow, and rain.

## How to use

```bash
$ pip install -r requirements.txt
$ python3 WeatherAccident.py <temperature> <snow> <rain>
```

## Demo

```bash
$ python3 WeatherAccident.py 2 0 67
There should be `1197` traffic accidents in this month if the temperature was like that.
```

## Data sources

- [Traffic Collision Data](https://open.ottawa.ca/datasets/ottawa::traffic-collision-data/about)
- [Climate/weather data: OTTAWA CDA](https://www.climate.weather.gc.ca/climate_data/monthly_data_e.html?hlyRange=%7C&dlyRange=1889-11-01%7C2025-03-09&mlyRange=1889-01-01%7C2006-12-01&StationID=4333&Prov=ON&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=2024&EndYear=2025&selRowPerPage=25&Line=0&searchMethod=contains&Month=4&Day=6&txtStationName=Ottawa&timeframe=3&Year=2006)
