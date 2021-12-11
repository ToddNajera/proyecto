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
import numpy as np
from time import sleep
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt


#Clase que usaremos para leer nuestro archivo de audio
class audio:
    
    def __init__(self, archivoWAV):
        self.canales = archivoWAV.shape
        if len(archivoWAV.shape) == 1 :
            self.canal = archivoWAV[:]
        else:
            self.canal = archivoWAV[:,len(archivoWAV.shape)]
