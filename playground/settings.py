
from os import environ

from natasha import NamesExtractor


EXTRACTOR = NamesExtractor()

BIND_HOST = environ.get('HOST', '0.0.0.0')
BIND_PORT = int(environ.get('PORT', 4000))
