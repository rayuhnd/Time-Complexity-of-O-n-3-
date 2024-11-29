import time
from selection_sort import selection_sort
from insertion_sort import insertion
from bubble_sort import bubble_sort
import random as r

def lists_selection(): #List for log-log
    sizes = []
    times = []
    repeat = 5

    print("test")

    for sz in range(2000, 10000, 250):
        sizes.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(1, 1000) for _ in range(sz)]
            before = time.perf_counter()  # Start timer
            selection_sort(lst)  # Call function
            total_time += time.perf_counter() - before
        average_time = total_time / repeat
        times.append(average_time)  # Save average time

    return sizes, times

def lists_insertion():
    sizes1 = []
    times1 = []
    repeat = 5

    print("test")

    for sz in range(2000, 10000, 250):
        sizes1.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(1, 1000) for _ in range(sz)]
            before = time.perf_counter()  # Start timer
            insertion(lst)  # Call function
            total_time += time.perf_counter() - before
        average_time = total_time / repeat
        times1.append(average_time)  # Save average time

    return sizes1, times1

def lists_bubble():
    sizes2 = []
    times2 = []
    repeat = 5

    print("test")

    for sz in range(2000, 10000, 250):
        sizes2.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            # Generate random list of size sz
            lst = [r.randint(1, 1000) for _ in range(sz)]
            before = time.perf_counter()  # Start timer
            bubble_sort(lst)  # Call function
            total_time += time.perf_counter() - before
        average_time = total_time / repeat
        times2.append(average_time)  # Save average time

    return sizes2, times2
