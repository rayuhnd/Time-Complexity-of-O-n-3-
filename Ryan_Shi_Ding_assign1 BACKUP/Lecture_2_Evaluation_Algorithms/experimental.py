import time
from bruteforce import threesum_v3
import random as r


def experimentfunc():
    sizes = []
    times = []
    repeat = 5

    print("test")

    for sz in range(100, 601, 25):
        sizes.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(-5, 5) for _ in range(sz)]
            before = time.time()  # Start timer
            threesum_v3(lst, sum=0)  # Call function
            total_time += time.time() - before
        average_time = total_time / repeat
        times.append(average_time)  # Save average time

    return sizes, times


experimentfunc()
