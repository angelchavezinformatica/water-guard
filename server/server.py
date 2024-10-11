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
            try:
                conn, addr = self.sock.accept()
                self.request_handler(conn, addr)
            except OSError:
                pass

    def request_handler(self, conn: socket.socket, addr):
        try:
            data = conn.recv(self.buffer_size)
            if not data:
                return
            request = Request(data, addr)
            response = self.router(request)
            logger(response)
            data = response.encode()
            self.send_async(conn, data)
        finally:
            conn.close()

    def send_async(self, conn: socket.socket, data: bytes, chunk_size=512):
        total_sent = 0
        data_len = len(data)

        while total_sent < data_len:
            sent = conn.send(data[total_sent:total_sent+chunk_size])
            if sent == 0:
                return
            total_sent += sent

    def router(self, request: Request) -> Response:
        for path in self.routes:
            if path.method != request.method:
                continue
            if (path.start and request.path.startswith(path.path)) or \
                    (not path.start and request.path == path.path):
                return path.view(request=request)
        return get_response_not_found(request=request)
