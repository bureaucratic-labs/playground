
from aiohttp import web
from aiohttp_cors import ResourceOptions, setup as setup_cors

from playground import views


def make_app():
    app = web.Application()
    cors = setup_cors(app, defaults={
        '*': ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        )
    })

    cors.add(
        app.router.add_route('POST', '/api/extract', views.extract)
    )
    cors.add(
        app.router.add_route('GET', '/api/version', views.version)
    )

    return app


app = make_app()
