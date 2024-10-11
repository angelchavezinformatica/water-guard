from server import Path

from .views import bomb_on, bomb_off, bomb_state, index, javascript, style

routes = [
    Path('/', index),
    Path('/style.css', style),
    Path('/main.js', javascript),
    Path('/bomb/on', bomb_on),
    Path('/bomb/off', bomb_off),
    Path('/bomb/state', bomb_state),
]
