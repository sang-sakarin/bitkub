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
        # print(self.bitkub.ticker())
        self.assertTrue(True)

    def test_trades(self):
        # print(self.bitkub.trades("THB_BTC", 10))
        self.assertTrue(True)

    def test_bids(self):
        # print(self.bitkub.bids("THB_BTC", 10))
        self.assertTrue(True)

    def test_asks(self):
        # print(self.bitkub.asks("THB_BTC", 10))
        self.assertTrue(True)

    def test_books(self):
        print(self.bitkub.books("THB_BTC", 10))
        self.assertTrue(True)
