
from os import environ
from urllib.parse import urlparse

from natasha import (
    NamesExtractor,
    LocationExtractor,
    AddressExtractor,
)

EXTRACTORS = [
    NamesExtractor(),
    LocationExtractor(),
    AddressExtractor(),
]

BIND_HOST = environ.get('HOST', '0.0.0.0')
BIND_PORT = int(environ.get('PORT', 4000))
REDIS_URL = environ.get('REDIS_URL', 'redis://localhost:6379')

redis = urlparse(REDIS_URL)

REDIS_HOST = redis.hostname
REDIS_PORT = redis.port
REDIS_PASSWORD = redis.password

REDIS_ISSUES_KEY = 'issues'
REDIS_ISSUES_TTL = 60 * 60 * 24 * 7  # 7 days
