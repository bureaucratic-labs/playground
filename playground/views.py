from hashlib import sha256
from datetime import datetime

from yargy import __version__ as yargy_version
from natasha import __version__ as natasha_version
from pymorphy2 import __version__ as pymorphy_version
from pymorphy2_dicts_ru import __version__ as pymorphy_dicts_version

from aiohttp import web

from playground.settings import *
from playground.utils import json_dumps


async def extract(request):
    form = await request.post()
    matches = []
    for extractor in EXTRACTORS:
        matches.extend(extractor(form['text']).as_json)
    return web.json_response(
        matches,
        dumps=json_dumps
    )


def version(request):
    return web.json_response({
        'yargy': yargy_version,
        'natasha': natasha_version,
        'pymorphy': pymorphy_version,
        'pymorphy_dicts': pymorphy_dicts_version,
    })


async def get_issues(request):
    async with request.app.redis.get() as conn:
        items = await conn.keys('{0}:*'.format(REDIS_ISSUES_KEY))
        items = [await conn.hgetall(_id) for _id in items]
        items = [
            {
                '_id': item[b'_id'].decode('utf-8'),
                'text': item[b'text'].decode('utf-8'),
                'description': item[b'description'].decode('utf-8'),
                'datetime': item[b'datetime'].decode('utf-8'),
            } for item in items
        ]
        return web.json_response(
            items,
            dumps=json_dumps,
        )

async def send_issue(request):
    form = await request.post()
    text = form['text']
    description = form['description']
    _id = sha256(text.encode('utf-8')).hexdigest()
    async with request.app.redis.get() as conn:
        key = '{0}:{1}'.format(REDIS_ISSUES_KEY, _id)
        await conn.hmset_dict(
            key,
            {
                '_id': _id,
                'text': text,
                'description': description,
                'datetime': str(datetime.now()),
            }
        )
        await conn.expire(key, REDIS_ISSUES_TTL)
    return web.json_response(
        {
            'status': True,
        },
        dumps=json_dumps,
    )
