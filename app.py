import subprocess
from typing import List # Solo necesario si usas Python < 3.9
import time
diccionario_vozes = {
    "Lincoln:" : "diego",
    "lincoln:" : "diego",
    "clyde:" : "American Spanish male voice :: Carlos 44100 L",
    "Clyde:" : "American Spanish male voice :: Carlos 44100 L",
    "John pork:" : "juan",
    "john pork:" : "juan",
    "default" : "jorge",
    "Lori:" : "Castilian Spanish female voice :: Carmen 44100 L",
    "lori:" : "Castilian Spanish female voice :: Carmen 44100 L",
    "lana:": "American Spanish female voice :: Soledad 44100 L",
    "Lana:" : "American Spanish female voice :: Soledad 44100 L"
}

def ejecutar_balabolka(voice: str, text: str, file: str):
    # Establecer los argumentos del comando de Balabolka
    args = ["balcon", "-n", voice, "-t", text, "-w", file]

    # Lanzar el subproceso y esperar a que termine
    #subprocess.run(args)
    p = subprocess.Popen(args)
    return p
def ejecutar_balabolka_solocore(voice: str, text: str, file: str):
    # Establecer los argumentos del comando de Balabolka
    args = ["balcon", "-n", voice, "-t", text, "-w", file]

    # Lanzar el subproceso y esperar a que termine
    #subprocess.run(args)
    subprocess.run(args)
    print("se ha echo el audio {} con la voz {} en el archivo {}".format(text,voice,file))
# Llamar a la función con algunos valores de ejemplo

def wait(processes: List[subprocess.Popen]):
    running = True
    while running:
        all_end = True # Asumir que todos los procesos han terminado
        for process in processes:
            if process.poll() is None: # Si algún proceso aún se está ejecutando
                all_end = False # Cambiar el valor de all_end a False
                break # Salir del bucle for
        if all_end: # Si todos los procesos han terminado
            running = False # Cambiar el valor de running a False para salir del bucle while
        time.sleep(0.01) # Hacer una pausa de 200 milisegundos
    return [p.returncode for p in processes] # Devolver una lista con los códigos de salida 
def obtenerDialogos():
    """
    esta linea obtiene todos los dialogos del archivo
    """
    archivo = open("historia.txt","r",encoding="utf8")
    texto = archivo.read()
    archivo.close()
    lista =  texto.split("\n")
    return lista


def main():
    Dialogos = obtenerDialogos()
    Procesos = []
    Procesos.append(ejecutar_balabolka("Sabina", "Audio de ejemplo no se tu"*200, ".\out\e.mp3"))
    start = time.time()
    for i in range(len(Dialogos)):
        # Procesos.append(ejecutar_balabolka("jorge", "Hola, este esta embrujado y espero que este bien", ".\out\ejemplo_"+ str(i)+ ".mp3"))


        #esta linea de codigo por el prefijo asigna la voz por defecto sera jorge
        Voz = diccionario_vozes["default"] 
        prefijo = "" 
        for pre in diccionario_vozes:
            if(Dialogos[i].startswith(pre)):
                Voz = diccionario_vozes[pre]
                prefijo = pre
                break
        if(Dialogos[i] != "\n" and Dialogos[i]!= ""):
            #esta linea elimina el prefijo
            ejecutar_balabolka_solocore(Voz, "{}".format(Dialogos[i].replace(prefijo,"")), ".\out\ejemplo{:03}.wav".format(i))
        
    lista = wait(Procesos)
    end = time.time()
    duration = end - start # Tiempo que tarda cada ejecución
    print("duracion en segundos: " ,duration,"audios: ", len(Dialogos)) # Número de ejecuciones por segundo
    

if __name__ == "__main__":
    main()