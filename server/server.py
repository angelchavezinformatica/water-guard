import socket

from .logger import logger
from .request import Request
from .response import get_response_not_found, Response
from .router import Path
from .wlan import WLAN


class Server:

    def __init__(self, routes: list[Path], host='', port=80, buffer_size=1024):
        self.routes = routes
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()

        self.ifconfig = None
        self.buffer_size = buffer_size

    def run(self):
        while not WLAN.isconnected():
            pass

        self.ifconfig = WLAN.ifconfig()

        print('Server on:', self.ifconfig[0])

        while True:
            conn, addr = self.sock.accept()
            self.request_handler(conn, addr)

    def request_handler(self, conn: socket.socket, addr: socket._RetAddress):
        data = conn.recv(self.buffer_size)
        request = Request(data, addr)
        response = self.router(request)
        logger(response)
        conn.sendall(response.encode())
        conn.close()

    def router(self, request: Request) -> Response:
        for path in self.routes:
            if path.method != request.method:
                continue
            if (path.start and request.path.startswith(path.path)) or \
                    (not path.start and request.path == path.path):
                return path.view(request=request)
        return get_response_not_found(request=request)
