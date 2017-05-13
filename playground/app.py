from aiohttp import web
from aiohttp_cors import ResourceOptions, setup as setup_cors

from playground import views

app = web.Application()
cors = setup_cors(app, defaults={
    '*': ResourceOptions(
        allow_credentials=True,
        expose_headers='*',
        allow_headers='*',
    )
})

'''
Setup routes
'''

cors.add(
    app.router.add_route('POST', '/api/extract', views.extract)
)
cors.add(
    app.router.add_route('GET', '/api/version', views.version)
)