#!/usr/bin/env python3

import sys
import csv
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def load_csv(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def load_traffic_data(filename):
    df = load_csv(filename)
    traffic = {}
    for i in range(1, len(df)):
        y = df[i][5].split('/')[0]
        m = df[i][5].split('/')[1]
        if traffic.get(m) is None:
            traffic[m] = {}
        if traffic[m].get(y) is None:
            traffic[m][y] = 0
        traffic[m][y] += 1
    for m in traffic:
        curM = traffic[m].values()
        traffic[m] = sum(curM) / len(curM)
    return [x[1] for x in sorted(traffic.items(), key=lambda x: int(x[0]))]


def load_climate_data(filename):
    df = load_csv(filename)
    climate = {}
    for i in range(1, len(df)):
        y = df[i][5]
        m = df[i][6]
        temp = df[i][11]
        rain = df[i][17]
        snow = df[i][19]
        if temp == '' or rain == '' or snow == '':
            continue
        if climate.get(m) is None:
            climate[m] = {
                'temp': {},
                'rain': {},
                'snow': {}
            }
        if climate[m]['temp'].get(y) is None:
            climate[m]['temp'][y] = float(temp)
        if climate[m]['rain'].get(y) is None:
            climate[m]['rain'][y] = float(rain)
        if climate[m]['snow'].get(y) is None:
            climate[m]['snow'][y] = float(snow)
    for m in climate:
        curT = climate[m]['temp'].values()
        curR = climate[m]['rain'].values()
        curS = climate[m]['snow'].values()
        climate[m] = [
            sum(curT) / len(curT),
            sum(curR) / len(curR),
            sum(curS) / len(curS)
        ]
    return [x[1] for x in sorted(climate.items(), key=lambda x: int(x[0]))]


def main():
    if len(sys.argv) != 4:
        print("Please input the weather info, in the order of temperature, rain, and snow.")
        print("Usage: python3 WeatherAccident.py <number1> <number2> <number3>")
        print("Example: python3 WeatherAccident.py -7 44 8")
        return
    try:
        temp = float(sys.argv[1])
        rain = float(sys.argv[2])
        snow = float(sys.argv[3])
    except ValueError:
        print("All arguments must be numbers.")
        return

    traffic_data = load_traffic_data('data/traffic.csv')
    climate_data = load_climate_data('data/climate.csv')
    model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    model.fit(climate_data, traffic_data)
    res = model.predict([[temp, rain, snow]])
    if res[0] < 0:
        print("The prediction is negative, which is not possible. Try another input.")
        return
    print(
        f'There should be `{round(res[0])}` traffic accidents in this month if the temperature was like that.')


if __name__ == "__main__":
    main()
