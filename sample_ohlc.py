from bitkub import Bitkub

# v3
API_KEY = ""
API_SECRET = ""


bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

coin_name = 'BTC'
symbol = f'THB_{coin_name}'

tf = 15

bk_times = int(bitkub.servertime())

time_from = (str(bk_times - (tf*60*1000)))
time_to = (str(bk_times))

ohclv = bitkub.tradingview(symbol, 15, time_from, time_to)

print(ohclv)