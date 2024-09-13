import random
import time
import sys


def quick_sort(A): #function to divide the array

    left =[]
    middle =[]
    right =[]

    if len(A) <= 1: #return when the array has only one element which is sorted
        return A
    else:
        # pivot = A[0] # first element as pivot
        pivot = random.choice(A) #randomly choosing pivot

        for i in A:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            elif i > pivot:
                right.append(i)
                    
        return quick_sort(left) + middle + quick_sort(right) #sorting sub arrays based on left and right.

num=2000
sys.setrecursionlimit(3000)

   
# function to do the merge sort for random variables
start = time.time()
a =quick_sort([random.randint(1, 50) for _ in range(num)])
end = time.time()
print(f"Execution time for random numbers is {end-start}")

start = time.time()
quick_sort(list(range(num)))
end = time.time()
print(f"Execution time for sorted numbers is {end-start}")

start = time.time()
quick_sort(list(range(num, 0, -1)))
end = time.time()
print(f"Execution time for reverse sorted numbers is {end-start}")

start = time.time()
a =quick_sort([15 for _ in range(num)]) # array of repeated element
end = time.time()
print(f"Execution time for repeated elemets is {end-start}")
