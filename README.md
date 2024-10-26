# Bitkub Python


A Python library for [bitkub.com](https://github.com/bitkub/bitkub-official-api-docs) API

## Releases
  * ```2024-10-26``` version ```2.0.0```
    * support api ```v3```
  * ```2022-01-07``` version ```1.1.0```
    * add [Create buy order test](#createbuyordertest)
    * add [Create sell order test](#createsellordertest)
    * [Viewing tradingview history](#viewingtradingviewhistory) endpoint is now deprecated and will be updated with a new endpoint soon. The old endpoint will always return empty result.
    * include is_maker in [My order history](#myorderhistory)
    * removed address and instead include from_address and to_address in [Crypto deposit history](#cryptodeposithistory)
    * add [Crypto internal withdraw](#cryptinternalowithdraw)
    * include partial_filled and remaining in [Order info](#orderinfo)
  * ```2020-04-02``` version ```1.0.3``` add [generate-address](#cryptogenerateaddress) method

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Creating a Bitkub](#creating)
  - [Set API key & API secret](#api_key)
  - [Viewing status](#viewingstatus)
  - [Viewing servertime](#viewingservertime)
  - [Viewing symbols](#viewingsymbols)
  - [Viewing ticker](#viewingticker)
  - [Viewing trades](#viewingtrades)
  - [Viewing bids](#viewingbids)
  - [Viewing asks](#viewingasks)
  - [Viewing books](#viewingbooks)
  - [Viewing depth](#viewingdepth)
  - [Viewing tradingview history](#viewingtradingviewhistory)
  - [Viewing wallet](#viewingwallet)
  - [Viewing balances](#viewingbalances)
  - [Create buy order](#createbuyorder)
  - [Create sell order](#createsellorder)
  - [Cancel order](#cancelorder)
  - [My open orders](#myopenorders)
  - [My order history](#myorderhistory)
  - [Order info](#orderinfo)
  - [Crypto addresses](#cryptoaddressses)
  - [Crypto withdraw](#cryptowithdraw)
  - [Crypto internal withdraw](#cryptinternalowithdraw)
  - [Crypto deposit history](#cryptodeposithistory)
  - [Crypto withdraw history](#cryptowithdrawhistory)
  - [Crypto generate address](#cryptogenerateaddress)
  - [Fiat accounts](#fiataccounts)
  - [Fiat withdraw](#fiatwithdraw)
  - [Fiat deposit history](#fiatdeposithistory)
  - [Fiat withdraw history](#fiatwithdrawhistory)
  - [Market wstoken](#marketwstoken)
  - [User limits](#userlimits)
  - [User trading credits](#usertradingcredits)


## Installation <a name="installation"></a>

    pip install bitkub

## Usage <a name="usage"></a>

    from bitkub import Bitkub

### Creating a Bitkub Object <a name="creating"></a>

    API_KEY = 'YOUR API KEY'
    API_SECRET = 'YOUR API SECRET'

    # initial obj only non-secure
    bitkub = Bitkub()

    # initial obj non-secure and secure
    bitkub = Bitkub(api_key=API_KEY, api_secret=API_SECRET)

You can find API KEY and API SECRET from [here](https://www.bitkub.com/publicapi).

### Set API key and API secret <a name="api_key"></a>
  If you initial obj with only non-secure. You can set up API key and API secret on below.

    API_KEY = 'YOUR API KEY'
    API_SECRET = 'YOUR API SECRET'

    bitkub = Bitkub()
    bitkub.set_api_key(API_KEY)
    bitkub.set_api_secret(API_SECRET)

### Viewing status <a name="viewingstatus"></a>

Get endpoint status.

#### Function:
    bitkub.status()

#### Response:

    [
      {
        'name': 'Non-secure endpoints',
        'status': 'ok',
        'message': ''
      },
      {
        'name': 'Secure endpoints',
        'status': 'ok',
        'message': ''
      }
    ]

### Viewing servertime <a name="viewingservertime"></a>

Get server timestamp.

#### Function:
    bitkub.servertime()

#### Response:

    1583051817

### Viewing symbols <a name="viewingsymbols"></a>

List all available symbols.

#### Function:
    bitkub.symbols()

#### Response:

    {
      'error': 0,
      'result': [
        {
          'id': 1,
          'info': 'Thai Baht to Bitcoin',
          'symbol': 'THB_BTC'
        },
        {
          'id': 2,
          'info': 'Thai Baht to Ethereum',
          'symbol': 'THB_ETH'
        }
      ]
    }

### Viewing ticker <a name="viewingticker"></a>

Get ticker information.

#### Function:
    bitkub.ticker(sym='THB_BTC')

#### Parameter:

  * ```sym``` **string** The symbol (optional) ```default``` ""

#### Response:

    {
      'THB_BTC': {
        'id': 1,
        'last': 278000,
        'lowestAsk': 278869.41,
        'highestBid': 278000,
        'percentChange': -1.44,
        'baseVolume': 206.01549914,
        'quoteVolume': 57883319.04,
        'isFrozen': 0,
        'high24hr': 284000,
        'low24hr': 277579.62,
        'change': -4075.81,
        'prevClose': 281800,
        'prevOpen': 281800
      }
    }

### Viewing trades <a name="viewingtrades"></a>

List recent trades.

#### Function:
    bitkub.trades(sym="THB_BTC", lmt=2)

#### Parameter:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to Parameter recent trades ```default``` 1

#### Response:

    {
      'error': 0,
      'result': [
        [
          1583246192, // timestamp
          278798.34, // rate
          0.00375672, // amount
          'BUY' // side
        ],
        [
          1583246159,
          278000,
          0.0001042,
          'SELL'
        ]
      ]
    }


### Viewing bids <a name="viewingbids"></a>

List open buy orders.

#### Function:
    bitkub.bids(sym="THB_BTC", lmt=2)

#### Parameter:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to Parameter open buy orders ```default``` 1

#### Response:

    {
      'error': 0,
      'result': [
        [
          4632978, // order id
          1583245687, // timestamp
          73110.59, // volume
          278000, // rate
          0.26298773 // amount
        ],
        [
          4632732,
          1583245871,
          1312.68,
          278000,
          0.00472187
        ]
      ]
    }


### Viewing asks <a name="viewingasks"></a>

List open sell orders.

#### Function:
    bitkub.asks(sym="THB_BTC", lmt=2)
#### Parameter:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to Parameter open sell orders ```default``` 1

#### Response:

    {
      'error': 0,
      'result': [
        [
          4761288, // order id
          1583246870, // timestamp
          163813.12, // volume
          278499.03, // rate
          0.5882 // amount
        ],
        [
          4761287,
          1583246870,
          379232.12,
          278499.03,
          1.3617
        ]
      ]
    }


### Viewing books <a name="viewingbooks"></a>

List all open orders.

#### Function:
    bitkub.books(sym="THB_BTC", lmt=1)
#### Parameter:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of imit to Parameter open orders ```default``` 1

#### Response:

    {
      'error': 0,
      'result': {
        'asks': [
          [
            4761425, // order id
            1583247105, // timestamp
            360885.74, // volume
            278300.17, // rate
            1.29675 // amount
          ]
        ],
        'bids': [
          [
            4633099, // order id
            1583247090, // timestamp
            622146.15, // volume
            277946.2, // rate
            2.23836897 // amount
          ]
        ]
      }
    }



### Viewing tradingview history <a name="viewingtradingviewhistory"></a>

Get historical data for TradingView chart.

#### Function:
    bitkub.tradingview(sym='THB_BTC', int=1, frm='', to='')
#### Parameter:

  * ```sym``` **string** The symbol
  * ```int``` **int** Chart resolution (1, 5, 15, 60, 240, 1D) ```default``` 1
  * ```frm``` **int** Timestamp of the starting time
  * ```to``` **int** Timestamp of the ending time

#### Response:
    
    {
      'c': [
        1685000,
        1680699.95,
        1688998.99,
        1692222.22
      ],
      'h': [
        1685000,
        1685000,
        1689000,
        1692222.22
      ],
      'l': [
        1680053.22,
        1671000,
        1680000,
        1684995.07
      ],
      'o': [
        1682500,
        1685000,
        1680100,
        1684995.07
      ],
      's': "ok",
      't': [
        1633424400,
        1633425300,
        1633426200,
        1633427100
      ],
      'v': [
        4.604352630000001,
        8.530631670000005,
        4.836581560000002,
        2.8510189200000022
      ]
    }

### Viewing depth <a name="viewingdepth"></a>

Get depth information.

#### Function:
    bitkub.depth(sym='THB_BTC', lmt=1)
#### Parameter:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** Depth size  ```default``` 1

#### Response:

    {
      'asks': [
        [
          277946.16,
          1.29675
        ]
      ],
      'bids': [
        [
          277936.27,
          0.94071896
        ]
      ]
    }


### Viewing wallet <a name="viewingwallet"></a>

Get user available balances. ```Required initial secure obj```

#### Function:
    bitkub.wallet()

#### Response:

    {
      'error': 0,
      'result': {
        'THB': 0,
        'BTC': 0,
        'ETH': 0
      }
    }


### Viewing balances <a name="viewingbalances"></a>

Get balances info: this includes both available and reserved balances. ```Required initial secure obj```

#### Function:
    bitkub.balances()

#### Response:

    {
      'error': 0,
      'result': {
        'THB': {
          'available': 0,
          'reserved': 0
        },
        'BTC': {
          'available': 0,
          'reserved': 0
        }
      }
    }


### Create buy order <a name="createbuyorder"></a>

Create a buy order. ```Required initial secure obj```

#### Function:
    bitkub.place_bid(sym='THB_BTC', amt=1, rat=1, typ='limit', client_id='a7sjas7', post_only=false)

#### Parameter:
  * ```sym``` **string** The symbol
  * ```amt``` **float** Amount you want to spend with no trailing zero (e.g 1000.00 is invalid, 1000 is ok) ```default``` 1
  * ```rat``` **float** Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok) ```default``` 1
  * ```typ``` **string** Order type: limit or market ```default``` limit
  * ```client_id``` **string** your id for reference ( not required )
  * ```post_only``` **bool** Postonly flag: ```true``` or ```false``` ( not required )


#### Response:

    {
      'error': 0,
      'result': {
        'id': 1,
        'hash': 'fwQ6dnQWQPs4cbatF5Am2xCDP1J',
        'typ': 'limit',
        'amt': 1,
        'rat': 1,
        'fee': 2.5,
        'cre': 2.5,
        'rec': 0.06666666,
        'ts': 1533834547
      }
    }

### Create sell order <a name="createsellorder"></a>

Create a sell order. ```Required initial secure obj```

#### Function:
    bitkub.place_ask(sym='THB_BTC', amt=1, rat=1, typ='limit', client_id='a7sjas7', post_only=false)

#### Parameter:
  * ```sym``` **string** The symbol
  * ```amt``` **float** Amount you want to spend with no trailing zero (e.g 1000.00 is invalid, 1000 is ok) ```default``` 1
  * ```rat``` **float** Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok) ```default``` 1
  * ```typ``` **string** Order type: limit or market ```default``` limit'
  * ```client_id``` **string** your id for reference ( not required )
  * ```post_only``` **bool** Postonly flag: ```true``` or ```false``` ( not required )


#### Response:

    {
      'error': 0,
      'result': {
        'id': 1,
        'hash': 'fwQ6dnQWQPs4cbatF5Am2xCDP1J',
        'typ': 'limit',
        'amt': 1,
        'rat': 1,
        'fee': 2.5,
        'cre': 2.5,
        'rec': 0.06666666,
        'ts': 1533834547
      }
    }


### Cancel order<a name="cancelorder"></a>

Cancel an open order. ```Required initial secure obj```

#### Function:
    bitkub.cancel_order(sym='THB_BTC', id=1, sd=1, hash='XXXXXX')

#### Parameter:
  * ```sym``` **string** The symbol
  * ```id``` **int** Order id you wish to cancel
  * ```sd``` **string** Order side: buy or sell ```default``` buy
  * ```hash``` **string** Cancel an order with order hash (optional). You don't need to specify sym, id, and sd when you specify order hash.


#### Response:

    {
      'error': 0
    }


### My open orders<a name="myopenorders"></a>

List all open orders of the given symbol. ```Required initial secure obj```

#### Function:
    bitkub.my_open_orders(sym='THB_BTC')

#### Parameter:
  * ```sym``` **string** The symbol


#### Response:

    {
      'error': 0,
      'result': [
        {
          'id': 2,
          'hash': 'fwQ6dnQWQPs4cbatFSJpMCcKTFR',
          'side': 'SELL',
          'type': 'limit',
          'rate': 15000,
          'fee': 35.01,
          'credit': 35.01,
          'amount': 0.93333334,
          'receive': 14000,
          'parent_id': 1,
          'super_id': 1,
          'ts': 1533834844
        }
      ]
    }


### My order history<a name="myorderhistory"></a>

List all orders that have already matched. ```Required initial secure obj```

#### Function:
    bitkub.my_open_history(sym='THB_BTC', p=1, lmt=10)

#### Parameter:
  * ```sym``` **string** The symbol
  * ```p``` **string** Page (optional)
  * ```lmt``` **string** Limit (optional)
  * ```start``` **string** Start timestamp (optional)
  * ```end``` **string** End timestamp (optional)


#### Response:

    {
      'error': 0,
      'result': [
        {
          'txn_id': 'ETHBUY0000000197',
          'order_id': 240,
          'hash': 'fwQ6dnQWQPs4cbaujNyejinS43a',
          'parent_order_id': 0,
          'super_order_id': 0,
          'taken_by_me': true,
          'is_maker': true,
          'side': 'buy',
          'type': 'limit',
          'rate': 13335.57,
          'fee': 0.34,
          'credit': 0.34,
          'amount': 0.00999987,
          'ts': 1531513395
        }

    {
      'error': 0,
      'result': {
          'id': 289,
      ],
      'pagination': {
        'page': 2,
        'last': 3,
        'next': 3,
        'prev': 1
      }
    }


### Order info<a name="orderinfo"></a>

Get information regarding the specified order. ```Required initial secure obj```

#### Function:
    bitkub.order_info(sym='THB_BTC', id=1, sd='buy', hash='XXXXXX')

#### Parameter:
  * ```sym``` **string** The symbol
  * ```id``` **int** Order id
  * ```sd``` **string** Order side: buy or sell ```default```  buy
  * ```hash``` **string** Lookup an order with order hash (optional). You don't need to specify sym, id, and sd when you specify order hash.


#### Response:

    {
      'error': 0,
      'result': {
          'id': 289,
          'first': 289,
          'parent': 0,
          'last': 316,
          'amount': 4000,
          'rate': 291000,
          'fee': 10,
          'credit': 10,
          'filled': 3999.97,
          'total': 4000,
          'status': 'filled',
          'partial_filled': False,
          'remaining': 0,
          'history': [
            {
                'amount': 98.14848,
                'credit': 0.25,
                'fee': 0.25,
                'id': 289,
                'rate': 291000,
                'timestamp': 1525944169
            }
          ]
        }
      }


### Crypto addresses<a name="cryptoaddress"></a>

List all crypto addresses. ```Required initial secure obj```

#### Function:
    bitkub.crypto_address(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error': 0,
      'result': [
        {
           'currency': 'BTC',
           'address': '3BtxdKw6XSbneNvmJTLVHS9XfNYM7VAe8k',
           'tag': 0,
           'time': 1570893867
        }
      ],
      'pagination': {
        'page': 1,
        'last": 1
      }
    }


### Crypto withdraw<a name="cryptowithdraw"></a>

Make a withdrawal to a trusted address. ```Required initial secure obj```

#### Function:
    bitkub.crypto_withdraw(cur='BTC', amt=0.1, adr='4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x', mem='', net='')

#### Parameter:
  * ```cur``` **string** Currency for withdrawal (e.g. BTC, ETH)
  * ```amt``` **float** Amount you want to withdraw
  * ```adr``` **string** Address to which you want to withdraw
  * ```mem``` **string** (Optional) Memo or destination tag to which you want to withdraw
  * ```net``` **string** Cryptocurrency network to withdraw


#### Response:

    {
      'error': 0,
      'result': {
          'txn': 'BTCWD0000012345',
          'adr': '4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x'
          'mem': '',
          'cur': 'BTC',
          'amt': 0.1,
          'fee': 0.0002,
          'ts': 1569999999
      }
    }


### Crypto internal withdraw<a name="cryptointernalwithdraw"></a>

Make a withdrawal to a trusted address. ```Required initial secure obj```

The destination address is not required to be a trusted address. This API is not enabled by default, Only KYB users can request this feature by contacting us via support@bitkub.com

#### Function:
    bitkub.crypto_internal_withdraw(cur='BTC', amt=0.1, adr='4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x', mem='', net='')

#### Parameter:
  * ```cur``` **string** Currency for withdrawal (e.g. BTC, ETH)
  * ```amt``` **float** Amount you want to withdraw
  * ```adr``` **string** Address to which you want to withdraw
  * ```mem``` **string** (Optional) Memo or destination tag to which you want to withdraw
  * ```net``` **string** Cryptocurrency network to withdraw


#### Response:

    {
      'error': 0,
      'result': {
          'txn': 'BTCWD0000012345',
          'adr': '4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x'
          'mem': '',
          'cur': 'BTC',
          'amt': 0.1,
          'fee': 0.0002,
          'ts': 1569999999
      }
    }


### Crypto deposit history<a name="cryptodeposithistory"></a>

List crypto deposit history. ```Required initial secure obj```

#### Function:
    bitkub.crypto_deposit_history(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error': 0,
      'result': [
        {
           'hash': 'XRPWD0000100276',
           'currency': 'XRP',
           'amount': 5.75111474,
           'from_address': 'sender address',
           'to_address': 'receipent address',
           'confirmations': 1,
           'status': 'complete',
           'time': 1570893867
        }
      ],
      'pagination': {
        'page': 1,
        'last': 1
      }
    }


### Crypto withdraw history<a name="cryptowithdrawhistory"></a>
:
List crypto withdrawal history. ```Required initial secure obj```

#### Function:
    bitkub.crypto_withdraw_history(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error': 0,
      'result': [
        {
          'txn_id': 'XRPWD0000100276',
          'hash': 'send_internal',
          'currency': 'XRP',
          'amount': '5.75111474',
          'fee': 0.01,
          'address': 'rpXTzCuXtjiPDFysxq8uNmtZBe9Xo97JbW',
          'status': 'complete',
          'time': 1570893493
        }
      ],
      'pagination': {
        'page': 1,
        'last': 1
      }
    }


### Crypto generate address<a name="cryptogenerateaddress"></a>
Generate a new crypto address (will replace existing address; previous address can still be used to received funds)
List all approved bank accounts. ```Required initial secure obj```

#### Function:
    bitkub.crypto_generate_address(sym='THB_BTC')

#### Parameter:
  * ```sym``` **string** The symbol


#### Response:

    {
      'error': 0,
      'result': [
        {
           'currency': 'BTC',
           'address': '0x520165471daa570ab632dd504c6af257bd36edfb',
           'memo': ''
        }
      ]
    }



### Fiat accounts<a name="fiataccounts"></a>

List all approved bank accounts. ```Required initial secure obj```

#### Function:
    bitkub.fiat_accounts(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error': 0,
      'result': [
        {
          'id': '7262109099',
          'bank': 'Kasikorn Bank',
          'name': 'Somsak',
          'time': 1570893867
        }
      ],
      'pagination': {
        'page': 1,
        'last': 1
      }
    }


### Fiat withdraw<a name="fiatwithdraw"></a>

Make a withdrawal to an approved bank account. ```Required initial secure obj```

#### Function:
    bitkub.fiat_withdraw(id=1, amt=1)

#### Parameter:
  * ```id``` **string** Bank account id
  * ```amt``` **float** Amount you want to withdraw


#### Response:

    {
      'error': 0,
      'result': {
        'txn': 'THBWD0000012345',
        'acc': '7262109099',
        'cur': 'THB',
        'amt': 21,
        'fee': 20,
        'rec': 1,
        'ts': 1569999999
      }
    }


### Fiat deposit history<a name="fiatdeposithistory"></a>

List fiat deposit history. ```Required initial secure obj```

#### Function:
    bitkub.fiat_deposit_history(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error':0,
      'result':[
        {
           'txn_id': 'THBDP0000012345',
           'currency': 'THB',
           'amount': 5000.55,
           'status': 'complete',
           'time': 1570893867
        }
      ],
      'pagination':{
        'page': 1,
        'last': 1
      }
    }


### Fiat withdraw history<a name="fiatwithdrawhistory"></a>

List fiat withdrawal history. ```Required initial secure obj```

#### Function:
    bitkub.fiat_withdraw_history(p=1, lmt=1)

#### Parameter:
  * ```p``` **int** Page (optional) ```default``` 1
  * ```lmt``` **int** Limit (optional) ```default``` 10


#### Response:

    {
      'error': 0,
      'result': [
        {
           'txn_id': 'THBDP0000012345',
           'currency': 'THB',
           'amount': 5000.55,
           'fee': 20,
           'status': 'complete',
           'time': 1570893867
        }
      ],
      'pagination':{
        'page': 1,
        'last': 1
      }
    }


### Market wstoken<a name="marketwstoken"></a>

Get the token for websocket authentication. ```Required initial secure obj```

#### Function:
    bitkub.market_wstoken()

#### Response:

    {
      'error': 0,
      'result': 'sdCBCTwaS2Z1IBB6uTCefIbVN6dQVz9dkDeU96IoFJp14GGhlw9hoUDNe1KSYC23dXBPIqyX2QjVEOFHITxgPMvo8kdVaTkiZBA8KgvVTSMsq6JjjlyERDVZn3tt4PEp'
    }

### User limits<a name="userlimits"></a>

Check deposit/withdraw limitations and usage. ```Required initial secure obj```

#### Function:
    bitkub.user_limits()

#### Response:

    {
      'error': 0,
      'result': {
        'limits': {
          'crypto': {
            'deposit': 0,
            'withdraw': 0
          },
          'fiat': {
            'deposit': 0,
            'withdraw': 0
          }
        },
        'usage': {
          'crypto': {
            'deposit': 0,
            'withdraw': 0,
            'deposit_percentage': 0,
            'withdraw_percentage': 0,
            'deposit_thb_equivalent': 0,
            'withdraw_thb_equivalent': 0
          },
          'fiat': {
            'deposit': 0,
            'withdraw': 0,
            'deposit_percentage': 0,
            'withdraw_percentage': 0
          }
        },
        'rate': 177100.32
      }
    }


### User trading-credit<a name="usertradingcredits"></a>

Check trading credit balance. ```Required initial secure obj```

#### Function:
    bitkub.user_trading_credits()

#### Response:

    {
      'error': 0,
      'result': 0
    }
