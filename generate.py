from flask import Blueprint, jsonify,request
import json

from utils import borrar_archivos_directorio, obtenerDialogos_fromArray, procesarAudios2

generate_blueprint = Blueprint('generate', __name__,)


@generate_blueprint.route('/',methods=['POST'])
def generate():
    data = request.json
    directorio_a_borrar = "out/"
    borrar_archivos_directorio(directorio_a_borrar)
    if "contenttext" in data:
        dialogs = obtenerDialogos_fromArray(data["contenttext"])
        procesarAudios2(dialogs)

    return jsonify(data)