import sounddevice as sd
import numpy as np
from config import SAMPLE_RATE, CHUNK_SIZE

class NoiseSensor:
    def __init__(self):
        # Sounddevice ko open rakhne ki zarurat nahi, direct record karenge
        pass

    def get_db_level(self):
        # Mic se 1 chunk record karo
        recording = sd.rec(CHUNK_SIZE, samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()  # Record complete hone tak wait karo

        # RMS nikal ke dB mein convert karo
        rms = np.sqrt(np.mean(recording**2))
        if rms > 0:
            db = 20 * np.log10(rms)
        else:
            db = 0
        return round(db, 2)

    def close(self):
        # Kuch close karna nahi hai sounddevice mein
        pass
