
import json

from aiohttp import web


def dumps(data):
    return json.dumps(
        data,
        indent=2,
        ensure_ascii=False
    )


def jsonify(data):
    return web.json_response(
        data,
        dumps=dumps
    )
