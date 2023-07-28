from flask import Blueprint,render_template,request,jsonify, send_file
import zipfile
from utils import zipdir

getAudios_blueprint = Blueprint('getAudios', __name__,)


@getAudios_blueprint.route('/',methods=['GET'])
def getAudioszip():
    workspace = "out/"
    with zipfile.ZipFile('tmp/out.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(workspace, zipf)
    return send_file('tmp/out.zip')