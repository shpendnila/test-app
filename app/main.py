from flask import Flask
from app.routes.hello import hello_router


def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_router)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=6000)
