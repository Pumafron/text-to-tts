from flask import Flask,render_template,request,jsonify,send_file
from lib import Voz,timeis
import json
import subprocess
from typing import List # Solo necesario si usas Python < 3.9
import os, zipfile
import time

#el prefijo usa voces, pero el audio o voz pronto se pondra en clases para detallar los acentos y el tipo de loquendo que es

app = Flask(__name__)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))
def borrar_archivos_directorio(directorio):
    try:
        # Obtener la lista de archivos en el directorio
        archivos = os.listdir(directorio)

        # Iterar sobre cada archivo y borrarlo
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)
                print(f"Archivo eliminado: {ruta_archivo}")
            else:
                print(f"Saltando directorio: {ruta_archivo}")

        print("Todos los archivos han sido eliminados del directorio.")
    except Exception as e:
        print(f"Error al borrar archivos: {e}")
            
def ejecutar_balabolka_solocore(voice: Voz, text: str, file: str):
    args = "balcon -p {} -s {} -n \"{}\" -t \"{}\" -w {}".format(voice.pitch,voice.rate,voice.voz,text,file)
    subprocess.run(args)
    print("se ha echo el audio {} con la voz {} en el archivo {}".format(text,voice.voz,file))

def obtenerDialogos_fromArray(texto):
    lista = texto.split("\n")
    return lista
def obtenerDialogos():
    """
    esta linea obtiene todos los dialogos del archivo
    """
    archivo = open("historia.txt","r",encoding="utf8")
    texto = archivo.read()
    archivo.close()
    lista =  texto.split("\n")
    return lista

def loadVoices():
    list_of_voices = []
    with open('voices.json') as json_file:
        voices : dict = json.load(json_file)
        for i in voices.keys():
            voz = voices[i]
            list_of_voices.append( Voz(voz["voice"],prefix=voz["prefix"],pitch=voz["pitch"],rate=voz["rate"]) )
    return list_of_voices

# @lib.timeis
def procesarAudios(Dialogos):   
    voice_list : List[Voz] = loadVoices() 
    default = Voz("jorge",0,0,"default")

    for i in range(len(Dialogos)):
        selected_voice = default
        prefijo = "" 
        for voice in voice_list:
            if(Dialogos[i].startswith(voice.prefix)):
                
                selected_voice = voice
                break
        if(Dialogos[i] != "\n" and Dialogos[i]!= ""):
            #esta linea elimina el prefijo
            ejecutar_balabolka_solocore(selected_voice, "{}.".format(Dialogos[i].replace(selected_voice.prefix,"")), "./out/"+"fix{:04}.wav".format(i))

def procesarAudios2(Dialogos):   
    voice_list : List[Voz] = loadVoices() 
    default = Voz("jorge",0,0,"default")

    for i in range(len(Dialogos)):
        selected_voice = default
        prefijo = "" 
        for voice in voice_list:
            if(Dialogos[i].startswith(voice.prefix)):
                
                selected_voice = voice
                break
        if(Dialogos[i] != "\n" and Dialogos[i]!= ""):
            #esta linea elimina el prefijo
            ejecutar_balabolka_solocore(selected_voice, "{}.".format(Dialogos[i].replace(selected_voice.prefix,"")), "./out/"+"fix{:04}.wav".format(i))


@app.route("/clasicGenerate")
def main():
    
    Dialogos = obtenerDialogos()
    procesarAudios(Dialogos)
    return "do"

@app.route("/")
def index():
    # Devolver "Hola mundo" como respuesta
    return render_template('index.html')

@app.route('/getAudios', methods=['GET'])
def getAudioszip():
    workspace = "out/"
    with zipfile.ZipFile('tmp/out.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(workspace, zipf)
    return send_file('tmp/out.zip')

@app.route('/generate', methods=['POST']) 
def foo():
    data = request.json

    directorio_a_borrar = "out/"
    borrar_archivos_directorio(directorio_a_borrar)
    if "contenttext" in data:
        dialogs = obtenerDialogos_fromArray(data["contenttext"])
        procesarAudios2(dialogs)

    return jsonify(data)

@app.route('/getVoices', methods=['GET']) 
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

@app.route('/getVoicesAvalaible', methods=['GET']) 
def getvoicesAvalaible():
     with open('voices.json') as json_file:
        voices : dict = json.load(json_file)
        return jsonify(voices)


if __name__ == "__main__":
    #main()
    app.run(debug = True)