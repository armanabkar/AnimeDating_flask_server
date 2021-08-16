from flask import Flask, jsonify, current_app
from flask_cors import CORS, cross_origin
from data import suggestions, characters
import random

app = Flask(__name__, static_folder='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
urlPrefix = "/api/v1"

# auto reload
app.run(debug=True)


@app.route('/', methods=['GET'])
def welcome():
    return current_app.send_static_file('index.html')


@cross_origin()
@app.route(f'{urlPrefix}/suggestions', methods=['GET'])
def getSuggestions():
    random.shuffle(suggestions, random.random)
    return jsonify(suggestions)


@cross_origin()
@app.route(f'{urlPrefix}/characters', methods=['GET'])
def getCharacters():
    random.shuffle(characters, random.random)
    return jsonify(characters)
