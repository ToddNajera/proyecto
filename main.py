"""
INSTITUTO POLITECNICO NACIONAL
ESCUELA SUPERIOR DE COMPUTO

Materia:Teoria de Comunicaciones Y Señaes
Profesor: Jaime Hugo Puebla


Alumno:Porras Najera Miguel Angel
Boleta:2017613251

Sirve:
El programa se encarga de tomar 2 pistas de audio en formato WAV y
 obtener la correlacion normalizada entre estas.

Recibe dos cadenas de audio wav y valor K de retraso para la señal (1) 

Salidas:
-Grafica de las dos señales y valor de correlacion entre 0-1
-valor de la energia relacionada a la señal (autocorrelacion)
"""
from utilerias.clases import *
#constantes para el programa
ruta_audios = os.path.dirname(os.path.abspath(__file__))+"\\audios"
lista_audios = os.listdir(ruta_audios)
opcion =True

while(opcion):
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print("\t**********CORRELACION Y AUTOCORRELACION**********")
    print("La siguiente es una lista de las señales de audio disponibles para probar \n Seleccione el cual desea probar:")
    
    for op,automata in enumerate(lista_audios,start=1):
        print("{0} - {1}".format(op,automata))

    print ("0 - salir")
    opcion = input("inserte un valor numerico >>")

    if opcion !='0': 
        muestreo , sonido = waves.read(ruta_audios+"\\"+lista_audios[int(opcion)-1])
        señalWAV = audio(sonido)
        
    elif opcion == '0': 
      break
    else: 
        print("Opcion desconocida :( ")
        sleep(1)