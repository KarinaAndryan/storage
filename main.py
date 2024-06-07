import key
import class_req

url = 'https://seller-analytics-api.wildberries.ru/api/v1/paid_storage'
params = {'dateFrom' : '2024-05-27T00:00:00', 'dateTo' : '2024-06-02T23:23:59'}
headers = {'Authorization' : key.wb_api_token}
request = class_req.Request(url, headers, params).get_request()