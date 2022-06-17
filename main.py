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

