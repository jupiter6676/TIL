import requests

URL = "https://api.bithumb.com/public/ticker/BTC_KRW"
response = requests.get(URL).json()

print(response.get('data').get('prev_closing_price'))