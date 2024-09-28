from server import Path

from .views import index

routes = [
    Path('/', index)
]
