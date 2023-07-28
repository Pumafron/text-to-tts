import json
from flask import Blueprint,jsonify

urls6_blueprint = Blueprint('getVoicesAvalaible', __name__,)
@urls6_blueprint.route('/')
def getvoicesAvalaible():
     with open('voices.json') as json_file:
        voices : dict = json.load(json_file)
        return jsonify(voices)