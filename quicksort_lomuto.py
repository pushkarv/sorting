import numpy as np
import time

def quicksort_lomuto(A, lo, hi):
    # print(f"lo = {lo}, hi = {hi}")
    if lo < hi:
        p = partition_lomuto(A,lo,hi)
        # print(f"partition = {p}")
        if (p > 0):
            quicksort_lomuto(A,lo,p-1)
        quicksort_lomuto(A, p+1, hi)

def partition_lomuto(A, lo, hi):
    # print("***START ***")
    tmp = 0
    pivot = A[hi]
    i = lo
    # print(f"pivot = {pivot}, i = {i}")
    for j in range(lo,hi+1):
        if A[j] < pivot:
            #swap A[i] & A[j]
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            # print(f"Swapped {A[i]} and {A[j]}")
            # print(A)
            i += 1
            # print(f"i = {i}")
    tmp = A[i]
    A[i] = A[hi]
    A[hi] = tmp
    # print(A)
    # print(f"Finally Swapped: {A[hi]}, {A[i]}")
    # print("***END ***")
    return i

sizes = [10,100,1000,10000,100000]
for k in sizes:
    A = np.random.randint(1,1000000,k)
    # print(f"len(A) = {len(A)}")
    start = time.perf_counter()
    quicksort_lomuto(A, 0, len(A)-1) 
    end = time.perf_counter()
    total = end-start
    print(f"{k} {total}")

