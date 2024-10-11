class HttpMethod:
    HEAD = "HEAD"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"


class StatusCode:
    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name


class HttpStatusCode:
    OK = StatusCode(200, "OK")
    CREATED = StatusCode(201, "Created")
    BAD_REQUEST = StatusCode(400, "Bad Request")
    NOT_FOUND = StatusCode(404, "Not Found")


class RequestLine:
    """A representation of the request line"""

    def __init__(self, method: HttpMethod, path: str, http_version: str) -> None:
        self.method = method
        self.path = path
        self.http_version = http_version
