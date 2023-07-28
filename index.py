from flask import Blueprint,render_template

urls_blueprint = Blueprint('index', __name__,)


@urls_blueprint.route('/')
def index():
    # Devolver "Hola mundo" como respuesta
    return render_template('index.html')
