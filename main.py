from flask import Flask
from views.api import api
from dao.db import CassandraDBConnector
from cassandra.cqlengine import connection
from flask.ext.cache import Cache


def create_app():
    
    app = Flask(__name__)
    cache = Cache(app,config={'CACHE_TYPE': 'simple'})
    cache.init_app(app)

    app.debug = True
    app.register_blueprint(api)
    db = CassandraDBConnector()

    return app

restApp = create_app()

if __name__ == '__main__':
    connection.setup(['127.0.0.1'], 'cqlengine', protocol_version=3)
    restApp.run(host="0.0.0.0", port=8081)
