import pyaudio
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

    def recode(self, output_file_name=""):
        print(self.channels)
        stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            input_device_index=0,
            frames_per_buffer=self.chunk
        )

        print("::start::")
        frames = []
        for i in range(self.rate, self.chunk, self.record_time):
            data = stream.read(self.chunk)
            frames.append(data)

        print("::finish::")
        stream.stop_stream()
        stream.close()
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
        wf.writeframes(b''.join(frames))
        wf.close()
