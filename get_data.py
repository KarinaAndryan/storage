import key
import class_req
import pandas as pd

url = 'https://seller-analytics-api.wildberries.ru/api/v1/paid_storage/tasks/{157175f8-8a82-4e6b-b9da-beab21bc7343}/download'
headers = {'Authorization' : key.wb_api_token}
params = {'task_id' : "157175f8-8a82-4e6b-b9da-beab21bc7343"}
request = class_req.Request(url, headers, params).get_request()
request = pd.json_normalize(request.json())
request.to_excel('хранение.xlsx')