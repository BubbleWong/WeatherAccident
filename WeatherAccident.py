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

traffic_data = load_traffic_data('traffic.csv')

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
            climate[m]['snow'][y] =  float(snow)
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

climate_data = load_climate_data('climate.csv')




# print(climate_data)
# print(traffic_data)

model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
model.fit(climate_data, traffic_data)


print(model.predict([[0, 0, 0]]))

# yay