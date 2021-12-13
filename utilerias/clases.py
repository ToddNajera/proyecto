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
        if len(archivoWAV.shape) == 1 :
            self.wave = archivoWAV[:]
        else:
            self.wave = archivoWAV[:,len(archivoWAV.shape)]
        self.amplitud = numpy.max(self.wave)
        self.longitud = len(self.wave)

    def normalizar(self):
        """
        Sirve para tomar el conjunto de datos y normalizar los valores entre 0 y 1 
        esto dividiendo todos nuestros elemetos entre la amplitud maxima de la señal
        """
        self.wave = self.wave / self.amplitud
        
    
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
        if self.longitud > signalWAV.longitud :

            correlacion_norm = 0
            correlacion_signal = numpy.zeros(signalWAV.longitud,dtype=numpy.float64)
            for n in enumerate(signalWAV.wave):
                correlacion_signal[n[0]] = (1/signalWAV.longitud) * numpy.sqrt(numpy.float_power(self.wave[n[0]+k],2) * numpy.float_power(signalWAV.wave[n[0]],2))
                correlacion_norm = correlacion_norm + (correlacion_signal[n[0]] / (1/signalWAV.longitud) * correlacion_signal[n[0]])
        else:
            correlacion_norm = 0
            correlacion_signal = numpy.zeros(self.longitud,dtype=numpy.float64)
            for n in enumerate(self.wave):
                correlacion_signal[n[0]] = (1/self.longitud) * numpy.sqrt(numpy.float_power(self.wave[n[0]],2) * numpy.float_power(signalWAV.wave[n[0]+k],2))
                correlacion_norm = correlacion_norm + (correlacion_signal[n[0]] / (1/signalWAV.longitud) * correlacion_signal[n[0]])

        return correlacion_norm , correlacion_signal

    def autocorrelacion(self):
        """
        La autocorrelacion es la correlacion cruzada hecha sobre la misma señal

        donde el valor que sevuelve la suma es 
        """
        autocorrelacion_norm = 0
        autocorrelacion_signal = numpy.zeros(self.longitud+1,dtype=numpy.float64)
        
        for n in enumerate(self.wave):
                autocorrelacion_signal[n[0]] = numpy.sqrt(numpy.float_power(self.wave[n[0]],2) * numpy.float_power(self.wave[n[0]],2))
                autocorrelacion_norm = autocorrelacion_norm + (autocorrelacion_signal[n[0]] / (1/self.longitud) * autocorrelacion_signal[n[0]])
        
        return autocorrelacion_norm , autocorrelacion_signal
