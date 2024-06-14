import pandas as pd
import sys
import key
import requests
import db_connection
from datetime import datetime

url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
headers = {'Authorization': key.wb_api_token}
params = {'dateFrom' : '2023-08-31'}

try:
	request = requests.get(url, headers = headers, params = params)
	if request.status_code != 200:
				print("Request status: ", request.status_code, '\nMessage: ', request.text)
				sys.exit()
	# print(request.text)
except Exception as exc:
	print(exc)
	sys.exit()
df = pd.json_normalize(request.json())
df = df[df['warehouseName'] != 'Санкт-Петербург Шушары']
date = datetime.today().strftime('%Y-%m-%d')
df['date loading'] = date
df.to_excel('stocks' + date + '.xlsx')

db_connection.db_creation(df, 'stocks_all')
