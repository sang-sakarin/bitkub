# Bitkub Python



A Python library for [bitkub.com](https://github.com/bitkub/bitkub-official-api-docs) API

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Creating a Bitkub](#creating)
  - [Viewing status](#viewingstatus)
  - [Viewing servertime](#viewingservertime)
  - [Viewing symbols](#viewingsymbols)
  - [Viewing ticker](#viewingticker)
  - [Viewing trades](#viewingtrades)
  - [Viewing bids](#viewingbids)
  - [Viewing asks](#viewingasks)
  - [Viewing books](#viewingbooks)
  - [Viewing depth](#viewingdepth)
  - Coming Soon ...

## Installation <a name="installation"></a>

    pip install bitkub

## Usage <a name="usage"></a>

    from bitkub import Bitkub

### Creating a Bitkub Object <a name="creating"></a>

    bitkub = Bitkub()

### Viewing status <a name="viewingstatus"></a>

#### Description:
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

#### Description:
Get server timestamp.

#### Function:
    bitkub.servertime()

#### Response:

    1583051817

### Viewing symbols <a name="viewingsymbols"></a>

#### Description:
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

#### Description:
Get ticker information.

#### Function:
    bitkub.ticker(sym='THB_BTC')

#### Query:

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

#### Description:
List recent trades.

#### Function:
    bitkub.trades(sym="THB_BTC", lmt=2)

#### Query:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to query recent trades ```default``` 1

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

#### Description:
List open buy orders.

#### Function:
    bitkub.bids(sym="THB_BTC", lmt=2)

#### Query:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to query open buy orders ```default``` 1

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

#### Description:
List open sell orders.

#### Function:
    bitkub.asks(sym="THB_BTC", lmt=2)
#### Query:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of limit to query open sell orders ```default``` 1

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

#### Description:
List all open orders.

#### Function:
    bitkub.books(sym="THB_BTC", lmt=1)
#### Query:

  * ```sym``` **string** The symbol
  * ```lmt``` **int** No. of imit to query open orders ```default``` 1

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


### Viewing depth <a name="viewingdepth"></a>

#### Description:
Get depth information.

#### Function:
    bitkub.depth(sym='THB_BTC', lmt=1)
#### Query:

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
