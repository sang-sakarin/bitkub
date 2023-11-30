from bitkub import Bitkub
from unittest import TestCase


class BitkubTest(TestCase):

    @classmethod
    def setUpClass(cls):
        API_KEY = "XXXXXX"
        API_SECRET = "XXXXXX"

        cls.bitkub = Bitkub()
        cls.bitkub.set_api_key(API_KEY)
        cls.bitkub.set_api_secret(API_SECRET)

    def test_status(self):
        # print(self.bitkub.status())
        self.assertTrue(True)

    def test_servertime(self):
        # print(self.bitkub.servertime())
        self.assertTrue(True)

    def test_symbols(self):
        # print(self.bitkub.symbols())
        self.assertTrue(True)

    def test_ticker(self):
        # print(self.bitkub.ticker('THB_BTC'))
        self.assertTrue(True)

    def test_trades(self):
        # print(self.bitkub.trades(sym="THB_BTC", lmt=2))
        self.assertTrue(True)

    def test_bids(self):
        # print(self.bitkub.bids(sym="THB_BTC", lmt=2))
        self.assertTrue(True)

    def test_asks(self):
        # print(self.bitkub.asks(sym="THB_BTC", lmt=2))
        self.assertTrue(True)

    def test_books(self):
        # print(self.bitkub.books(sym="THB_BTC", lmt=1))
        self.assertTrue(True)

    def test_tradingview(self):
        # print(self.bitkub.tradingview())
        self.assertTrue(True)

    def test_depth(self):
        # print(self.bitkub.depth(sym='THB_BTC', lmt=1))
        self.assertTrue(True)

    def test_wallet(self):
        # print(self.bitkub.wallet())
        self.assertTrue(True)

    def test_balances(self):
        # print(self.bitkub.balances())
        self.assertTrue(True)

    def test_place_bid(self):
        # print(self.bitkub.place_bid(sym='THB_BTC'))
        self.assertTrue(True)

    def test_place_ask(self):
        # print(self.bitkub.place_ask(sym='THB_BTC'))
        self.assertTrue(True)

    def test_cancel_order(self):
        # print(self.bitkub.cancel_order(sym='THB_BTC', id=1, sd='buy', hash='123'))
        self.assertTrue(True)

    def test_my_open_orders(self):
        # print(self.bitkub.my_open_orders(sym='THB_BTC'))
        self.assertTrue(True)

    def test_my_open_history(self):
        # print(self.bitkub.my_open_history(sym='THB_BTC'))
        self.assertTrue(True)

    def test_order_info(self):
        # print(self.bitkub.order_info(sym='THB_BTC'))
        self.assertTrue(True)

    def test_crypto_address(self):
        # print(self.bitkub.crypto_address())
        self.assertTrue(True)

    def test_crypto_withdraw(self):
        # print(self.bitkub.crypto_withdraw())
        self.assertTrue(True)

    def test_crypto_deposit_history(self):
        # print(self.bitkub.crypto_deposit_history())
        self.assertTrue(True)

    def test_crypto_withdraw_history(self):
        # print(self.bitkub.crypto_withdraw_history())
        self.assertTrue(True)

    def test_fiat_accounts(self):
        # print(self.bitkub.fiat_accounts())
        self.assertTrue(True)

    def test_fiat_withdraw(self):
        # print(self.bitkub.fiat_withdraw(id='123', amt=1))
        self.assertTrue(True)

    def test_fiat_deposit_history(self):
        # print(self.bitkub.fiat_deposit_history())
        self.assertTrue(True)

    def test_fiat_withdraw_history(self):
        # print(self.bitkub.fiat_withdraw_history())
        self.assertTrue(True)

    def test_market_wstoken(self):
        # print(self.bitkub.market_wstoken())
        self.assertTrue(True)

    def test_user_limits(self):
        # print(self.bitkub.user_limits())
        self.assertTrue(True)

    def test_user_trading_credits(self):
        # print(self.bitkub.user_trading_credits())
        self.assertTrue(True)
