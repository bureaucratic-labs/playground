
from yargy import __version__ as yargy_version
from natasha import __version__ as natasha_version

from aiohttp import web

from playground.settings import EXTRACTOR
from playground.utils import json_dumps


async def extract(request):
    form = await request.post()
    matches = EXTRACTOR(form['text'])
    return web.json_response(
        matches.as_json,
        dumps=json_dumps
    )


def version(request):
    return web.json_response({
        'yargy': yargy_version,
        'natasha': natasha_version,
    })
