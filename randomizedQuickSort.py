import random
import time
import tracemalloc

def quick_sort(A): #function to divide the array

    left =[]
    middle =[]
    right =[]

    if len(A) <= 1: #return when the array has only one element which is sorted
        return A
    else:
        # pivot = A[len(A) // 2]
        pivot = random.choice(A)

        for i in A:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            elif i > pivot:
                right.append(i)
                    
        return quick_sort(left) + middle + quick_sort(right)

    
# function to do the merge sort for already sorted array
# tracemalloc.start()
# start = time.time()
# quick_sort(list(range(100)))
# end = time.time()
# current, peak_memory = tracemalloc.get_traced_memory()
# tracemalloc.clear_traces()
# print("Execution time for sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


# tracemalloc.start()
# start = time.time()
# a = quick_sort([])
# print("final", a)
# end = time.time()
# current, peak_memory = tracemalloc.get_traced_memory()
# tracemalloc.clear_traces()
# print("Execution time for reverse sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


tracemalloc.start()
start = time.time()
a =quick_sort([random.randint(1, 5000) for _ in range(100000)])
# print("final", a)
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for random numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))