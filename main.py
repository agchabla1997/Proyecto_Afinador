import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic 
from PyQt5.QtCore import QByteArray
import time
import publicador

class Proceso(QObject): 
  def __init__(self):
        super(Proceso, self).__init__()
  def procesoPub(self):
        publicador.PublicaNota()

class Ventana(QMainWindow):
  def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi("disenofinal.ui", self)  

        self.hilo = QThread()
        self.proceso = Proceso()
        self.proceso.moveToThread(self.hilo)
        self.boton.clicked.connect(self.hilo.start)
        self.hilo.started.connect(self.proceso.procesoPub) 
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.actualizaVentana)
        self.timer.start()
   
  def actualizaVentana(self):
       
        pub_numeroMIDI =  "%.2f" % (publicador.numeroMIDI) 
        self.ResMidi.setText(str(pub_numeroMIDI)) 
        pub_frecHz =  "%.2f" % (publicador.frecHz)
        self.ResFrec.setText(str(pub_frecHz))
        self.ResNota.setText(str(publicador.notaProxima))                                    
        distNP = "%.2f" % (publicador.distNotaProxima)
        self.ResDist.setText(str(distNP))    
        self.verticalSlider.setValue((publicador.numeroMIDI)*10) 

