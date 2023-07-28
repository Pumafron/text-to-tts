from flask import Blueprint,jsonify
import subprocess

urls6_blueprint = Blueprint('getVoicesAvalaible', __name__,)
@urls6_blueprint.route('/')
def getvoices():
    process = subprocess.Popen(['balcon','-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = process.communicate()[0]
    processed = out.decode("u8").replace("\r","").replace("  ","").split("\n")
    dicc = {
        "None":[],
        "SAPI 4:":[],
        "SAPI 5:":[]
    }
    actualValue = "None"
    for i in processed:
        if(i == "SAPI 4:" or i == "SAPI 5:"):
            actualValue = i
            continue
        dicc[actualValue].append(i)

    del dicc['None']
    return jsonify(dicc)