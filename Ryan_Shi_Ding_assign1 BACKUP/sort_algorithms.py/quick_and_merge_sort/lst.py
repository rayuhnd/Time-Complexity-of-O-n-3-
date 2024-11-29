from merge_sort import merge_sort
from quick_sort import quick_sort
import random as r
import time


def lists_quick(): #List for log-log
    sizes = []
    times = []
    repeat = 5

    print("test")

    for sz in range(1000, 20000, 500):
        sizes.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(1, 1000) for _ in range(sz)]
            before = time.perf_counter()  # Start timer
            quick_sort(lst)  # Call function
            total_time += time.perf_counter() - before
        average_time = total_time / repeat
        times.append(average_time)  # Save average time

    return sizes, times

def lists_merge(): #List for log-log
    sizes1 = []
    times1 = []
    repeat = 5

    print("test")

    for sz in range(1000, 20000, 500):
        sizes1.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(1, 1000) for _ in range(sz)]
            before = time.perf_counter()  # Start timer
            merge_sort(lst)  # Call function
            total_time += time.perf_counter() - before
        average_time = total_time / repeat
        times1.append(average_time)  # Save average time

    return sizes1, times1