import socket
import uasyncio as asyncio

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
        self.sock.setblocking(False)

        self.ifconfig = None
        self.buffer_size = buffer_size

    async def run_non_blocking(self):
        while not WLAN.isconnected():
            await asyncio.sleep(1)

        self.ifconfig = WLAN.ifconfig()

        print('Server on:', self.ifconfig[0])

        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                await self.request_handler(conn, addr)
            except OSError:
                await asyncio.sleep(0.1)

    async def request_handler(self, conn: socket.socket, addr):
        try:
            data = await asyncio.wait_for(self.read_async(conn), timeout=10)
            if not data:
                return
            request = Request(data, addr)
            response = self.router(request)
            logger(response)
            await self.send_async(conn, response.encode())
        finally:
            conn.close()

    async def read_async(self, conn: socket.socket):
        while True:
            try:
                return conn.recv(self.buffer_size)
            except OSError:
                await asyncio.sleep(0.1)

    async def send_async(self, conn: socket.socket, data: bytes, chunk_size=512):
        total_sent = 0
        data_len = len(data)
        while total_sent < data_len:
            try:
                sent = conn.send(data[total_sent:total_sent+chunk_size])
                if sent == 0:
                    raise RuntimeError("Socket connection broken")
                total_sent += sent
            except OSError:
                await asyncio.sleep(0.1)

    def router(self, request: Request) -> Response:
        for path in self.routes:
            if path.method != request.method:
                continue
            if (path.start and request.path.startswith(path.path)) or \
                    (not path.start and request.path == path.path):
                return path.view(request=request)
        return get_response_not_found(request=request)
