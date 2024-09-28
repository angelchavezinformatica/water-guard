from .response import Response
from .types import HttpMethod


class Path:
    def __init__(
        self,
        path: str,
        view: Response,
        start: bool = False,
        method: HttpMethod = HttpMethod.GET,
    ) -> None:
        self.path = path
        self.view = view
        self.start = start
        self.method = method
