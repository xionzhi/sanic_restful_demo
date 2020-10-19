import socket

from sanic import Sanic

import config.dev as dev_config
import config.pro as pro_config
from service.v1.urls import api_blueprint_v1


app = Sanic(name=__name__)

hostname = socket.gethostname()
if hostname == 'pro_name':
    app.config.from_object(pro_config)
else:
    app.config.from_object(dev_config)

app.debug = app.config['APP_DEBUG']


def init_route():
    app.blueprint(api_blueprint_v1, url_prefix='/v1')


init_route()
