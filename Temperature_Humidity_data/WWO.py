import requests
import csv

# url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=fe87d912d7e045e6b9a91044202304&q=London&format=json&date=2020-01-22&enddate=2020-04-22'

# params = dict(
#     origin='Chicago,IL',
#     destination='Los+Angeles,CA',
#     waypoints='Joplin,MO|Oklahoma+City,OK',
#     sensor='false'
# )

# resp = requests.get(url=url)
# data = resp.json()  # Check the JSON Response Content documentation below

# list_of_dates = data["data"]["weather"]
# # print(list_of_dates)
# first_date = list_of_dates[0]
# # print(first_date["date"])
# avg_temp = first_date["avgtempC"]
# humidity = first_date["hourly"][1]["humidity"]
# print(first_date["date"], avg_temp, humidity)

# ,"Italy", "France", "Germany", "Turkey", "UK", "New York"]
# , "Spain", "Italy", "France", "Germany", "Turkey", "UK", "New York"]
regions = ["Hubei", "Spain", "Italy", "France",
           "Germany", "Turkey", "UK", "New York"]
columns = [["Date", "Region", "AvgTemp", "Humidity"]]
# print(list_of_dates)
for region in regions:
    dates = ["2020-01-22", "2020-02-26", "2020-04-01"]
    for st_date in dates:
        url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=fe87d912d7e045e6b9a91044202304&q=' + \
            region+'&format=json&date=' + st_date + '&enddate=2020-04-22'
        resp = requests.get(url=url)
        data = resp.json()
        if region == "UK":
            region = "United Kingdom"
        list_of_dates = data["data"]["weather"]
        for date in list_of_dates:
            first_date = date
            # print(first_date["date"])
            day = first_date["date"]
            avg_temp = first_date["avgtempC"]
            avg_humidity = 0
            count = 0
            for data in first_date["hourly"]:
                humidity = float(data["humidity"])
                # print(humidity, " avg - ", avg_humidity)
                avg_humidity = avg_humidity + humidity
                count += 1
            avg_humidity = avg_humidity/count
            # print(first_date["date"], avg_temp, humidity)
            columns.append([day, region, avg_temp, avg_humidity])

with open('Avg_Temperature_Humidity_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(columns)
