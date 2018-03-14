
from hashlib import sha256
from datetime import datetime
from collections import namedtuple

from yargy import __version__ as yargy_version
from natasha import __version__ as natasha_version
from pymorphy2 import __version__ as pymorphy_version

from playground.settings import (
    EXTRACTORS,
    REDIS_ISSUES_KEY,
    REDIS_ISSUES_TTL
)
from playground.utils import jsonify


class Issue(namedtuple('Issue', 'id, timestamp, text, description')):
    @classmethod
    def from_text(cls, text, description):
        return cls(
            id=sha256(text.encode('utf8')).hexdigest(),
            timestamp=datetime.now(),
            text=text,
            description=description
        )

    @property
    def as_json(self):
        return {
            '_id': self.id,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'text': self.text,
            'description': self.description
        }

    @classmethod
    def from_blob(cls, data):
        return cls(
            id=data[b'_id'].decode('utf8'),
            timestamp=datetime.strptime(
                data[b'timestamp'].decode('utf8'),
                '%Y-%m-%d %H:%M:%S'
            ),
            text=data[b'text'].decode('utf8'),
            description=data[b'description'].decode('utf8')
        )


async def extract(request):
    form = await request.post()
    text = form['text']
    matches = []
    for extractor in EXTRACTORS:
        matches.extend(extractor(text).as_json)
    matches = sorted(matches, key=lambda _: _['span'])
    return jsonify(matches)


def version(request):
    return jsonify({
        'yargy': yargy_version,
        'natasha': natasha_version,
        'pymorphy': pymorphy_version,
    })


async def get_issues(request):
    async with request.app.redis.get() as conn:
        ids = await conn.keys('{0}:*'.format(REDIS_ISSUES_KEY))
        items = [await conn.hgetall(_) for _ in ids]
        items = [Issue.from_blob(_).as_json for _ in items]
        return jsonify(items)


async def send_issue(request):
    form = await request.post()
    text = form['text']
    description = form['description']

    async with request.app.redis.get() as conn:
        item = Issue.from_text(text, description)
        key = '{0}:{1}'.format(REDIS_ISSUES_KEY, item.id)
        await conn.hmset_dict(key, item.as_json)
        await conn.expire(key, REDIS_ISSUES_TTL)
    return jsonify({
        'status': True
    })
