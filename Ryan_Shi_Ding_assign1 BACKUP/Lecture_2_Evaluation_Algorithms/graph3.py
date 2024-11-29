import matplotlib.pyplot as plt
from experimental import experimentfunc
import math

# Get sizes and times from the experimental function
sizes, times = experimentfunc()

# Apply logarithmic transformation (base 3)
x = [math.log(s, 3) for s in sizes]
y = [math.log(t, 3) for t in times]

# Linear regression calculations
n = len(x)
Sx = sum(x)
Sy = sum(y)
Sxx = sum(x[i]**2 for i in range(n))
Sxy = sum(x[i] * y[i] for i in range(n))

# Coefficients
k = ((n * Sxy) - (Sx * Sy)) / ((n * Sxx) - (Sx ** 2))
m = ((Sxx * Sy) - (Sx * Sxy)) / ((n * Sxx) - (Sx ** 2))

# Predicted values
ypredict = [k * xi + m for xi in x]

# Plotting
plt.scatter(x, y, marker="+")
plt.plot(x, ypredict)
plt.ylabel("log3 of run times")
plt.xlabel("log3 of list sizes")
plt.legend(["y = a + b*x", "log(x) vs log(y)"])
plt.tight_layout()
plt.show()

print("Estimated coefficient:", k)
