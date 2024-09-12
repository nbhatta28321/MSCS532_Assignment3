import random
import time
import tracemalloc


size = 5 #size of the hash table
map={} #empty hash table
primme_num = 6700417 # larger prime number
a = 6 # random value from {1,2 ... p-1}
b = 5 # random value from {0,1,2 ... p-1}

def hash_func(key):
          # Using universal family of hash function where is k is key of the hash table
          # size is the number of slot available for storage       
        return ((a * key + b) % primme_num) % size
        
def insert(key, value):
        if len(map) >= size:
               print("Size exceeded for the hashTable")
               return
        k = hash_func(key)
        map[k] = value
   
def search(key):
        k = hash_func(key)
        print("Searching key", k)

        if k in map:
            print(map[k])
        else:
            print("Key not found while searching")

def delete(key):
        k = hash_func(key)
        print("Mappp", map)
        print("Mappp lenght", len(map))
        
        print(f"Checing deleting key {key} to {k}")

        if k in map:
                print("deleting key", k)
                map.pop(k)
                print("After delete", map)
        else:
            print("Key not found")        
   

    
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
insert(1, "cat")
insert(2, "dog")
insert(3, "sheep")
insert(4, "tiger")
insert(5, "w")
insert(6, "e")

search(9)
delete(7)
# a =quick_sort([random.randint(1, 5) for _ in range(100)])
# print( "final", map)
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for random numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))