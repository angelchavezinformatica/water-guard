import os

import compatibility as cpb
from server.request import Request
from server.response import get_response, get_file_response, Response
from state import state


def _get_bomb_state(request: Request) -> Response:
    response = f"""{{"state": {"true" if state.bomb.get_state() else "false"}}}"""
    return get_response(request, message=response, content_type='application/json')


def index(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'index.html')
    return get_file_response(
        request,
        file_path,
        'text/html'
    )


def style(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'style.css')
    return get_file_response(
        request,
        file_path,
        'text/css'
    )


def javascript(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'main.js')
    return get_file_response(
        request,
        file_path,
        'text/javascript'
    )


def bomb_on(request: Request) -> Response:
    state.bomb.on()
    return _get_bomb_state(request)


def bomb_off(request: Request) -> Response:
    state.bomb.off()
    return _get_bomb_state(request)


def bomb_state(request: Request) -> Response:
    return _get_bomb_state(request)
