from .response import Response
from .types import HttpStatusCode

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[1m"


def logger(response: Response) -> None:
    """A simple logger."""
    if response.code == HttpStatusCode.OK:
        message = f"{GREEN}"
    else:
        message = f"{RED}"
    message += f"{BOLD}{response.rq.method} {response.code.code} "
    message += f"{response.rq.path}"
    message += RESET
    print(message)
