from datetime import datetime

from aiohttp import web

routers = web.RouteTableDef()


@routers.get('/healthcheck/')
async def healthcheck(request):
    data = {
        'date': datetime.utcnow().isoformat()
    }
    return web.json_response(data)


async def setup(app):
    # Define app objects here likewise DB connections
    pass


def create_app():
    app = web.Application()
    app.add_routes(routers)
    app.on_startup.append(setup)
    return app
