import sys
import numpy as np
import sounddevice as sd
import math
import time
import sounddevice as sd


# Konfiguration
SAMPLE_RATE = 44100
BUFFER_SIZE = 1024
CHANNELS = 2  # stereo
sd.default.device = 'pipewire'

device_name = "pipewire"
try:
    device_id = sd.query_devices(device_name)['index']
    stream = sd.InputStream(
        device=device_id,
        channels=CHANNELS,
        samplerate=SAMPLE_RATE,
        blocksize=BUFFER_SIZE,
        dtype='int16'
    )
    stream.start()
except Exception as e:
    #print(f"Gerät '{device_name}' not found.")
    sys.exit(1)
# Input-Stream öffnen
try:
    stream = sd.InputStream(
        channels=CHANNELS,
        samplerate=SAMPLE_RATE,
        blocksize=BUFFER_SIZE,
        dtype='int16'
    )
    stream.start()
except Exception as e:
    sys.exit(1)

def calculate_levels(data):
    data = np.frombuffer(data, dtype=np.int16)
    if len(data) < 2:
        return 0, 0

    left = data[::2]
    right = data[1::2]

    def level(channel_data):
        amplitude = np.abs(channel_data).max() / 32767
        dBFS = 20 * math.log10(amplitude + 1e-10)
        return max(0, int(60 + dBFS))

    return level(left), level(right)

while True:
    audio_data, _ = stream.read(BUFFER_SIZE)
    LevelL, LevelR = calculate_levels(audio_data)

    #print(f"L:{LevelL} R:{LevelR}")