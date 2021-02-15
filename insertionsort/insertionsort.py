#Insertion sort
#https://en.wikipedia.org/wiki/Insertion_sort
import numpy as np
import time
import math
import sys

def insertionsort(A):
    i = 1
    while i < len(A):
        j = i
        #work backwards from i index and sort 0 to i elements
        while j > 0 and A[j-1] > A[j]:
            #swap elements
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1

sys.setrecursionlimit(10**6)
sizes = [10,100,1000,10000,100000,1000000,10000000]
for k in sizes:
    A = np.random.randint(1,100,k)
    start = time.perf_counter()
    insertionsort(A)
    end = time.perf_counter()
    total = end-start
    print(f"{k} {total}")

