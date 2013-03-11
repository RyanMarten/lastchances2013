# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver",Server(
	use_debugger = True,
	use_reloader = True,
	host = '127.0.0.1',
	port = 9003)
)

if __name__ == "__main__":
	manager.run()
