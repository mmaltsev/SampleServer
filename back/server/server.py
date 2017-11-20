"""File that contains the endpoints for the app."""
import logging
import traceback

from gevent.wsgi import WSGIServer

from flask import (Flask, Response, render_template, request,
                   send_from_directory)
from pylogging import HandlerType, setup_logger

from .config import CONFIG

logger = logging.getLogger(__name__)
app = Flask(__name__, static_folder='../../front/src')


@app.before_first_request
def init():
    """Initialize the application with defaults."""
    logger.info("App initialized")


@app.route('/')
def root():
    """Root route."""
    logger.info("route: /")
    return app.send_static_file('index.html')
    # return render_template("index.html")
    return


@app.route('/index')
def system():
    """System route."""
    logger.info("route: /index")
    return app.send_static_file('index.html')


@app.route('/outdex')
def object():
    """Object route."""
    logger.info("route: /outdex")
    return app.send_static_file('outdex.html')


@app.route('/node_modules/<path:path>')
def send_node_modules(path):
    """Server static files from node_modules."""
    logger.info("route: node_modules/{}".format(path))
    path_prefix = '../../front/node_modules'
    return send_from_directory(path_prefix, path)


@app.route('/<path:path>')
def send_static(path):
    """Server static files."""
    logger.info("route: {}".format(path))
    path_prefix = '../../front/src'
    return send_from_directory(path_prefix, path)


def main():
    """Main entry point of the app."""
    try:
        http_server = WSGIServer((CONFIG['host'], CONFIG['port']),
                                 app,
                                 log=logging,
                                 error_log=logging)

        http_server.serve_forever()
    except Exception as exc:
        logger.error(exc.message)
        logger.exception(traceback.format_exc())
    finally:
        # Do something here
        pass
