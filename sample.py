from bitkub import Bitkub
import time

# v3
API_KEY = ""
API_SECRET = ""


bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

coin_name = 'BTC'
symbol = f'THB_{coin_name}'
amountTHB = 15.00

# Get last price
ticker = bitkub.ticker(symbol)
last_price = ticker[symbol]['last']
print(f'Last price: {last_price}')

# Get lowestAsk price
ask_price = ticker[symbol]['lowestAsk']
print(f'Ask price: {ask_price}')

# Get highestBid price
bid_price = ticker[symbol]['highestBid']
print(f'Bid price: {bid_price}')

# buy order
buy_order = bitkub.place_bid(sym=symbol, amt=amountTHB, rat=ask_price)
print(f'Buy order: {buy_order}')

# wait 5 seconds for order to be filled
time.sleep(5)

# get balance
balance = bitkub.balances()
# print(balance)
symbol_balance = balance['result'][coin_name]['available']
print(f'Balance: {symbol_balance}')

my_open_orders = bitkub.my_open_orders(sym=symbol)
print(f'my_open_orders: {my_open_orders}')

# sell order
# sell_order = bitkub.place_ask(sym=symbol, amt=symbol_balance, rat=bid_price)
# print(f'Sell order: {sell_order}')

# # sell order by fiat
coinTHB = symbol_balance*bid_price
sell_order = bitkub.place_ask_by_fiat(sym=symbol, amt=coinTHB, rat=bid_price)
print(f'Sell order by fiat: {sell_order}')

# wait 5 seconds for order to be filled
time.sleep(5)

# get balance
balance = bitkub.balances()
symbol_balance = balance['result'][coin_name]['available']
print(f'Balance: {symbol_balance}')

# print(bitkub.crypto_generate_address(sym=symbol))
# print(bitkub.crypto_address())
# print(bitkub.crypto_deposit_history())
# print(bitkub.crypto_withdraw_history())
# print(bitkub.fiat_accounts())
# print(bitkub.fiat_deposit_history())
# print(bitkub.fiat_withdraw_history())
