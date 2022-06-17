import numpy as np
import pyaudio
from time import time

NOTA_MIN = 40       
NOTA_MAX = 64       
FSAMP = 22050       
FRAME_SIZE = 2048   
FRAMES_PER_FFT = 16

varPub = 10
numeroMIDI, frecHz, notaProxima, distNotaProxima = 0, 0, 0, 0

SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = float(FSAMP) / SAMPLES_PER_FFT