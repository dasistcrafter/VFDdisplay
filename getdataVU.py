import numpy as np
import sounddevice as sd
import math
import time

def _calculate_levels(LevelL, LevelR, device_name='pipewire', buffer_size=1024, sample_rate=44100, channels=2):
    try:
        device_id = sd.query_devices(device_name)['index']
    except Exception as e:
        print(f"Device '{device_name}' not found: {e}")
        return

    try:
        stream = sd.InputStream(
            device=device_id,
            channels=channels,
            samplerate=sample_rate,
            blocksize=buffer_size,
            dtype='int16'
        )
        stream.start()
    except Exception as e:
        print(f"Failed to start stream: {e}")
        return

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

    try:
        while True:
            data, _ = stream.read(buffer_size)
            l, r = calculate_levels(data)
            LevelL[0] = l
            LevelR[0] = r
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop()
        stream.close()
