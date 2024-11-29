def threesum_v3(lst, sum=0):
    
    unique_triplets = set()
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == sum:
                    triplet = [lst[i], lst[j], lst[k]]
                    triplet.sort()
                    unique_triplets.add(tuple(triplet))
    return list(unique_triplets)
