import requests
import datetime
import time
import termplotlib as tpl
import config

payload = {
  'access_key': config.api_key,
  'symbols': config.symbols
}

api_result = requests.get('http://api.marketstack.com/v1/eod', params=payload)

api_response = api_result.json()

price = []
dates = []

for stock_data in api_response['data']:
    price.append(int(float(stock_data['high'])))
    dates.append(int(time.mktime(datetime.datetime.strptime(stock_data['date'], "%Y-%m-%dT%H:%M:%S+%f").timetuple())))

fig = tpl.figure()
fig.plot(dates, price, width=200, height=50)
fig.show()
