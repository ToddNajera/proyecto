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
from numpy.core.numeric import correlate
import scipy.io.wavfile as waves
import matplotlib.pyplot as pyplot


#Clase que usaremos para leer nuestro archivo de audio
class audio:
    
    def __init__(self, archivoWAV,name):
        """
        Constructor de la clase
        """
        self.name = name
        self.wave = archivoWAV
        self.amplitud = numpy.max(self.wave)
        self.longitud = len(self.wave)
    
    def __str__(self):
        """
        Funcion para imprension en pantalla de la señal
        """
        return str(self.name)+"-"+str(self.wave)+"-"+str(self.amplitud)+"-"+str(self.longitud) 

    def normalizar(self):
        """
        Sirve para tomar el conjunto de datos y normalizar los valores entre 0 y 1 
        esto dividiendo todos nuestros elemetos entre la amplitud maxima de la señal
        """
        self.norm = numpy.linalg.norm(self.wave)
        self.wave = self.wave / self.norm

    
    def plotear(self,color):
        """
        Sirve para mostrar una grafica de la señal
        de audio obtenida del archivo WAV

        *uso de pyplot*
        """
        pyplot.plot(self.wave,color, label = 'Señal '+self.name)
        pyplot.legend()
    

    def correlacion(self, signalWAV):
        """
        Sirve para realizar la correlacion con una señal (signalWAV)

        *se utiliza el mode = same 
        *por si se tiene una señal con mayor longitud el proceso solo se realice con el segmento correspodiente
        corresponde a la operacion
        la suma de los productos punto a punto de cada señal, la funcion respeta la manera C12 = signal1[n] * signal2[n+1]
        """
        correlacion = numpy.correlate(self.wave,signalWAV,mode="same")
        return correlacion

    def correlacion_cruzada(self, signalWAV,k):
        """
        Sirve para realizar la correlacion con una señal (signalWAV)
        recibe un k que es el retraso que se le otorga a la seguna señal

        Depende de las señales se realiza la correlacion hasta la señal mas corta

        regresa correlacion nomalizada  y señal resultante
        """
        #la correlacion se acota a la señal mas corta
        k = int (k)
        correlacion_norm = 0
        correlacion_signal = numpy.zeros(signalWAV.longitud,dtype=numpy.float64)
        relleno = numpy.zeros(k,dtype=numpy.float64)
        self.wave = numpy.concatenate((self.wave,relleno),axis=0)
        if signalWAV.longitud > self.longitud:

            for index in range(self.longitud):
                correlacion_signal[index] = self.wave[index+k] * signalWAV.wave[index]
                correlacion_norm = correlacion_norm + correlacion_signal[index] 
        else:
            for index in range(signalWAV.longitud):
                correlacion_signal[index] = self.wave[index+k] * signalWAV.wave[index]
                correlacion_norm = correlacion_norm + correlacion_signal[index] 

        return correlacion_norm , correlacion_signal

    def autocorrelacion(self,k):
        """
        La autocorrelacion es la correlacion cruzada hecha sobre la misma señal

        donde el valor que sevuelve la suma es 
        """
        k = int (k)
        autocorrelacion_norm = 0
        autocorrelacion_signal = numpy.zeros(self.longitud+1,dtype=numpy.float64)
        relleno = numpy.zeros(k,dtype=numpy.float64)
        self.wave = numpy.concatenate((self.wave,relleno),axis=0)
        
        for index in range(self.longitud):
            autocorrelacion_signal[index] = self.wave[index+k] * self.wave[index]
            autocorrelacion_norm = autocorrelacion_norm + autocorrelacion_signal[index] 
        
        return autocorrelacion_norm , autocorrelacion_signal
