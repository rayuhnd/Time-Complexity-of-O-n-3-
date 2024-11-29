import matplotlib.pyplot as plt
import time
import random as r
from bruteforce import threesum_v3


def experimentfunc():

    all_sizes = []
    all_times = []
    markers = ["x", "1", "+"]
    runs = 0

    for _ in range(3):  # Repeat 3 runs
        times = []
        sizes = []
        for sz in range(100, 601, 25):
            sizes.append(sz)  # Save size
            # Generate random list of size sz
            lst = [r.randint(-5, 5) for _ in range(sz)]
            before = time.time()  # Start timer
            threesum_v3(lst, sum=0)  # Call function
            times.append(time.time() - before)

        all_sizes.append(sizes)
        all_times.append(times)

        plt.plot(sizes, times, markers[runs], label=f"Run {runs + 1}")
        runs += 1

    plt.ylabel("Run times with random lists")
    plt.xlabel("List sizes in range 100 to 600")
    plt.title("3 Separate Runs for 3-Sum")
    plt.legend(["Run 1", "Run 2", "Run 3"])
    plt.tight_layout()
    plt.show()

    return all_sizes, all_times


experimentfunc()  # Calls function
