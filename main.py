import numpy as np
import matplotlib.pyplot as plt


def generate_sine_wave(frequency=1, amplitude=1, duration=1, sampling_rate=100):
    """
    Generate a sine wave.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        amplitude (float): Amplitude of the sine wave.
        duration (float): Duration of the sine wave in seconds.
        sampling_rate (int): Number of samples per second.

    Returns:
        t (numpy.ndarray): Time points.
        y (numpy.ndarray): Sine wave values.
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time vector
    y = amplitude * np.sin(2 * np.pi * frequency * t)  # Sine wave formula
    return t, y


def plot_sine_wave(frequency=1, amplitude=1, duration=1, sampling_rate=100):
    """
    Plot a sine wave using the given parameters.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        amplitude (float): Amplitude of the sine wave.
        duration (float): Duration of the sine wave in seconds.
        sampling_rate (int): Number of samples per second.
    """
    t, y = generate_sine_wave(frequency, amplitude, duration, sampling_rate)

    # Plot the sine wave
    plt.figure(figsize=(10, 5))
    plt.plot(t, y, label=f'{frequency}Hz Sine Wave')
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()
    plt.show()


# Example usage
if __name__ == "__main__":
    # Generate and plot a sine wave with a frequency of 5Hz, amplitude of 1, and duration of 2 seconds
    plot_sine_wave(frequency=5, amplitude=1, duration=2, sampling_rate=500)
