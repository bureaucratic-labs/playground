from yargy import __version__ as yargy_version
from natasha import __version__ as natasha_version


from aiohttp import web

from playground.utils import json_dumps, serialize_entities
from playground.settings import Combinator


async def extract(request):
    form = await request.post()
    matches = Combinator.extract(form['text'])
    results = serialize_entities(Combinator.resolve_matches(matches))
    return web.json_response(results, dumps=json_dumps)


def version(request):
    return web.json_response({
        'yargy': yargy_version,
        'natasha': natasha_version,
    })
