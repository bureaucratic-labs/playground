# Playground [![Build Status](https://travis-ci.org/bureaucratic-labs/playground.svg?branch=master)](https://travis-ci.org/bureaucratic-labs/playground)

```bash
$ http --form https://natasha.b-labs.pro/api/extract  \
        text='Простите, еще несколько цитат из приговора. «…Отрицал существование Иисуса и пророка Мухаммеда», «наделял Иисуса Христа качествами ожившего мертвеца — зомби» [и] «качествами покемонов — представителей бестиария японской мифологии, тем самым совершил преступление, предусмотренное статьей 148 УК РФ».'

HTTP/1.1 200 OK
Content-Length: 2188
Content-Type: application/json; charset=utf-8
Date: Sat, 13 May 2017 09:18:15 GMT
Server: Python/3.6 aiohttp/2.0.7

{
    "objects": [
        {
            "fields": {
                "firstname": "Иисус",
                "lastname": "Христа"
            },
            "spans": [
                {
                    "normalized": "Иисус Христа",
                    "position": [
                        106,
                        119
                    ]
                },
                {
                    "normalized": "Иисус",
                    "position": [
                        68,
                        74
                    ]
                }
            ],
            "type": "person"
        },
        {
            "fields": {
                "firstname": "Мухаммед"
            },
            "spans": [
                {
                    "normalized": "Мухаммед",
                    "position": [
                        85,
                        94
                    ]
                }
            ],
            "type": "person"
        },
        {
            "fields": {
                "name": "РФ"
            },
            "spans": [
                {
                    "normalized": "РФ",
                    "position": [
                        295,
                        297
                    ]
                }
            ],
            "type": "location"
        }
    ],
    "spans": [
        {
            "grammar": "ProbabilisticPerson",
            "normal_form": "Иисус Христа",
            "rule": "FirstnameAndLastname",
            "tokens": [
                {
                    "forms": [
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "masc",
                                "gent",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "иисус"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "accs",
                                "masc",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "иисус"
                        }
                    ],
                    "position": [
                        106,
                        112
                    ],
                    "value": "Иисуса"
                },
                {
                    "forms": [
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "masc",
                                "Sgtm",
                                "gent",
                                "anim"
                            ],
                            "normal_form": "христос"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "accs",
                                "masc",
                                "Sgtm",
                                "anim"
                            ],
                            "normal_form": "христос"
                        }
                    ],
                    "position": [
                        113,
                        119
                    ],
                    "value": "Христа"
                }
            ]
        },
        {
            "grammar": "Person",
            "normal_form": "Иисус",
            "rule": "Firstname",
            "tokens": [
                {
                    "forms": [
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "masc",
                                "gent",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "иисус"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "accs",
                                "masc",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "иисус"
                        }
                    ],
                    "position": [
                        68,
                        74
                    ],
                    "value": "Иисуса"
                }
            ]
        },
        {
            "grammar": "Person",
            "normal_form": "Мухаммед",
            "rule": "Firstname",
            "tokens": [
                {
                    "forms": [
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "masc",
                                "gent",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "мухаммед"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "sing",
                                "accs",
                                "masc",
                                "anim",
                                "Name"
                            ],
                            "normal_form": "мухаммед"
                        }
                    ],
                    "position": [
                        85,
                        94
                    ],
                    "value": "Мухаммеда"
                }
            ]
        },
        {
            "grammar": "Location",
            "normal_form": "РФ",
            "rule": "Object",
            "tokens": [
                {
                    "forms": [
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "Sgtm",
                                "Geox",
                                "gent",
                                "Abbr",
                                "Fixd",
                                "inan"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "loct",
                                "Sgtm",
                                "Geox",
                                "Abbr",
                                "Fixd",
                                "inan"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "Sgtm",
                                "Geox",
                                "Abbr",
                                "Fixd",
                                "nomn",
                                "inan"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "Sgtm",
                                "Geox",
                                "Abbr",
                                "Fixd",
                                "ablt",
                                "inan"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "Sgtm",
                                "Geox",
                                "Abbr",
                                "Fixd",
                                "datv",
                                "inan"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "NOUN",
                                "femn",
                                "sing",
                                "accs",
                                "Sgtm",
                                "Geox",
                                "Abbr",
                                "Fixd",
                                "inan"
                            ],
                            "normal_form": "рф"
                        }
                    ],
                    "position": [
                        295,
                        297
                    ],
                    "value": "РФ"
                }
            ]
        }
    ]
}
```
