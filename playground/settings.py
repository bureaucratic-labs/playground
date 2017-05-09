from os import environ

from natasha import Combinator, DEFAULT_GRAMMARS
from natasha.grammars.person import ProbabilisticPerson


GRAMMARS = DEFAULT_GRAMMARS + [
    ProbabilisticPerson,
]

Combinator = Combinator(GRAMMARS)

BIND_HOST = environ.get('HOST', '0.0.0.0')
BIND_PORT = int(environ.get('PORT', 4000))
