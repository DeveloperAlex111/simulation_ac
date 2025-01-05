import numpy as np
import matplotlib.pyplot as plt

# Define the angle range(0 to 360 degrees)
angles = np.linspace(0, 360, 1000)

#Convert angles to radians
radians = np.deg2rad(angles)

#Calculate the AC voltage (V) using a sine wave function
voltage = 311 * np.sin(radians)

#Plot the chart
plt.plot(angles, voltage)
plt.title('AC Current chart')
plt.axhline(0, color='black', linewidth=1.1) # add x-axis line
plt.axvline(0, color='black', linewidth=1.1) # add y-axis line

# Add arrows to the axes 
plt.annotate('', xy=(360, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='black')) 
plt.annotate('', xy=(0, 220), xytext=(0, -1), arrowprops=dict(arrowstyle="->", color='black'))

plt.xlabel('Angles (degrees)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()