# Bitkub Python


A Python library for [bitkub.com](https://github.com/bitkub/bitkub-official-api-docs) API

# Releases
* 2022–11-03 Added trading apis prefix ```api/market/v2``` namely [place-bid-v2(```beta```)](#post-apimarketV2place-bidbeta), [place-ask-v2(```beta```)](#post-apimarketV2place-askbeta), [cancel-order-v2(```beta```)](#post-apimarketV2cancel-orderbeta). We recommend to use these apis because their performance are improved. These API are considered as ```beta```. If you encounter any issue, please kindly contact Bitkub customer support.
* 2022-08-16 Added new error code. For `suspended purchasing` and `selling`.
* 2022-08-15 Changed the input `net` (network) of the API [POST /api/crypto/withdraw](#post-apicryptowithdraw) to mandatory. Please find available `net` from https://www.bitkub.com/fee/cryptocurrency
* 2022-07-05 Increased APIs rate limit. For APIs [GET /api/market/depth](#get-apimarketdepth), [POST /api/market/place-bid](#post-apimarketplace-bid), [POST /api/market/place-ask](#post-apimarketplace-ask) and [POST /api/market/cancel-order](#post-apimarketcancel-order)
* 2022-06-21 Added field ```net``` for the APIs [POST /api/crypto/withdraw](#post-apicryptowithdraw)
* 2022-06-02 Added rate limits table
* 2021-10-05 Updated usage of [tradingview](#get-tradingviewhistory) endpoint
* 2021-09-03 Include ```partial_filled``` and ```remaining``` in [POST /api/market/order-info](#post-apimarketorder-info)
* 2021-08-31 Added [POST /api/crypto/internal-withdraw](#post-apicryptointernal-withdraw)
* 2021-07-03 Removed ~~```address```~~ and instead include ```from_address``` and ```to_address``` in [POST /api/crypto/deposit-history](#post-apicryptodeposit-history)
* 2021-05-28 Include ```is_maker``` in [POST /api/market/my-order-history](#post-apimarketmy-order-history)
* 2021-01-16 [tradingview](#get-tradingviewhistory) endpoint is now deprecated and will be updated with a new endpoint soon. The old endpoint will always return empty result.
* 2020-06-26 Added [place-bid/test](#post-apimarketplace-bidtest) and [place-ask/test](#post-apimarketplace-asktest)
* 2020-04-01 Added [generate-address](#post-apicryptogenerate-address)
* 2020-03-12 Added query by start and end timestamps to [my-order-history](#post-apimarketmy-order-history)
* 2020-03-03 Added order hash to: [my-order-history](#post-apimarketmy-order-history), [my-open-orders](#post-apimarketmy-open-orders), [place-bid](#post-apimarketplace-bid), [place-ask](#post-apimarketplace-ask), [place-ask-by-fiat](#post-apimarketplace-ask-by-fiat), [cancel-order](#post-apimarketcancel-order), and [order-info](#post-apimarketorder-info)
* 2020-01-21 Depth API
* 2020-01-14 Trading credit balance API
* 2020-01-07 Place ask by fiat API
* 2020-01-06 Status API
* 2019-12-03 Limit API
* 2019-11-26 Websocket token API
* 2019-11-12 Fiat withdrawal and fiat deposit/withdrawal history
* 2019-10-28 Crypto withdrawal and crypto deposit/withdrawal history
* 2019-05-25 Ticker API now allows symbol query
* 2019-03-23 Added order info API
* 2018-12-16 Updated documentation
* 2018-08-09 V1 Release

# Table of contents
* [Base URL](#base-url)
* [Endpoint types](#endpoint-types)
* [Constructing the request](#constructing-the-request)
* [API documentation](#api-documentation)
* [Error codes](#error-codes)
* [Rate limits](#rate-limits)

# Base URL
* The base URL is: https://api.bitkub.com

# Endpoint types
### Non-secure endpoints
All non-secure endpoints do not need authentication and use the method GET.
* [GET /api/status](#get-apistatus)
* [GET /api/servertime](#get-apiservertime)
* [GET /api/market/symbols](#get-apimarketsymbols)
* [GET /api/market/ticker](#get-apimarketticker)
* [GET /api/market/trades](#get-apimarkettrades)
* [GET /api/market/bids](#get-apimarketbids)
* [GET /api/market/asks](#get-apimarketasks)
* [GET /api/market/books](#get-apimarketbooks)
* [GET /api/market/depth](#get-apimarketdepth)
* [GET /tradingview/history](#get-tradingviewhistory)

### Secure endpoints
All secure endpoints require [authentication](#constructing-the-request) and use the method POST.
* [POST /api/market/wallet](#post-apimarketwallet)
* [POST /api/market/balances](#post-apimarketbalances)
* [POST /api/market/place-bid](#post-apimarketplace-bid)
* [POST /api/market/place-ask](#post-apimarketplace-ask)
* [POST /api/market/place-bid/test](#post-apimarketplace-bidtest)
* [POST /api/market/place-ask/test](#post-apimarketplace-asktest)
* [POST /api/market/place-ask-by-fiat](#post-apimarketplace-ask-by-fiat)
* [POST /api/market/cancel-order](#post-apimarketcancel-order)
* [POST /api/market/my-open-orders](#post-apimarketmy-open-orders)
* [POST /api/market/my-order-history](#post-apimarketmy-order-history)
* [POST /api/market/order-info](#post-apimarketorder-info)
* [POST /api/crypto/addresses](#post-apicryptoaddresses)
* [POST /api/crypto/withdraw](#post-apicryptowithdraw)
* [POST /api/crypto/internal-withdraw](#post-apicryptointernal-withdraw) 
* [POST /api/crypto/deposit-history](#post-apicryptodeposit-history)
* [POST /api/crypto/withdraw-history](#post-apicryptowithdraw-history)
* [POST /api/crypto/generate-address](#post-apicryptogenerate-address)
* [POST /api/fiat/accounts](#post-apifiataccounts)
* [POST /api/fiat/withdraw](#post-apifiatwithdraw)
* [POST /api/fiat/deposit-history](#post-apifiatdeposit-history)
* [POST /api/fiat/withdraw-history](#post-apifiatwithdraw-history)
* [POST /api/market/wstoken](#post-apimarketwstoken)
* [POST /api/user/limits](#post-apiuserlimits)
* [POST /api/user/trading-credits](#post-apiusertrading-credits)
* [POST /api/market/v2/place-bid(```beta```)](#post-apimarketV2place-bidbeta)
* [POST /api/market/v2/place-ask(```beta```)](#post-apimarketV2place-askbeta)
* [POST /api/market/v2/cancel-order(```beta```)](#post-apimarketV2cancel-orderbeta)

# Constructing the request
### GET/POST request
* GET requests require parameters as **query string** in the URL (e.g. ?sym=THB_BTC&lmt=10). 
* POST requests require JSON payload (application/json).

### Request headers (POST)
Authentication requires API KEY and API SECRET. Every request to the server must contain the following in the request header:
* Accept: application/json
* Content-type: application/json
* X-BTK-APIKEY: {YOUR API KEY}

### Payload (POST)
The payload is always JSON. **Always include timestamp in the payload; use `ts` as the key name for timestamp**.

### Signature (POST)
Generate the signature from the JSON payload using HMAC SHA-256. Use the API SECRET as the secret key for generating the HMAC variant of JSON payload. Signature is in **hex** format.

#### Example payload:
```javascript
{"sym":"THB_BTC","amt":0.1,"rat":10000,"typ":"limit","ts":1529490685}
```

#### Example payload with signature:
```javascript
{"sym":"THB_BTC","amt":0.1,"rat":10000,"typ":"limit","ts":1529490685,"sig":"d0c66fabb816c46953270e4a442836ca449711e143c8658dd03103c90b2d0fb7"}
```

#### Example cURL:
```javascript
curl -X POST \
  https://api.bitkub.com/api/market/place-ask \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H 'x-btk-apikey: 6da634977495306b2206eee7772532cb' \
  -d '{"sym":"THB_BTC","amt":0.1,"rat":10000,"typ":"limit","ts":1529490685,"sig":"d0c66fabb816c46953270e4a442836ca449711e143c8658dd03103c90b2d0fb7"}'
```

### Nonce
You can secure your request even further by including `nonce` in the request payload. Nonce is a numeric value which is incremental in each request (nonce value has to be higher in each new request). Use `non` as the key name for nonce.

#### Example payload (with nonce):
```javascript
{"sym":"THB_BTC","amt":0.1,"rat":10000,"typ":"limit","ts":1529490685,"non":1}
```

# API documentation
Refer to the following for description of each endpoint

### GET /api/status

#### Description:
Get endpoint status. When status is not `ok`, it is highly recommended to wait until the status changes back to `ok`.

#### Query:
-

#### Response:
```javascript
[
  {
    "name": "Non-secure endpoints",
    "status": "ok",
    "message": ""
  },
  {
    "name": "Secure endpoints",
    "status": "ok",
    "message": ""
  }
]
```

### GET /api/servertime

#### Description:
Get server timestamp.

#### Query:
-

#### Response:
```javascript
1529999999
```

### GET /api/market/symbols

#### Description:
List all available symbols.

#### Query:
-

#### Response:
```javascript
{
  "error": 0,
  "result": [
    {
      "id": 1,
      "symbol": "THB_BTC",
      "info": "Thai Baht to Bitcoin"
    },
    {
      "id": 2,
      "symbol": "THB_ETH",
      "info": "Thai Baht to Ethereum"
    }
  ]
}
```

### GET /api/market/ticker

#### Description:
Get ticker information.

#### Query:
* `sym` **string** The symbol (optional)

#### Response:
```javascript
{
  "THB_BTC": {
    "id": 1,
    "last": 216415.00,
    "lowestAsk": 216678.00,
    "highestBid": 215000.00,
    "percentChange": 1.91,
    "baseVolume": 71.02603946,
    "quoteVolume": 15302897.99,
    "isFrozen": 0,
    "high24hr": 221396.00,
    "low24hr": 206414.00
  },
  "THB_ETH": {
    "id": 2,
    "last": 11878.00,
    "lowestAsk": 12077.00,
    "highestBid": 11893.00,
    "percentChange": -0.49,
    "baseVolume": 455.17839270,
    "quoteVolume": 5505664.42,
    "isFrozen": 0,
    "high24hr": 12396.00,
    "low24hr": 11645.00
  }
}
```

### GET /api/market/trades

#### Description:
List recent trades.

#### Query:
* `sym`		**string** The symbol
* `lmt`		**int** No. of limit to query recent trades

#### Response:
```javascript
{
  "error": 0,
  "result": [
    [
      1529516287, // timestamp
      10000.00, // rate
      0.09975000, // amount
      "BUY" // side
    ]
  ]
}
```

### GET /api/market/bids

#### Description:
List open buy orders.

#### Query:
* `sym` **string** The symbol
* `lmt` **int** No. of limit to query open buy orders

#### Response:
```javascript
{
  "error": 0,
  "result": [
    [
      1, // order id
      1529453033, // timestamp
      997.50, // volume
      10000.00, // rate
      0.09975000 // amount
    ]
  ]
}

```

### GET /api/market/asks

#### Description:
List open sell orders.

#### Query:
* `sym` **string** The symbol
* `lmt` **int** No. of limit to query open sell orders

#### Response:
```javascript
{
  "error": 0,
  "result": [
    [
      680, // order id
      1529491094, // timestamp
      997.50, // volume
      10000.00, // rate
      0.09975000 // amount
    ]
  ]
}
```

### GET /api/market/books

#### Description:
List all open orders.

#### Query:
* `sym` **string** The symbol
* `lmt` **int** No. of limit to query open orders

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "bids": [
      [
        1, // order id
        1529453033, // timestamp
        997.50, // volume
        10000.00, // rate
        0.09975000 // amount
      ]
    ],
    "asks": [
      [
        680, // order id
        1529491094, // timestamp
        997.50, // volume
        10000.00, // rate
        0.09975000 // amount
      ]
    ]
  }
}
```

### GET /tradingview/history
#### Description:
Get historical data for TradingView chart.

#### Query:
* `symbol`		**string**		The symbol (e.g. BTC_THB)
* `resolution`		**string**		Chart resolution (1, 5, 15, 60, 240, 1D)
* `from`		**int**		Timestamp of the starting time (e.g. 1633424427)
* `to`		**int**		Timestamp of the ending time (e.g. 1633427427)

#### Response:
```javascript
{
  "c": [
    1685000,
    1680699.95,
    1688998.99,
    1692222.22
  ],
  "h": [
    1685000,
    1685000,
    1689000,
    1692222.22
  ],
  "l": [
    1680053.22,
    1671000,
    1680000,
    1684995.07
  ],
  "o": [
    1682500,
    1685000,
    1680100,
    1684995.07
  ],
  "s": "ok",
  "t": [
    1633424400,
    1633425300,
    1633426200,
    1633427100
  ],
  "v": [
    4.604352630000001,
    8.530631670000005,
    4.836581560000002,
    2.8510189200000022
  ]
}
```

### GET /api/market/depth

#### Description:
Get depth information.

#### Query:
* `sym` **string** The symbol
* `lmt` **int** Depth size

#### Response:
```javascript
{
  "asks": [
    [
      262600,
      0.61905798
    ],
    [
      263000,
      0.00210796
    ],
    [
      263200,
      0.89555545
    ],
    [
      263422.5,
      0.03796183
    ],
    [
      263499,
      0.4123439
    ]
  ],
  "bids": [
    [
      262510,
      0.38038703
    ],
    [
      262100.01,
      1.22519999
    ],
    [
      262100,
      0.00381533
    ],
    [
      262024.88,
      0.00352718
    ],
    [
      262001,
      0.09999961
    ]
  ]
}
```

### POST /api/market/wallet

#### Description:
Get user available balances (for both available and reserved balances please use [POST /api/market/balances](#post-apimarketbalances)).

#### Query:
-

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "THB": 188379.27,
    "BTC": 8.90397323,
    "ETH": 10.1
  }
}
```

### POST /api/market/balances

#### Description:
Get balances info: this includes both available and reserved balances.

#### Query:
-

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "THB":  {
      "available": 188379.27,
      "reserved": 0
    },
    "BTC": {
      "available": 8.90397323,
      "reserved": 0
    },
    "ETH": {
      "available": 10.1,
      "reserved": 0
    }
  }
}
```

### POST /api/market/place-bid

#### Description:
Create a buy order.

#### Query:
* `sym`		**string**		The symbol
* `amt`		**float**		Amount you want to spend with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `rat`		**float**		Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`		**string**		Order type: limit or market (for market order, please specify rat as 0)
* `client_id` **string**		your id for reference ( not required )

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 1, // order id
    "hash": "fwQ6dnQWQPs4cbatF5Am2xCDP1J", // order hash
    "typ": "limit", // order type
    "amt": 1000, // spending amount
    "rat": 15000, // rate
    "fee": 2.5, // fee
    "cre": 2.5, // fee credit used
    "rec": 0.06666666, // amount to receive
    "ts": 1533834547 // timestamp
  }
}
```

### POST /api/market/place-bid/test

#### Description:
Test creating a buy order (no balance is deducted).

#### Query:
* `sym`		**string**		The symbol
* `amt`		**float**		Amount you want to spend with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `rat`		**float**		Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`		**string**		Order type: limit or market
* `client_id`		**string**		your id for reference ( not required )

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 0, // order id
    "hash": "test", // test hash
    "typ": "limit", // order type
    "amt": 1000, // spending amount
    "rat": 15000, // rate
    "fee": 2.5, // fee
    "cre": 2.5, // fee credit used
    "rec": 0.06666666, // amount to receive
    "ts": 1533834547 // timestamp
  }
}
```

### POST /api/market/place-ask

#### Description:
Create a sell order.

#### Query:
* `sym`		**string**		The symbol
* `amt`		**float**		Amount you want to sell with no trailing zero (e.g 0.10000000 is invalid, 0.1 is ok)
* `rat`		**float**		Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`		**string**		Order type: limit or market (for market order, please specify rat as 0)
* `client_id`		**string**		your id for reference ( not required )


#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 1, // order id
    "hash": "fwQ6dnQWQPs4cbatFGc9LPnpqyu", // order hash
    "typ": "limit", // order type
    "amt": 1.00000000, // selling amount
    "rat": 15000, // rate
    "fee": 37.5, // fee
    "cre": 37.5, // fee credit used
    "rec": 15000, // amount to receive
    "ts": 1533834844 // timestamp
  }
}
```

### POST /api/market/place-ask/test

#### Description:
Test creating a sell order (no balance is deducted).

#### Query:
* `sym`		**string**		The symbol
* `amt`		**float**		Amount you want to sell with no trailing zero (e.g 0.10000000 is invalid, 0.1 is ok)
* `rat`		**float**		Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`		**string**		Order type: limit or market
* `client_id`		**string**		your id for reference ( not required )

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 0, // order id
    "hash": "test", // test hash
    "typ": "limit", // order type
    "amt": 1.00000000, // selling amount
    "rat": 15000, // rate
    "fee": 37.5, // fee
    "cre": 37.5, // fee credit used
    "rec": 15000, // amount to receive
    "ts": 1533834844 // timestamp
  }
}
```

### POST /api/market/place-ask-by-fiat

#### Description:
Create a sell order by specifying the fiat amount you want to receive (selling amount of cryptocurrency is automatically calculated). If order type is `market`, currrent highest bid will be used as rate.

#### Query:
* `sym`		**string**		The symbol
* `amt`		**float**		Fiat amount you want to receive with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `rat`		**float**		Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`		**string**		Order type: limit or market

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 1, // order id
    "hash": "fwQ6dnQWQPs4cbatFGc9LPnpqyu", // order hash
    "typ": "limit", // order type
    "amt": 0.0000422, // selling amount resulted from calculation
    "rat": 236999, // rate
    "fee": 0.03, // fee
    "cre": 0.03, // fee credit used
    "rec": 10, // fiat amount to receive
    "ts": 1578390814 // timestamp
  }
}
```

### POST /api/market/cancel-order

### Description:
Cancel an open order.

### Query:
* `sym`		**string**		The symbol
* `id`		**int**		Order id you wish to cancel
* `sd`		**string**		Order side: buy or sell
* `hash`	**string**		Cancel an order with order hash (optional). You don't need to specify sym, id, and sd when you specify order hash.

### Response:
```javascript
{
  "error": 0
}
```

### POST /api/market/my-open-orders

### Description:
List all open orders of the given symbol.

### Query:
* `sym`		**string**		The symbol

### Response:
```javascript
{
  "error": 0,
  "result": [
    {
      "id": 2, // order id
      "hash": "fwQ6dnQWQPs4cbatFSJpMCcKTFR", // order hash
      "side": "SELL", // order side
      "type": "limit", // order type
      "rate": 15000, // rate
      "fee": 35.01, // fee
      "credit": 35.01, // credit used
      "amount": 0.93333334, // amount
      "receive": 14000, // amount to receive
      "parent_id": 1, // parent order id
      "super_id": 1, // super parent order id
      "ts": 1533834844 // timestamp
    }
  ]
}
```

### POST /api/market/my-order-history

### Description:
List all orders that have already matched.

### Query:
* `sym` **string** The symbol
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)
* `start` **int** Start timestamp (optional)
* `end` **int** End timestamp (optional)

### Response:
```javascript
{
  "error": 0,
  "result": [
    {
      "txn_id": "ETHBUY0000000197",
      "order_id": 240,
      "hash": "fwQ6dnQWQPs4cbaujNyejinS43a", // order hash
      "parent_order_id": 0,
      "super_order_id": 0,
      "taken_by_me": false,
      "is_maker": true,
      "side": "buy",
      "type": "limit",
      "rate": "13335.57",
      "fee": "0.34",
      "credit": "0.34",
      "amount": "0.00999987",
      "ts": 1531513395
    }
  ],
  "pagination": {
      "page": 2,
      "last": 3,
      "next": 3,
      "prev": 1
  }
}
```

### POST /api/market/order-info

### Description:
Get information regarding the specified order.

### Query:
* `sym`		**string**		The symbol
* `id`		**int**		Order id
* `sd`		**string**		Order side: buy or sell
* `hash`	**string**		Lookup an order with order hash (optional). You don't need to specify sym, id, and sd when you specify order hash.

### Response:
```javascript
{
    "error": 0,
    "result": {
        "id": 289, // order id
        "first": 289, // first order id
        "parent": 0, // parent order id
        "last": 316, // last order id
        "amount": 4000, // order amount
        "rate": 291000, // order rate
        "fee": 10, // order fee
        "credit": 10, // order fee credit used
        "filled": 3999.97, // filled amount
        "total": 4000, // total amount
        "status": "filled", // order status: filled, unfilled
        "partial_filled": false, // true when order has been partially filled, false when not filled or fully filled
        "remaining": 0, // remaining amount to be executed
        "history": [
            {
                "amount": 98.14848,
                "credit": 0.25,
                "fee": 0.25,
                "id": 289,
                "rate": 291000,
                "timestamp": 1525944169
            },
            {
                "amount": 87.3,
                "credit": 0.22,
                "fee": 0.22,
                "id": 290,
                "rate": 291000,
                "timestamp": 1525947677
            },
            {
                "amount": 11.64,
                "credit": 0.03,
                "fee": 0.03,
                "id": 301,
                "rate": 291000,
                "timestamp": 1525947712
            },
            {
                "amount": 116.4,
                "credit": 0.3,
                "fee": 0.3,
                "id": 302,
                "rate": 291000,
                "timestamp": 1525947746
            },
            {
                "amount": 10.185,
                "credit": 0.03,
                "fee": 0.03,
                "id": 303,
                "rate": 291000,
                "timestamp": 1525948237
            },
            {
                "amount": 10.185,
                "credit": 0.03,
                "fee": 0.03,
                "id": 315,
                "rate": 291000,
                "timestamp": 1525948253
            },
            {
                "amount": 3666.13731,
                "credit": 9.17,
                "fee": 9.17,
                "id": 316,
                "rate": 291000,
                "timestamp": 1525977397
            }
        ]
    }
}
```

### POST /api/crypto/addresses

### Description:
List all crypto addresses.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error":0,
   "result": [
      {
         "currency": "BTC",
         "address": "3BtxdKw6XSbneNvmJTLVHS9XfNYM7VAe8k",
         "tag": 0,
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/crypto/withdraw

### Description:
Make a withdrawal to a **trusted** address.

### Body:
* `cur`		**string**		Currency for withdrawal (e.g. BTC, ETH)
* `amt`		**float**		Amount you want to withdraw
* `adr`		**string**		Address to which you want to withdraw
* `mem`		**string**		(Optional) Memo or destination tag to which you want to withdraw
* `net` **string** Cryptocurrency network to withdraw\
No default value of this field. Please find the available network from the link as follows. https://www.bitkub.com/fee/cryptocurrency

For example `ETH` refers to `ERC-20`.\
For request on `ERC-20`, please assign the `net` value as `ETH`.\
For request on `BEP-20`, please assign the `net` value as `BSC`.\
For request on `KAP-20`, please assign the `net` value as `BKC`.


### Response:
```javascript
{
    "error": 0,
    "result": {
        "txn": "BTCWD0000012345", // local transaction id
        "adr": "4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x", // address
        "mem": "", // memo
        "cur": "BTC", // currency
        "amt": 0.1, // withdraw amount
        "fee": 0.0002, // withdraw fee
        "ts": 1569999999 // timestamp
    }
}
```

### POST /api/crypto/internal-withdraw

### Description:
Make a withdraw to an internal address. The destination address is not required to be a trusted address.
**This API is not enabled by default**, Only KYB users can request this feature by contacting us via **support@bitkub.com**

### Query:
* `cur`		**string**		Currency for withdrawal (e.g. BTC, ETH)
* `amt`		**float**		Amount you want to withdraw
* `adr`		**string**		Address to which you want to withdraw
* `mem`		**string**		(Optional) Memo or destination tag to which you want to withdraw

### Response:
```javascript
{
    "error": 0,
    "result": {
        "txn": "BTCWD0000012345", // local transaction id
        "adr": "4asyjKw6XScneNvhJTLVHS9XfNYM7VBf8x", // address
        "mem": "", // memo
        "cur": "BTC", // currency
        "amt": 0.1, // withdraw amount
        "fee": 0.0002, // withdraw fee
        "ts": 1569999999 // timestamp
    }
}
```


### POST /api/crypto/deposit-history

### Description:
List crypto deposit history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "hash": "XRPWD0000100276",
         "currency": "XRP",
         "amount": 5.75111474,
         "from_address": "sender address",
         "to_address": "recipient address",
         "confirmations": 1,
         "status": "complete",
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/crypto/withdraw-history

### Description:
List crypto withdrawal history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "txn_id": "XRPWD0000100276",
         "hash": "send_internal",
         "currency": "XRP",
         "amount": "5.75111474",
         "fee": 0.01,
         "address": "rpXTzCuXtjiPDFysxq8uNmtZBe9Xo97JbW",
         "status": "complete",
         "time": 1570893493
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/crypto/generate-address

### Description:
Generate a new crypto address (will replace existing address; previous address can still be used to received funds)

### Query (URL):
* `sym` **string** Symbol (e.g. THB_BTC, THB_ETH, etc.)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "currency": "ETH",
         "address": "0x520165471daa570ab632dd504c6af257bd36edfb",
         "memo": ""
      }
   ]
}
```

### POST /api/fiat/accounts

### Description:
List all approved bank accounts.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "id": "7262109099",
         "bank": "Kasikorn Bank",
         "name": "Somsak",
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/fiat/withdraw

### Description:
Make a withdrawal to an **approved** bank account.

### Query:
* `id`		**string**	Bank account id
* `amt`		**float**		Amount you want to withdraw

### Response:
```javascript
{
    "error": 0,
    "result": {
        "txn": "THBWD0000012345", // local transaction id
        "acc": "7262109099", // bank account id
        "cur": "THB", // currency
        "amt": 21, // withdraw amount
        "fee": 20, // withdraw fee
        "rec": 1, // amount to receive
        "ts": 1569999999 // timestamp
    }
}
```

### POST /api/fiat/deposit-history

### Description:
List fiat deposit history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "txn_id": "THBDP0000012345",
         "currency": "THB",
         "amount": 5000.55,
         "status": "complete",
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/fiat/withdraw-history

### Description:
List fiat withdrawal history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error":0,
   "result": [
      {
         "txn_id": "THBWD0000012345",
         "currency": "THB",
         "amount": "21",
         "fee": 20,
         "status": "complete",
         "time": 1570893493
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/market/wstoken

### Description:
Get the token for websocket authentication.

### Query (URL):
-

### Response:
```javascript
{
   "error": 0,
   "result": "BYGoc1Pt81s1ouhZD095UtMdwWU2ZU0tVPYZSZ22WPU8GcMC9jOldV3e9aBJoDWLsfqxWH8jkZYI9ID4EZeeueEFNDL1OznPcS0z1Da19sSF0MlBbqpgT3TQpyp2oea9"
}
```

### POST /api/user/limits

### Description:
Check deposit/withdraw limitations and usage.

### Query (URL):
-

### Response:
```javascript
{
   "error": 0,
   "result": { 
       "limits": { // limitations by kyc level
          "crypto": { 
             "deposit": 0.88971929, // BTC value equivalent
             "withdraw": 0.88971929 // BTC value equivalent
          },
          "fiat": { 
             "deposit": 200000, // THB value equivalent
             "withdraw": 200000 // THB value equivalent
          }
       },
       "usage": { // today's usage
          "crypto": { 
             "deposit": 0, // BTC value equivalent
             "withdraw": 0, // BTC value equivalent
             "deposit_percentage": 0,
             "withdraw_percentage": 0,
             "deposit_thb_equivalent": 0, // THB value equivalent
             "withdraw_thb_equivalent": 0 // THB value equivalent
          },
          "fiat": { 
             "deposit": 0, // THB value equivalent
             "withdraw": 0, // THB value equivalent
             "deposit_percentage": 0,
             "withdraw_percentage": 0
          }
       },
       "rate": 224790 // current THB rate used to calculate
    }
}
```


### POST /api/user/trading-credits

### Description:
Check trading credit balance.

### Query (URL):
-

### Response:
```javascript
{
   "error": 0,
   "result": 1000
}
```

### POST /api/market/v2/place-bid(```beta```)

#### Description:
Create a buy order.

#### Body:
* `sym`   **string**    The symbol
* `amt`   **float**   Amount you want to spend with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `rat`   **float**   Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`   **string**    Order type: limit or market (for market order, please specify rat as 0)
* `client_id` **string**    your id for reference ( not required )

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 1, // order id
    "hash": "fwQ6dnQWQPs4cbatF5Am2xCDP1J", // order hash
    "typ": "limit", // order type
    "amt": 1000, // spending amount
    "rat": 15000, // rate
    "fee": 2.5, // fee
    "cre": 2.5, // fee credit used
    "rec": 0.06666666, // amount to receive
    "ts": 1533834547 // timestamp
    "ci": "input_client_id" // input id for reference
  }
}
```

### POST /api/market/v2/place-ask(```beta```)

#### Description:
Create a sell order.

#### Body:
* `sym`   **string**    The symbol
* `amt`   **float**   Amount you want to sell with no trailing zero (e.g 0.10000000 is invalid, 0.1 is ok)
* `rat`   **float**   Rate you want for the order with no trailing zero (e.g 1000.00 is invalid, 1000 is ok)
* `typ`   **string**    Order type: limit or market (for market order, please specify rat as 0)
* `client_id`   **string**    your id for reference ( not required )


#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": 1, // order id
    "hash": "fwQ6dnQWQPs4cbatFGc9LPnpqyu", // order hash
    "typ": "limit", // order type
    "amt": 1.00000000, // selling amount
    "rat": 15000, // rate
    "fee": 37.5, // fee
    "cre": 37.5, // fee credit used
    "rec": 15000, // amount to receive
    "ts": 1533834844 // timestamp
    "ci": "input_client_id" // input id for reference
  }
}
```

### POST /api/market/v2/cancel-order(```beta```)

### Description:
Cancel an open order.

### Body:
* `sym`   **string**    The symbol
* `id`    **int**   Order id you wish to cancel
* `sd`    **string**    Order side: buy or sell
* `hash`  **string**    Cancel an order with order hash (optional). You don't need to specify sym, id, and sd when you specify order hash.

### Response:
```javascript
{
  "error": 0
}
```

# Additional
For the  use of `cur`(currency) for any APIs request. Please be cautious of these cryptocurrency when you specified on the request.

Name|Currency
---|---
Terra Classic|`LUNA`
Terra 2.0|`LUNA2`

# Error codes
Refer to the following descriptions:

Code | Description
------------ | ------------
0 | No error
1 | Invalid JSON payload
2 | Missing X-BTK-APIKEY
3 | Invalid API key
4 | API pending for activation
5 | IP not allowed
6 | Missing / invalid signature
7 | Missing timestamp
8 | Invalid timestamp
9 | Invalid user
10 | Invalid parameter
11 | Invalid symbol
12 | Invalid amount
13 | Invalid rate
14 | Improper rate
15 | Amount too low
16 | Failed to get balance
17 | Wallet is empty
18 | Insufficient balance
19 | Failed to insert order into db
20 | Failed to deduct balance
21 | Invalid order for cancellation
22 | Invalid side
23 | Failed to update order status
24 | Invalid order for lookup
25 | KYC level 1 is required to proceed
30 | Limit exceeds
40 | Pending withdrawal exists
41 | Invalid currency for withdrawal
42 | Address is not in whitelist
43 | Failed to deduct crypto
44 | Failed to create withdrawal record
45 | Nonce has to be numeric
46 | Invalid nonce
47 | Withdrawal limit exceeds
48 | Invalid bank account
49 | Bank limit exceeds
50 | Pending withdrawal exists
51 | Withdrawal is under maintenance
52 | Invalid permission
53 | Invalid internal address 
54 | Address has been deprecated
55 | Cancel only mode
56 | User has been suspended from purchasing
57 | User has been suspended from selling
90 | Server error (please contact support)

# Rate limits 
If the request rate exceeds the limit in any endpoints, the request will be blocked for 30 seconds. When blocked, HTTP response is 429 Too Many Requests. The limits apply to individual IP address accessing the API.

|Endpoint   | Rate Limit   |
| ------------ | ------------ |
| /api/market/ticker  | 100 req/sec  |
| /api/market/depth | 150 req/sec  |
| /api/market/symbols |  100 req/sec |
| /api/market/trades |  100 req/sec |
| /api/market/bids  |  100 req/sec |
| /api/market/asks  |  100 req/sec |
| /api/market/books  |  100 req/sec |
| /api/market/order-info  |  100 req/sec |
| /api/market/place-bid  | 50 req/sec  |
| /api/market/place-ask |  50 req/sec |
| /api/market/place-ask-by-fiat   | 45 req/sec  |
| /api/market/cancel-order  |  1,000 req/10sec |
| /api/market/balances |  150 req/sec |
| /api/market/wallet | 150 req/sec  |
| /api/crypto/deposit-history |  20 req/sec |
| /api/servertime  | 2,000 req/10secs  |
| /api/status | 100 req/sec  |
| /api/crypto/* | 250 req/10secs  |
| /api/fiat/* | 20 req/sec  |
| /api/user/*   |  20 req/sec |
| /tradingview/* | 100 req/sec  |
