# Playground

```bash
$ http --form POST http://natasha-playground.herokuapp.com/api/extract text='министру экономического развития рф антону силуанову'

HTTP/1.1 200 OK
Content-Length: 1977
Content-Type: application/json; charset=utf-8
Date: Sat, 14 Jan 2017 07:50:07 GMT
Server: Python/3.5 aiohttp/1.2.0

[
    {
        "grammar": "Person",
        "normal_form": "министр экономического развития рф антон силуанов",
        "rule": "WithPosition",
        "tokens": [
            {
                "forms": [
                    {
                        "grammemes": [
                            "sing",
                            "NOUN",
                            "anim",
                            "masc",
                            "datv"
                        ],
                        "normal_form": "министр"
                    }
                ],
                "position": [
                    0,
                    8
                ],
                "value": "министру"
            },
            {
                "forms": [
                    {
                        "grammemes": [
                            "gent",
                            "ADJF",
                            "sing",
                            "neut"
                        ],
                        "normal_form": "экономический"
                    },
                    {
                        "grammemes": [
                            "gent",
                            "ADJF",
                            "sing",
                            "masc"
                        ],
                        "normal_form": "экономический"
                    },
                    {
                        "grammemes": [
                            "sing",
                            "ADJF",
                            "anim",
                            "masc",
                            "accs"
                        ],
                        "normal_form": "экономический"
                    }
                ],
                "position": [
                    9,
                    23
                ],
                "value": "экономического"
            },
            {
                "forms": [
                    {
                        "grammemes": [
                            "inan",
                            "NOUN",
                            "sing",
                            "gent",
                            "neut"
                        ],
                        "normal_form": "развитие"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "plur",
                            "nomn",
                            "NOUN",
                            "neut"
                        ],
                        "normal_form": "развитие"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "plur",
                            "NOUN",
                            "accs",
                            "neut"
                        ],
                        "normal_form": "развитие"
                    }
                ],
                "position": [
                    24,
                    32
                ],
                "value": "развития"
            },
            {
                "forms": [
                    {
                        "grammemes": [
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "femn",
                            "gent",
                            "NOUN",
                            "sing"
                        ],
                        "normal_form": "рф"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "loct",
                            "femn",
                            "NOUN",
                            "sing"
                        ],
                        "normal_form": "рф"
                    },
                    {
                        "grammemes": [
                            "nomn",
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "femn",
                            "NOUN",
                            "sing"
                        ],
                        "normal_form": "рф"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "ablt",
                            "femn",
                            "NOUN",
                            "sing"
                        ],
                        "normal_form": "рф"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "datv",
                            "femn",
                            "NOUN",
                            "sing"
                        ],
                        "normal_form": "рф"
                    },
                    {
                        "grammemes": [
                            "inan",
                            "Geox",
                            "Sgtm",
                            "Abbr",
                            "Fixd",
                            "femn",
                            "NOUN",
                            "sing",
                            "accs"
                        ],
                        "normal_form": "рф"
                    }
                ],
                "position": [
                    33,
                    35
                ],
                "value": "рф"
            },
            {
                "forms": [
                    {
                        "grammemes": [
                            "Name",
                            "NOUN",
                            "sing",
                            "masc",
                            "anim",
                            "datv"
                        ],
                        "normal_form": "антон"
                    }
                ],
                "position": [
                    36,
                    42
                ],
                "value": "антону"
            },
            {
                "forms": [
                    {
                        "grammemes": [
                            "NOUN",
                            "sing",
                            "masc",
                            "Sgtm",
                            "anim",
                            "Surn",
                            "datv"
                        ],
                        "normal_form": "силуанов"
                    },
                    {
                        "grammemes": [
                            "Poss",
                            "ADJF",
                            "sing",
                            "masc",
                            "datv"
                        ],
                        "normal_form": "силуанов"
                    }
                ],
                "position": [
                    43,
                    52
                ],
                "value": "силуанову"
            }
        ]
    }
]
```
