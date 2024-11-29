import matplotlib.pyplot as plt
from experimental import experimentfunc

sizes, times = experimentfunc()

xpoints = sizes
ypoints = times

plt.plot(xpoints, ypoints, "x")
plt.ylabel("Average time of 5 runs with random lists")
plt.xlabel("List sizes in range 100 to 600")
plt.tight_layout()
plt.show()
