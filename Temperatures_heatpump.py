import matplotlib.pyplot as plt
import csv
import numpy as np

# Initialize variables and lists 
document = 'anton.txt'
result = []
time = []
y1 = []
y2 = []
temperature_a = []
temperature_b = []
i = 0
f = open(document, 'r')

# Read every line and append to list
for line in f.readlines():
    result.append(line)

# Access the actual data and put the data into lists 
for line in result:
    for data in line.split():
        
        if i == 0:
            time.append(float(data))
        if i == 1:
            temperature_a.append(float(data))
        if i == 2:
            temperature_b.append(float(data))

      
        i+=1
    i = 0

# Initialize plot 
fig, ax = plt.subplots()
plt.grid(True)


# Make list with values of tangents to the curve 
b1, a1 = np.polyfit(time[10:20], temperature_a[10:20], 1)
b2, a2 = np.polyfit(time[120:130], temperature_a[120:130], 1)

for x in time:
    y1.append(a1 + b1*x)
    y2.append(a2 + b2*x)


# Plot the linear approximation, the tangents and add legend and labels    
ax.plot(time, y1, linewidth=2.0, label= "Tangent initially: y = " + str(int(a1)) + " + " + str(round(b1, 3)) + "x")
ax.plot(time, y2, linewidth=2.0, label= "Tangent ending: y = " + str(int(a2)) + " + " + str(round(b2, 3)) + "x")
ax.plot(time, temperature_a, linewidth=2.0, color='red', label="Hot(C°)")
ax.plot(time, temperature_b, linewidth=2.0, label="Cold (C°)")
plt.ylabel("Temperature (C°)")
plt.xlabel("Time (seconds)")
ax.legend(loc='upper left')
plt.show()



    
