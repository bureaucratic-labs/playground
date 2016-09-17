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

def loader_verification(request):
    return web.Response(body=b'loaderio-f68cd84a6bf29dc6f5b6fe0726bce603')

def init(argv):
    app = web.Application()
    app.router.add_post('/api/extract', extract)
    app.router.add_get('/loaderio-f68cd84a6bf29dc6f5b6fe0726bce603.txt', loader_verification)
    app['combinator'] = Combinator(DEFAULT_GRAMMARS)
    return app
