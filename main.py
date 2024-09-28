from app import routes
from server import Server

server = Server(routes)
server.run()
