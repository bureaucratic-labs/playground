# Playground [![Build Status](https://travis-ci.org/bureaucratic-labs/playground.svg?branch=master)](https://travis-ci.org/bureaucratic-labs/playground)

```bash
$ http --form https://natasha.b-labs.pro/api/extract  \
        text='Простите, еще несколько цитат из приговора. «…Отрицал существование Иисуса и пророка Мухаммеда», «наделял Иисуса Христа качествами ожившего мертвеца — зомби» [и] «качествами покемонов — представителей бестиария японской мифологии, тем самым совершил преступление, предусмотренное статьей 148 УК РФ».'

$ HTTP/1.1 200 OK
Content-Length: 276
Content-Type: application/json; charset=utf-8
Date: Thu, 24 Aug 2017 14:18:22 GMT
Server: Python/3.5 aiohttp/2.2.5

[
  {
    "type": "Name",
    "fact": {
      "first": "иисус",
      "last": null,
      "middle": null,
      "nick": null
    },
    "span": [
      68,
      74
    ]
  },
  {
    "type": "Name",
    "fact": {
      "first": "мухаммед",
      "last": null,
      "middle": null,
      "nick": null
    },
    "span": [
      85,
      94
    ]
  },
  {
    "type": "Name",
    "fact": {
      "first": "иисус",
      "last": "христос",
      "middle": null,
      "nick": null
    },
    "span": [
      106,
      119
    ]
  }
]
```
