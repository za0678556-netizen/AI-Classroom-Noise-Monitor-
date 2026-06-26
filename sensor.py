# sensor.py
import pyaudio
import numpy as np
from config import SAMPLE_RATE, CHUNK_SIZE

class NoiseSensor:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE
        )

    def get_db_level(self):
        data = np.frombuffer(self.stream.read(CHUNK_SIZE), dtype=np.int16)
        rms = np.sqrt(np.mean(data**2))
        if rms == 0:
            return 0
        db = 20 * np.log10(rms)
        return round(db, 2)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
