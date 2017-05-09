from aiohttp import web

from playground.app import app
from playground.settings import BIND_HOST, BIND_PORT

if __name__ == '__main__':
    web.run_app(app, host=BIND_HOST, port=BIND_PORT)
