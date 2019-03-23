"""
This script runs the CodeQualityPortal application using a development server.
"""

from os import environ
from CodeQualityPortal import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8982'))
    except ValueError:
        PORT = 8982
    app.run(HOST, PORT)
