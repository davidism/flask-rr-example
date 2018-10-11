from functools import partial

from flask import Flask
from flask import request
from flask import Response as FlaskResponse
from werkzeug.local import Local
from werkzeug.local import LocalManager
from werkzeug.wrappers import Response as WerkzeugResponse

_rr_local = Local()
response = _rr_local("response")


class Response(FlaskResponse):
    def copy_from(self, other: WerkzeugResponse):
        self.headers = other.headers
        self.status = other.status

        try:
            self.response.close()
        except AttributeError:
            pass

        self.response = other.response
        self.direct_passthrough = other.direct_passthrough


class _RRViewFunctions(dict):
    def __getitem__(self, key):
        view = super().__getitem__(key)
        return partial(view, request, response)


class FlaskRR(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.view_functions = _RRViewFunctions(self.view_functions)
        self.wsgi_app = LocalManager([_rr_local]).make_middleware(self.wsgi_app)

    def make_response(self, rv):
        if rv is not None:
            res = super().make_response(rv)
            response.copy_from(res)

        return response

    def wsgi_app(self, environ, start_response):
        _rr_local.response = Response()
        return super().wsgi_app(environ, start_response)
