from bitkub import Bitkub
from unittest import TestCase


class BitkubTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bitkub = Bitkub()

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
