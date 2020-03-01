# Bitkub Python



A Python library for [bitkub.com](https://github.com/bitkub/bitkub-official-api-docs) API

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Creating a Bitkub](#creating)
  - [Viewing status](#viewingstatus)
  - [Viewing servertime](#viewingservertime)
  - Coming Soon ...

## Installation <a name="installation"></a>

    pip install bitkub

## Usage <a name="usage"></a>

    from bitkub import Bitkub

### Creating a Bitkub Object <a name="creating"></a>

    bitkub = Bitkub()

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
### Viewing status <a name="viewingstatus"></a>
#### Function
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
#### Function
    bitkub.servertime()

#### Response:

    1583051817
