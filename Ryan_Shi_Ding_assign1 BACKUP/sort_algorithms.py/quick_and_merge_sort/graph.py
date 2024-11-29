import math
import matplotlib.pyplot as plt
from lst import lists_quick, lists_merge

sizes, times = lists_quick() 
sizes1, times1 = lists_merge() 

plt.scatter(sizes, times, marker ="x", label ="quick")
plt.scatter(sizes1, times1, marker = "1", label ="merge")
plt.ylabel("Average time of 5 runs with random lists")
plt.xlabel("List sizes in range 1000 to 5500")
plt.title("Running times for n*log(n) algorithms")
plt.legend()
plt.tight_layout()
plt.show()  