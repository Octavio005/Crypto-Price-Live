import requests
from win10toast import ToastNotifier

request_crypto = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
request_dollar = requests.get('https://api.bluelytics.com.ar/v2/latest')

eth_usdt_json = request_crypto.json()
blue_usd_ars = request_dollar.json()

symbol_crypto = eth_usdt_json['symbol'].replace('H', 'H/')
price_crypto = round(float(eth_usdt_json['price']), 2)

symbol_fiat = list(blue_usd_ars.keys())[1]
price_fiat = round(float(blue_usd_ars['blue']['value_sell']), 2)

toaster = ToastNotifier()

toaster.show_toast(symbol_crypto + '  ' + str(price_crypto), symbol_fiat + '  ' + str(price_fiat), duration=20)