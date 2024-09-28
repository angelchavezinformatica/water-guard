from server.request import Request
from server.response import get_response, Response


def index(request: Request) -> Response:
    return get_response(request)
