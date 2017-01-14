from ujson import dumps
from functools import partial

from aiohttp import web
import aiohttp_cors

import yargy
import natasha

from yargy.normalization import get_normalized_text
from natasha import Combinator, DEFAULT_GRAMMARS

json_dumps = partial(dumps, ensure_ascii=False)


def serialize(results):
    for (grammar, tokens) in results:
        yield {
            'grammar': grammar.__class__.__name__,
            'rule': grammar.name,
            'tokens': [
                {
                    'value': t.value,
                    'position': t.position,
                    'forms': [
                        {
                            'normal_form': f['normal_form'],
                            'grammemes': f['grammemes'],
                        } for f in t.forms
                    ],
                } for t in tokens
            ],
            'normal_form': get_normalized_text(tokens),
        }

async def extract(request):
    form = await request.post()
    combinator = request.app['combinator']
    matches = combinator.extract(form['text'])
    results = serialize(combinator.resolve_matches(matches))
    return web.json_response(results, dumps=json_dumps)

def version(request):
    return web.json_response({
        'natasha': natasha.__version__,
        'yargy': yargy.__version__,
    })

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
    cors.add(app.router.add_route('GET', '/api/version', version))
    return app
