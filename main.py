import os

from flask import Flask, request, jsonify, make_response
import numpy.linalg as np_linalg

from utils import *

app = Flask(__name__)
config = read_config("config.json")

HTTP_INVALID_DATA = 400
HTTP_INVALID_AUTH_DATA = 401
HTTP_NOT_AUTHENTICATED = 403
HTTP_NOT_FOUND = 404
HTTP_ALREADY_REGISTERED = 409
HTTP_INTERNAL_ERROR = 500
HTTP_OK = 200


@app.route('/')
def home():
    return "Это начальная страница API, а не сайт. Вiйди отсюда!"


@app.route("/eig", methods=["POST"])
def eig():
    try:
        requestJson = request.get_json()
        matrix = requestJson['matrix']
    except:
        return make_response("Не удалось сериализовать json", HTTP_INVALID_DATA)

    return make_response(jsonify(np.linalg.eig(matrix)))


@app.route("/svd", methods=["POST"])
def svd():
    try:
        requestJson = request.get_json()
        matrix = requestJson['matrix']
    except:
        return make_response("Не удалось сериализовать json", HTTP_INVALID_DATA)

    return make_response(jsonify(np_linalg.svd(matrix, full_matrices=True)))


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', config['api_port'])))
