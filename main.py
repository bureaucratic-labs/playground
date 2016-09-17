from ujson import dumps
from aiohttp import web
from functools import partial


from natasha import Combinator, DEFAULT_GRAMMARS


json_dumps = partial(dumps, ensure_ascii=False)


def serialize(results):
    for (grammar, rule, match) in results:
        yield {
            'grammar': grammar.__name__,
            'rule': rule,
            'match': match,
        }

async def extract(request):
    form = await request.post()
    results = app['combinator'].extract(form['text'])
    return web.json_response(list(serialize(results)), dumps=json_dumps)


def init(argv):
    app = web.Application()
    app.router.add_post("/api/extract", extract)
    app['combinator'] = Combinator(DEFAULT_GRAMMARS)
    return app
