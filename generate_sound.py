import numpy as np
import sounddevice as sd

# Parameters
frequency = 4186.01  # Frequency in Hz
duration = 2        # Duration in seconds
sample_rate = 44100 # Standard audio sampling rate

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave (C4)
tone = np.sin(2 * np.pi * frequency * t)

# Play the tone
sd.play(tone, sample_rate)
sd.wait()  # Wait until the sound finishes playing
