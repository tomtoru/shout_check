import pyaudio
import wave
import os
import numpy as np
import matplotlib.pyplot as plt


class Analyzer():
    def __init__(self, chunk, file_dir="./recode_data/"):
        self.chunk = chunk
        self.file_dir = file_dir

    def waveform(self, file_name):
        wf = wave.open(self.file_dir + file_name, 'r')

        amp = (256) ** wf.getsampwidth() / 2
        data = wf.readframes(self.chunk)
        data = np.frombuffer(data, 'int16')
        data = data / amp

        rate = wf.getframerate()
        size = float(self.chunk)
        x = np.arange(0, size/rate, 1.0/rate)

        plt.plot(x, data)
        plt.show()


