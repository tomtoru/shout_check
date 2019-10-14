import pyaudio
import numpy as np
import wave
import datetime
import os


class Recoder():
    def __init__(self, channels=1, rate=44100, chunk=1024, record_time=30):
        self.channels = channels
        self.format = pyaudio.paInt16
        self.rate = rate
        self.chunk = chunk
        self.record_time = record_time
        self.audio = pyaudio.PyAudio()
        self.recode_dir = './recode_data/'
        self.stream = ""

    def recode(self, output_file_name=""):
        self.open_stream()
        print("::start::")
        frames = []
        for i in range(0, int(self.rate / self.chunk * self.record_time)):
            data = self.stream.read(self.chunk)
            frames.append(data)

        print("::finish::")
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        if not os.path.isdir(self.recode_dir):
            os.makedirs(self.recode_dir)

        if output_file_name == "":
            output_name = self.recode_dir + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_record.wav"
        else:
            output_name = self.recode_dir + output_file_name

        wf = wave.open(output_name, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b"".join(frames))
        wf.close()

    def auto_recode(self, threhold=0.05, output_file_name=""):
        while True:
            self.open_stream()
            data = self.stream.read(self.chunk)
            x = np.frombuffer(data, dtype="int16") / 32768.0

            if x.max() > threhold:
                if output_file_name == "":
                    file_name = self.recode_dir + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_autorecord.wav"
                else:
                    file_name = self.get_name_without_overwriting(output_file_name)

                frames = []
                frames.append(data)

                for i in range(0, int(self.rate / self.chunk * self.record_time)):
                    data = self.stream.read(self.chunk)
                    frames.append(data)

                wf = wave.open(file_name, 'wb')
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.audio.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(b"".join(frames))
                wf.close()
                break

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def open_stream(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            input_device_index=0,
            frames_per_buffer=self.chunk
        )

    def get_name_without_overwriting(self, file_name):
        # prevention to overwrite file
        if os.path.isfile(self.recode_dir + file_name):
            return self.get_name_without_overwriting(file_name + "_")
        else:
            return self.recode_dir + file_name
