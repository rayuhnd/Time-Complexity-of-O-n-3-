def insertion(lst):
    n = len(lst)
    for i in range(1, n): 
        key = lst[i] 
        j = i - 1 

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key
    return lst
