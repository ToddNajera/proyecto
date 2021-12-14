"""
INSTITUTO POLITECNICO NACIONAL
ESCUELA SUPERIOR DE COMPUTO

Materia:Teoria de Comunicaciones Y Señaes
Profesor: Jaime Hugo Puebla


Alumnos:García Dojaquez Joel Nicolás, Obregón Corona Aldo Josué, Porras Nájera Miguel Ángel
Grupo: 3CV15

Sirve:
El programa se encarga de tomar 2 pistas de audio en formato WAV y
obtener la correlacion normalizada entre estas.
*probado con archivos WAV en codificacion pcm_16 (16 bits) *

Recibe dos cadenas de audio wav y valor K de retraso para la señal (1) 

Salidas:
-Grafica de las dos señales y valor de correlacion entre 0-1
-valor de la energia relacionada a la señal (autocorrelacion)
"""
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
from numpy import float64
from utilerias.clases import *

class GreetingFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("INSTITUTO POLITÉCNICO NACIONAL.")
        self.label.pack(pady=10)

        self.label = ttk.Label(self)
        self.label["text"] = ("ESCUELA SUPERIOR DE CÓMPUTO.")
        self.label.pack(pady=10)

        self.label = ttk.Label(self)
        self.label["text"] = ("TEORÍA DE COMUNICACIONES Y SEÑALES.")
        self.label.pack(pady=10)

        self.label = ttk.Label(self)
        self.label["text"] = ("PROYECTO: CORRELACIÓN CRUZADA.")
        self.label.pack(pady=10)

        self.label = ttk.Label(self)
        self.label["text"] = ("PRESENTAN:\n García Dojaquez Joel Nicolás\n Obregón Corona Aldo Josué\n Porras Nájera Miguel Ángel.")
        self.label.pack(pady=10)

        self.label = ttk.Label(self)
        self.label["text"] = ("Grupo: 3CV15.")
        self.label.pack(pady=10)

"""
------------------------------------------------------------------------------
Ventana de la autocorrelación
------------------------------------------------------------------------------
"""
class AutoCorrelacionFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Calcule la autocorrelación de una pista de audio.")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Seleccione la pista de audio.")
        self.label.pack(pady=10)
        
        self.file1_button = ttk.Button(self, text="Buscar pista",command=lambda:[self.openfile(),self.norm1()])
        self.file1_button.pack(pady=10)

        self.forum_button = ttk.Button(self, text="calcular",command=lambda:self.graf())
        self.forum_button.pack(side=tkinter.BOTTOM,pady=20)
    """
    ------------------------------------------------------------------------------
    Funciones de la autocorrelación
    ------------------------------------------------------------------------------
    """
    def openfile(self):
        self.filename = filedialog.askopenfilename(title="Open file")
    
    def norm1(self):
        self.muestreo1 , self.sonido1 = waves.read(self.filename)
        self.signalWAV1 = audio(self.sonido1,"audio 1")
        #self.signalWAV1 = audio([0,1,2,3,4,5,6,7,8,9],"lista")
        self.signalWAV1.normalizar()
        
    def graf(self):
        self.correlacion_norm , self.correlacion_signal = self.signalWAV1.autocorrelacion()
        tkinter.messagebox.showinfo("Resultados","Correlacion Normalizada " + str(self.correlacion_norm))
        print("Correlacion Normalizada " + str(self.correlacion_norm))
        pyplot.title('Correlación de Señales')
        pyplot.subplot(311)
        self.signalWAV1.plotear("g")
        pyplot.subplot(312)
        #self.signalWAV2.plotear("b")
        #pyplot.subplot(313)
        pyplot.plot(self.correlacion_signal,"m", label ='Correlacion')
        pyplot.legend()
        pyplot.show()
"""
------------------------------------------------------------------------------
Ventana de la correlación
------------------------------------------------------------------------------
"""
class CorrelacionFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Calcule la correlación de dos pistas de audio.")
        self.label.pack()

        self.label = ttk.Label(self)
        self.label["text"] = ("Seleccione las pistas de audio.")
        self.label.pack(pady=10)
        
        self.file1_button = ttk.Button(self, text="Buscar pista 1",command=lambda:[self.openfile(),self.norm1()])
        self.file1_button.pack(pady=10)

        self.file2_button = ttk.Button(self, text="Buscar pista 2",command=lambda:[self.openfile(),self.norm2()])
        self.file2_button.pack(pady=10)

        self.forum_button = ttk.Button(self, text="calcular",command=self.graf)
        self.forum_button.pack(side=tkinter.BOTTOM,pady=20)
    """
    ------------------------------------------------------------------------------
    Funciones de la correlación
    ------------------------------------------------------------------------------
    """
    #funcion para abrir un archivo y obtener el directorio 
    def openfile(self):
        self.filename = filedialog.askopenfilename(title="Open file")
    #funcion para normalizar la pista de audio
    def norm1(self):
        self.muestreo1 , self.sonido1 = waves.read(self.filename)
        self.signalWAV1 = audio(self.sonido1,"audio 1")
        self.signalWAV1.normalizar()
    
    def norm2(self):
        self.muestreo2 , self.sonido1 = waves.read(self.filename)
        self.signalWAV2 = audio(self.sonido1,"audio 2")
        self.signalWAV2.normalizar()
    #funcion para graficar    
    def graf(self):
        self.correlacion_norm , self.correlacion_signal = self.signalWAV1.correlacion_cruzada(self.signalWAV2,0)
        tkinter.messagebox.showinfo("Resultados","Correlacion Normalizada " + str(self.correlacion_norm))
        print("Correlacion Normalizada " + str(self.correlacion_norm))
        pyplot.title('Correlación de Señales')
        pyplot.subplot(311)
        self.signalWAV1.plotear("g")
        pyplot.subplot(312)
        self.signalWAV2.plotear("b")
        pyplot.subplot(313)
        pyplot.plot(self.correlacion_signal,"m", label ='Correlacion')
        pyplot.legend()
        pyplot.show()

"""
-----------------------------------------------------------------------
Ventana principal
---------------------------------------------------------------------
"""
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Proyecto correlación y autocorrelación")
        
        self.notebook = ttk.Notebook(self)
        #elementos del cuaderno (tabs)
        self.greeting_frame = GreetingFrame(self.notebook)
        self.notebook.add(
            self.greeting_frame, text="Inicio", padding=10)
        
        self.about_frame = AutoCorrelacionFrame(self.notebook)
        self.notebook.add(
            self.about_frame, text="Autocorrelación", padding=10)

        self.about_frame = CorrelacionFrame(self.notebook)
        self.notebook.add(
            self.about_frame, text="Correlación", padding=10)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()


