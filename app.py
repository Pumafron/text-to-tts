from flask import Flask
from flask_cors import CORS
from index import urls_blueprint
from getVoices import urls2_blueprint
from generate import generate_blueprint
from getAudios import getAudios_blueprint
from getAvalaibleVoices import urls6_blueprint

#el prefijo usa voces, pero el audio o voz pronto se pondra en clases para detallar los acentos y el tipo de loquendo que es

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(urls_blueprint)
app.register_blueprint(urls2_blueprint,url_prefix='/api/getVoices')
app.register_blueprint(generate_blueprint,url_prefix='/api/generate')
app.register_blueprint(getAudios_blueprint,url_prefix='/api/getAudios')
app.register_blueprint(urls6_blueprint,url_prefix='/api/getVoicesAvalaible')


if __name__ == "__main__":
    #main()
    app.run(debug = True)