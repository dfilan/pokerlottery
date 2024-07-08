import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # set environment variable "FLASK_SECRET_KEY" to a random string
    # then the below will load it as SECRET_KEY.
    app.config.from_prefixed_env()
    # app.config.from_mapping(
    #     SECRET_KEY=os.environ['SECRET_KEY'],
    #     # SECRET_KEY='dev',
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # TODO: if I delete this, change test_factory.py accordingly
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import index
    app.register_blueprint(index.bp)

    from . import about
    app.register_blueprint(about.bp)
    
    return app
