
from aiohttp import web
from aiohttp_cors import ResourceOptions, setup as setup_cors

from aioredis import create_pool as create_redis

from playground import settings, views


async def setup_redis(app):
    app.redis = await create_redis(
        address=(settings.REDIS_HOST, settings.REDIS_PORT),
        password=settings.REDIS_PASSWORD,
    )


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
    cors.add(
        app.router.add_route('GET', '/api/issues', views.get_issues)
    )
    cors.add(
        app.router.add_route('POST', '/api/issues', views.send_issue)
    )

    app.on_startup.append(setup_redis)

    return app


app = make_app()
