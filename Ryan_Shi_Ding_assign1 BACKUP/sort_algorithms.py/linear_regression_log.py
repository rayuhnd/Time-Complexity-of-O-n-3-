import math
import matplotlib.pyplot as plt
from lst_log import lists_selection, lists_insertion, lists_bubble

# Use evaluation functions to get sizes and times
sizes, times = lists_selection()
sizes1, times1 = lists_insertion()
sizes2, times2 = lists_bubble()

def logarithm(sizes, times):
    # Apply logarithmic transformation (base 2)
    x = [math.log(s, 2) for s in sizes]
    y = [math.log(t, 2) for t in times]

    # Linear regression calculations
    n = len(x)
    Sx = sum(x)
    Sy = sum(y)
    Sxx = sum(x[i]**2 for i in range(n))
    Sxy = sum(x[i] * y[i] for i in range(n))

    # Coefficients
    k = ((n * Sxy) - (Sx * Sy)) / ((n * Sxx) - (Sx ** 2))  # Slope of log-log plot
    m = ((Sxx * Sy) - (Sx * Sxy)) / ((n * Sxx) - (Sx ** 2))  # Intercept (unused here)

    return x, y, k

# Logarithmic transformation for selection sort
x, y, k_selection = logarithm(sizes, times)

# Logarithmic transformation for insertion sort
a, b, k_insertion = logarithm(sizes1, times1)

# Logarithmic transformation for bubble sort
c, d, k_bubble = logarithm(sizes2, times2)

# Plotting
plt.scatter(x, y, label=f"Selection Sort k = {round(k_selection, 3)}", marker="+")
plt.scatter(a, b, label=f"Insertion Sort k = {round(k_insertion, 3)}", marker="1")
plt.scatter(c, d, label=f"Insertion Sort k = {round(k_bubble, 3)}", marker="x")

# Add labels, title, and legend
plt.title("Log-log Plots for O(n^2) Algorithms")
plt.ylabel("log2 of sorting times")
plt.xlabel("log2 of list sizes")
plt.legend()
plt.tight_layout()
plt.show()
