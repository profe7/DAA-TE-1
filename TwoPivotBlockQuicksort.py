#Nama   : Muhammad Fahreza Azka Arafat
#NPM    : 2106752331
#Kelas  : DAA-A

import random
import sys
from memory_profiler import memory_usage
import time

sys.setrecursionlimit(10**6)

def twoPivotBlockQuicksort(A, p, r):
    if p < r:
        q1, q2 = blockLomuto(A, p, r)
        twoPivotBlockQuicksort(A, p, q1 - 1)
        twoPivotBlockQuicksort(A, q1 + 1, q2 - 1)
        twoPivotBlockQuicksort(A, q2 + 1, r)

def blockLomuto(A, p, r):
    if A[p] > A[r]:
        A[p], A[r] = A[r], A[p]
    lt = p + 1
    gt = r - 1
    i = p + 1
    while i <= gt:
        if A[i] < A[p]:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
        elif A[i] > A[r]:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        i += 1
    A[p], A[lt - 1] = A[lt - 1], A[p]
    A[r], A[gt + 1] = A[gt + 1], A[r]
    return lt - 1, gt + 1

def performanceMetricsQuicksort(A):
    start = time.time()
    twoPivotBlockQuicksort(A, 0, len(A) - 1)
    end = time.time()
    return convertToMilliseconds(end - start)+"ms"+", "+str(round(max(memory_usage()), 3))+"MB"

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(A, L, R)

def merge(A, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def performanceMetricsMergeSort(A):
    start = time.time()
    memory_usage()
    end = time.time()
    return convertToMilliseconds(end - start)+"ms"+", "+str(round(max(memory_usage()), 3))+"MB"


def convertToMilliseconds(time):
    return str(round(time * 1000, 3))

def main():
    #Randomly generated arrays
    A = [random.randint(0, 1000) for i in range(2**9)]
    B = [random.randint(0, 1000) for i in range(2**13)]
    C = [random.randint(0, 1000) for i in range(2**16)]

    #Sorted arrays
    D = [i for i in range(2**9)]
    E = [i for i in range(2**13)]
    F = [i for i in range(2**16)]

    #Reverse sorted arrays
    G = [i for i in range(2**9, 0, -1)]
    H = [i for i in range(2**13, 0, -1)]
    I = [i for i in range(2**16, 0, -1)]

    validityCheck1 = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]
    validityCheck2 = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]

    print("Validity check, Quicksort:")
    print("Before: ", validityCheck1)
    twoPivotBlockQuicksort(validityCheck1, 0, len(validityCheck1) - 1)
    print("After: ", validityCheck1)
    print("====================================")
    print("Validity check, Merge sort:")
    print("Before: ", validityCheck2)
    mergeSort(validityCheck2)
    print("After: ", validityCheck2)
    print("====================================")
    print("Quicksort 2-pivot block partitioning (Random):")
    print("2^9: ", performanceMetricsQuicksort(A))
    print("2^13: ", performanceMetricsQuicksort(B))
    print("2^16: ", performanceMetricsQuicksort(C))
    print("====================================")
    print("Merge sort (Random):")
    print("2^9: ", performanceMetricsMergeSort(A))
    print("2^13: ", performanceMetricsMergeSort(B))
    print("2^16: ", performanceMetricsMergeSort(C))
    print("====================================")
    print("Quicksort 2-pivot block partitioning (Sorted):")
    print("2^9: ", performanceMetricsQuicksort(D))
    print("2^13: ", performanceMetricsQuicksort(E))
    print("2^16: ", performanceMetricsQuicksort(F))
    print("====================================")
    print("Merge sort (Sorted):")
    print("2^9: ", performanceMetricsMergeSort(D))
    print("2^13: ", performanceMetricsMergeSort(E))
    print("2^16: ", performanceMetricsMergeSort(F))
    print("====================================")
    print("Quicksort 2-pivot block partitioning (Reverse sorted):")
    print("2^9: ", performanceMetricsQuicksort(G))
    print("2^13: ", performanceMetricsQuicksort(H))
    print("2^16: ", performanceMetricsQuicksort(I))
    print("====================================")
    print("Merge sort (Reverse sorted):")
    print("2^9: ", performanceMetricsMergeSort(G))
    print("2^13: ", performanceMetricsMergeSort(H))
    print("2^16: ", performanceMetricsMergeSort(I))
    print("====================================")

if __name__ == "__main__":
    main()

