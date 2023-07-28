import subprocess
from typing import List # Solo necesario si usas Python < 3.9
from lib import Voz
import os, json
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
