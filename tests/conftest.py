import pytest

from app.app import create_app


@pytest.fixture
def app():
    async def cleanup(app):
        pass

    async def setup(app):
        pass

    app = create_app()
    app.on_cleanup.append(cleanup)
    app.on_startup.append(setup)
    return app


@pytest.fixture
def client(app, loop, aiohttp_client):
    return loop.run_until_complete(aiohttp_client(app))
