from flask import (
    Blueprint,
    Response,
    jsonify,
)
import requests

hello_router = Blueprint('hello', __name__)


@hello_router.route('/health')
def check_health():
    return jsonify(
        {"message": "Okay!!!"}
    )


@hello_router.route('/hello')
def hello():
    return Response(
        response=jsonify({"message": "Hello from k8s!"}),
        status=200,
        content_type="application/json",
    )


@hello_router.route('/check_web')
def get_web_info():
    # get response from nginx controller
    resp = requests.get(
        'http://ingress-nginx-controller.ingress-nginx/web'
    )
    return resp.content
