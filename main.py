from ujson import dumps
from functools import partial

from aiohttp import web
import aiohttp_cors

from natasha import Combinator, DEFAULT_GRAMMARS

json_dumps = partial(dumps, ensure_ascii=False)


def serialize(results):
    for (grammar, match) in results:
        yield {
            'grammar': grammar.__class__.__name__,
            'rule': grammar.name,
            'match': match,
        }

async def extract(request):
    form = await request.post()
    combinator = request.app['combinator']
    results = combinator.resolve_matches(combinator.extract(form['text']))
    return web.json_response(list(serialize(results)), dumps=json_dumps)

def init(argv):
    app = web.Application()
    app['combinator'] = Combinator(DEFAULT_GRAMMARS)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })
    cors.add(app.router.add_route('POST', '/api/extract', extract))
    return app
