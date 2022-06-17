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

NOTE_NAMES = 'Mi Fa Fa# Sol Sol# La La# Si Do Do# Re Re#'.split()


def freq_to_number(f): return 64 + 12 * np.log2(f / 329.63)
def number_to_freq(n): return 329.63 * 2.0**((n - 64) / 12.0)
