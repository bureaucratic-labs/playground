# Playground

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
                "lastname": "Христа",
                "spans": [
                    [
                        106,
                        119
                    ]
                ]
            },
            "type": "person"
        },
        {
            "fields": {
                "firstname": "Мухаммед",
                "spans": [
                    [
                        85,
                        94
                    ]
                ]
            },
            "type": "person"
        },
        {
            "fields": {
                "name": "РФ",
                "spans": [
                    [
                        295,
                        297
                    ]
                ]
            },
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
                                "anim",
                                "sing",
                                "masc",
                                "NOUN",
                                "Name",
                                "gent"
                            ],
                            "normal_form": "иисус"
                        },
                        {
                            "grammemes": [
                                "anim",
                                "accs",
                                "sing",
                                "masc",
                                "NOUN",
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
                                "anim",
                                "sing",
                                "masc",
                                "NOUN",
                                "gent",
                                "Sgtm"
                            ],
                            "normal_form": "христос"
                        },
                        {
                            "grammemes": [
                                "anim",
                                "accs",
                                "sing",
                                "masc",
                                "NOUN",
                                "Sgtm"
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
                                "anim",
                                "sing",
                                "masc",
                                "NOUN",
                                "Name",
                                "gent"
                            ],
                            "normal_form": "иисус"
                        },
                        {
                            "grammemes": [
                                "anim",
                                "accs",
                                "sing",
                                "masc",
                                "NOUN",
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
                                "anim",
                                "sing",
                                "masc",
                                "NOUN",
                                "Name",
                                "gent"
                            ],
                            "normal_form": "мухаммед"
                        },
                        {
                            "grammemes": [
                                "anim",
                                "accs",
                                "sing",
                                "masc",
                                "NOUN",
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
                                "sing",
                                "NOUN",
                                "femn",
                                "gent",
                                "Fixd",
                                "Abbr",
                                "Geox",
                                "inan",
                                "Sgtm"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "sing",
                                "NOUN",
                                "femn",
                                "Fixd",
                                "Abbr",
                                "loct",
                                "Geox",
                                "inan",
                                "Sgtm"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "sing",
                                "NOUN",
                                "femn",
                                "Fixd",
                                "Abbr",
                                "nomn",
                                "Geox",
                                "inan",
                                "Sgtm"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "sing",
                                "ablt",
                                "NOUN",
                                "femn",
                                "Fixd",
                                "Abbr",
                                "Geox",
                                "inan",
                                "Sgtm"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "sing",
                                "datv",
                                "NOUN",
                                "femn",
                                "Fixd",
                                "Abbr",
                                "Geox",
                                "inan",
                                "Sgtm"
                            ],
                            "normal_form": "рф"
                        },
                        {
                            "grammemes": [
                                "sing",
                                "NOUN",
                                "femn",
                                "Fixd",
                                "accs",
                                "Abbr",
                                "Geox",
                                "inan",
                                "Sgtm"
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
