import socket

import compatibility as cpb

from .types import RequestLine


class Request:
    """Request parser"""

    def __init__(self, data: bytes, addr: socket._RetAddress) -> None:
        self.addr = addr

        data: list[str] = cpb.splitlines(data.decode())
        method, self.path, self.http_version = data[0].split(' ')
        data.pop(0)
        self.method = method
        self.headers = {}
        self.body = data[-1]

        for header in data:
            if header == '':
                break
            key, value = header.split(': ')
            self.headers[key] = value

    def get_request_line(self) -> RequestLine:
        return RequestLine(self.method, self.path, self.http_version)
