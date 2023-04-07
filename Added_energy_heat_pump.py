import matplotlib.pyplot as plt
import csv
import numpy as np


# Init lists and variables
document = 'anton.txt'
result = []
time = []
energy = []
f = open(document, 'r')
i = 0

# Read every line and append to list
for line in f.readlines():
    result.append(line)

# Access the actual data and put the data into lists 
for line in result:
    for data in line.split():
        
        if i == 0:
            time.append(float(data)/60)

        if i == 4:
            energy.append(float(data))
        i+=1
    i = 0
    
# Wonky last value
time.pop()

# Initialize plot
fig, ax = plt.subplots()
plt.grid(True)
ax.plot(time, energy, linewidth=2.0, color='red', label="Added Energy (J)")


# Linear approximation of first degree
b2, a2 = np.polyfit(time, energy, 1)
y1 = []
y2 = []

# Make list with values of the linear approximation
for x in time:
    y2.append(a2 + b2*x)

# Plot the actual data and add legend and labels
ax.plot(time, y2, linewidth=2.0, label= "y = " + str(int(round(a2, -3))) + " + " + str(int(round(b2, -3)))+ "x")
plt.ylabel("Energy (J)")
plt.xlabel("Time (60s)")
ax.legend(loc='upper left')
plt.show()

