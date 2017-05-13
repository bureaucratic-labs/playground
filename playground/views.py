from yargy import __version__ as yargy_version
from natasha import __version__ as natasha_version


from aiohttp import web

from playground.utils import (
    json_dumps,
    extract_objects,
    serialize_spans,
    serialize_objects,
)
from playground.settings import Combinator


async def extract(request):
    form = await request.post()
    matches = list(
        Combinator.resolve_matches(
            Combinator.extract(form['text'])
        )
    )

    objects = extract_objects(matches)

    response = {
        'spans': serialize_spans(matches),
        'objects': serialize_objects(objects),
    }

    return web.json_response(response, dumps=json_dumps)


def version(request):
    return web.json_response({
        'yargy': yargy_version,
        'natasha': natasha_version,
    })
