from typing import Optional
from aiohttp.web import (
    Application as AiohttpApplication, run_app as aiohttp_run_app,
    Request as AiohttpRequest, View as AiohttpView,
)

from app.store import setup_accessors

from .routes import setup_routes
from app.store.crm.accessor import CrmAccessor

from main import app

class Application(AiohttpApplication):
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_routes(app)
    setup_accessors(app)
    aiohttp_run_app(app=app, host='127.0.0.1', port=8000)
