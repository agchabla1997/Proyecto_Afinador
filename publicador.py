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

def note_name(n):
    return NOTE_NAMES[n % NOTE_MIN % len(NOTE_NAMES)] + str(int(n / 12 - 1))
def note_to_fftbin(n): return number_to_freq(n) / FREQ_STEP

imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN - 1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX + 1))))
buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
num_frames = 0

# Initialize audio
stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)  #PEND: este de la frecuencia de transmision??????

stream.start_stream()
window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, SAMPLES_PER_FFT, False)))
print('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')
