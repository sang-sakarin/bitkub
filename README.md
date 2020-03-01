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

#### Description:
List all available symbols.

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

    coming soon

### Viewing ticker <a name="viewingticker"></a>

#### Description:
Get ticker information.

#### Function:
    bitkub.ticker()

#### Response:

    coming soon
