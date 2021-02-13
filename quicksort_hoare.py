#https://en.wikipedia.org/wiki/Quicksort (issue with floor(lo+hi)/2) not working)
#https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/ (Works)
import numpy as np
import time
import math
import sys

def quicksort_hoare(A, lo, hi):
    # print(f"lo = {lo}, hi = {hi}")
    if lo < hi:
        p = partition_hoare(A,lo,hi)
        # print(f"partition = {p}")
        quicksort_hoare(A,lo,p)
        quicksort_hoare(A, p+1, hi)

def partition_hoare(A, lo, hi):
    # print("***START ***")
    pivot = A[lo] #A[math.floor(lo+hi/2)]
    # print(f"Pivot: {pivot}")
    i = lo -1
    j = hi + 1
    # print(f"i = {i} and j = {j}")
    while(True):
        i += 1
        while (A[i] < pivot):
            i += 1

        j -= 1
        while (A[j] > pivot):
            j -= 1

        if (i >= j):
            return j
        
        A[i], A[j] = A[j], A[i]

sys.setrecursionlimit(10**6) 
sizes = [10,100,1000,10000,100000,1000000,10000000]
for k in sizes:
    A = np.random.randint(1,100,k)
    # print(f"len(A) = {len(A)}")
    start = time.perf_counter()
    quicksort_hoare(A, 0, len(A)-1) 
    end = time.perf_counter()
    total = end-start
    print(f"{k} {total}")

