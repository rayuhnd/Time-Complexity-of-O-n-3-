from lst_evaluation import evaluation_selection, evaluation_insertion, evaluation_bubble
import math
import matplotlib.pyplot as plt

sizes, times = evaluation_selection() 
sizes1, times1 = evaluation_insertion() 
sizes2, times2 = evaluation_bubble()

plt.scatter(sizes, times, marker ="x", label ="selection")
plt.scatter(sizes1, times1, marker = "1", label ="insertion")
plt.scatter(sizes2, times2, marker = "+", label ="bubble    ")
plt.ylabel("Average time of 3 runs with random lists")
plt.xlabel("List sizes in range 1000 to 5500")
plt.title("Running times for O(n^2) algorithms")
plt.legend()
plt.tight_layout()
plt.show()  