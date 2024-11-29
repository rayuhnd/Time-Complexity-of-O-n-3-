import time
import random as r
from selection_sort import selection_sort
from insertion_sort import insertion
from bubble_sort import bubble_sort

def evaluation_selection():
    print("Experiment")
    sizes = [] 
    times = []  
    repeat = 3  #3 runs

    for sz in range(2000, 10000, 250):
        sizes.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            lst = [r.randint(1, 1000) for _ in range(sz)]  # Generate random list of size sz
            before = time.perf_counter()  # Start timer
            selection_sort(lst)  # Call function
            total_time += time.perf_counter() - before  
        
        average_time = total_time / repeat  
        times.append(average_time)  # Save average time

    return sizes, times 

def evaluation_insertion():
    print("Experiment")
    sizes1 = [] 
    times1 = []  
    repeat = 3

    for sz in range(2000, 10000, 250):
        sizes1.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            lst = [r.randint(1, 1000) for _ in range(sz)]  # Generate random list of size sz
            before = time.perf_counter()  # Start timer
            insertion(lst)  # Call function
            total_time += time.perf_counter() - before  
        
        average_time = total_time / repeat  
        times1.append(average_time)  # Save average time

    return sizes1, times1

def evaluation_bubble():
    print("Experiment")
    sizes2 = [] 
    times2 = []  
    repeat = 3

    for sz in range(2000, 10000, 250):
        sizes2.append(sz)  # Save size
        total_time = 0
        for i in range(repeat):
            lst = [r.randint(1, 1000) for _ in range(sz)]  # Generate random list of size sz
            before = time.perf_counter()  # Start timer
            bubble_sort(lst)  # Call function
            total_time += time.perf_counter() - before  
        
        average_time = total_time / repeat  
        times2.append(average_time)  # Save average time

    return sizes2, times2