import pandas as pd
import sys
import requests
import db_connection
from datetime import datetime

url = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
wb_api_token = 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjMxMjI1djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyNDA5ODY2NywiaWQiOiI4NWU3NjNhNC04NGEyLTRmYmEtYmQyNC1kMDdkNjM3ZGQ1NzMiLCJpaWQiOjExMjM3MzI3NSwib2lkIjoxMzM1OTUyLCJzIjoxMDczNzQyMzM0LCJzaWQiOiI1ZjFmOTM4My03MmM4LTQ2NDgtYWRhZC0wMDZhODM2ZTNkMGYiLCJ0IjpmYWxzZSwidWlkIjoxMTIzNzMyNzV9.YgYDrYAo-nfPCnOxeZ8QE6HwApDfVQno547Ye1p3JMu83V4iAH3w4R5BOCRlHxFbisluvLvyFlJMmbR3Rx0eQw'
headers = {'Authorization': wb_api_token}
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
