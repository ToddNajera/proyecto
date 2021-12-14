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
*probado con archivos WAV en codificacion pcm_16 (16 bits) *

Recibe dos cadenas de audio wav y valor K de retraso para la señal (1) 

Salidas:
-Grafica de las dos señales y valor de correlacion entre 0-1
-valor de la energia relacionada a la señal (autocorrelacion)
"""
from numpy import float64
from utilerias.clases import *
#constantes para el programa
ruta_audios = os.path.dirname(os.path.abspath(__file__))+"/audios"
lista_audios = os.listdir(ruta_audios)
opcion =True

while(opcion):
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print("\t**********CORRELACION Y AUTOCORRELACION**********")
    print("La siguiente es una lista de las señales de audio disponibles para probar \n Seleccione el cual desea probar:")
    
    for op,audios in enumerate(lista_audios,start=1):
        print("{0} - {1}".format(op,audios))

    print ("0 - salir")
    opcion = input("inserte un valor numerico >>")

    if opcion !='0': 
        #Creamos nuestra primera señal de audio
        muestreo1 , sonido1 = waves.read(ruta_audios+"/"+lista_audios[int(opcion)-1])
        signalWAV1 = audio(sonido1,lista_audios[int(opcion)-1])
        signalWAV1.normalizar()

        #Seleccion de Señales para Correlacion Cruzada
        print("La siguiente es una lista de las señales de audio disponibles para realizar la correlacion\n (si selecciona el mismo audio, generara la auto correlacion) \n Seleccione el cual desea probar:")
    
        for op,audios in enumerate(lista_audios,start=1):
            print("{0} - {1}".format(op,audios))

        print ("0 - salir")
        op_corr = input("inserte un valor numerico >>")

        #Creamos nuestra primera señal de audio
        muestreo2 , sonido2 = waves.read(ruta_audios+"/"+lista_audios[int(op_corr)-1])
        signalWAV2 = audio(sonido2,lista_audios[int(op_corr)-1])
        signalWAV2.normalizar()

        #Proceso de Correlacion
        #correlacion = signalWAV1.correlacion(signalWAV2.wave)

        #Inicia Proceso de Ploteo de las Señales
        """pyplot.title('Correlación de Señales')
        pyplot.subplot(311)
        signalWAV1.plotear("g")
        pyplot.subplot(312)
        signalWAV2.plotear("b")
        pyplot.subplot(313)
        pyplot.plot(correlacion,"m", label ='Correlacion')
        pyplot.legend()
        pyplot.show()
        """
        
        #correlacion_norm , correlacion_signal = signalWAV1.correlacion_cruzada(signalWAV2,0)
        correlacion_norm , correlacion_signal = signalWAV1.autocorrelacion()
        print(signalWAV1)


        print("Correlacion Normalizada " + str(correlacion_norm))
        pyplot.title('Correlación de Señales')
        pyplot.subplot(311)
        signalWAV1.plotear("g")
        pyplot.subplot(312)
        signalWAV2.plotear("b")
        pyplot.subplot(313)
        pyplot.plot(correlacion_signal,"m", label ='Correlacion')
        pyplot.legend()
        pyplot.show()

        break
        
    elif opcion == '0': 
      break
    else: 
        print("Opcion desconocida :( ")
        sleep(1)