"""
Proyecto Teoria de Comunicacion y Señales 
Correacion Cruzada y AutoCorrelacion
Author: Miguel Angel Porras Najera

Sirve:
El programa se encarga de tomar 2 pistas de audio en formato WAV y
 obtener la correlacion normalizada entre estas.

Recibe dos cadenas de audio wav y valor K de retraso para la señal (1) 

Salidas:
-Grafica de las dos señales y valor de correlacion entre 0-1
-valor de la energia relacionada a la señal (autocorrelacion)
"""
#Librerias usadas
import os
import numpy
from time import sleep
import scipy.io.wavfile as waves
import matplotlib.pyplot as pyplot


#Clase que usaremos para leer nuestro archivo de audio
class audio:
    
    def __init__(self, archivoWAV):
        """
        Constructor de la clase
        """
        self.canales = archivoWAV.shape
        if len(archivoWAV.shape) == 1 :
            self.canal = archivoWAV[:]
        else:
            self.canal = archivoWAV[:,len(archivoWAV.shape)]

    def normalizar(self):
        """
        Sirve para tomar el conjunto de datos y normalizar los valores entre 0 y 1 
        esto dividiendo todos nuestros elemetos entre la amplitud maxima de la señal
        """
        amplitud = numpy.max(self.canal)
        self.canal = self.canal / amplitud
        
    
    def plotear(self):
        """
        Sirve para mostrar una grafica de la señal
        de audio obtenida del archivo WAV

        *uso de pyplot*
        """
        pyplot.figure(1)
        pyplot.title("signal 1")
        pyplot.plot(self.canal)
        pyplot.show()
    

    def correlacion(self, signalWAV, k):
        """
        Sirve para realizar la correlacion con una señal (signalWAV)
        recibe un k que es el retraso que se le otorga a la seguna senal
        """
        pass