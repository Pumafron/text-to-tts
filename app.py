from lib import Voz,timeis
import json
import subprocess
from typing import List # Solo necesario si usas Python < 3.9
import time

#el prefijo usa voces, pero el audio o voz pronto se pondra en clases para detallar los acentos y el tipo de loquendo que es


def ejecutar_balabolka_solocore(voice: Voz, text: str, file: str):
    args = ["balcon", "-p",str(voice.pitch),"-s",str(voice.rate),"-n", voice.voz, "-t", text, "-w", file]
    subprocess.run(args)
    print("se ha echo el audio {} con la voz {} en el archivo {}".format(text,voice.voz,file))

 
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
            list_of_voices.append(Voz(voz["voice"],prefix=voz["prefix"]))
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
            ejecutar_balabolka_solocore(selected_voice, "{}".format(Dialogos[i].replace(selected_voice.prefix,"")), "./out/ejemplo{:04}.wav".format(i))


@timeis
def main():
    
    Dialogos = obtenerDialogos()
    procesarAudios(Dialogos)
    

if __name__ == "__main__":
    main()