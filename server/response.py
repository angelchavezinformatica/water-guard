from .request import Request
from .types import HttpStatusCode, StatusCode


class Response:
    """Response parser"""

    CRLF = '\n'
    END_HEADERS = CRLF + CRLF

    def __init__(
        self,
        request: Request,
        code: StatusCode,
        headers: dict = {},
        body: str = ""
    ) -> None:
        self.rq = request.get_request_line()
        self.code = code
        self.headers = headers
        self.body = body

    def encode(self) -> bytes:
        message = f"{self.rq.http_version} {self.code.code} {self.code.name}"
        for header in self.headers:
            message += f"{self.CRLF}{header}: {self.headers[header]}"
        message += self.END_HEADERS + self.body
        return message.encode()


def get_response(
    request: Request,
    message: str = "",
    content_type: str = "text/plain",
    code=HttpStatusCode.OK,
) -> Response:
    """Create an OK response"""
    return Response(
        body=message,
        code=code,
        headers={
            'Content-Type': content_type,
            'Content-Length': len(message),
        },
        request=request,
    )


def get_file_response(
    request: Request,
    path: str,
    content_type: str = "text/plain",
) -> Response:
    with open(path, mode='r') as file:
        return get_response(
            request,
            message=file.read(),
            content_type=content_type,
        )


def get_response_not_found(request: Request) -> Response:
    """Create an 404 response"""
    return Response(
        code=HttpStatusCode.NOT_FOUND,
        request=request,
    )
