import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the angle range (0 to 360 degrees)
angles = np.linspace(0, 720, 2000)

# Convert angles to radians
radians = np.deg2rad(angles)

# Define the frequency (in Hz)
frequency = 1
Vpk = 311.15 # Voltage of the wave peak. Is the peak voltage of the AC signal.

Vrms = Vpk / np.sqrt(2) #  Root Mean Square Voltage. It's a way to express the effective value of an alternating current (AC) voltage

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.axhline(0, color='black', linewidth=0.5)  # Add x-axis line
ax.axvline(0, color='black', linewidth=0.5)  # Add y-axis line
ax.annotate('', xy=(720, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color='black'))
ax.annotate('', xy=(0, Vpk), xytext=(0, -Vpk),
             arrowprops=dict(arrowstyle="->", color='black'))
ax.set_xlim(0, 720)
ax.set_ylim(-Vpk, Vpk)
ax.set_xlabel('Angle (degrees)')
ax.set_ylabel('Voltage (V)')
ax.set_title(f'AC Current Chart with {frequency} Hz Frequency')

# Add lines for Vrms 
ax.axhline(Vrms, color='red', linestyle='--', linewidth=1.5, label=f'Vrms = {Vrms:.2f} V') 
ax.axhline(-Vrms, color='red', linestyle='--', linewidth=1.5)

# Add labels for Vrms lines 
ax.text(370, Vrms, f'Vrms = {Vrms:.1f} V', color='red', va='bottom') 
ax.text(370, -Vrms, f'Vrms = {Vrms:.1f} V', color='red', va='bottom')

# Initialize the plot
def init():
    line.set_data([], [])
    return line,

# Update the plot for each frame
def update(frame):
    voltage = Vpk * np.sin(radians + 2 * np.pi * frequency * frame / 100)
    line.set_data(angles, voltage)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=5000, init_func=init, blit=True, interval=5)

plt.grid(True)
plt.show()
