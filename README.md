# Randomized Quicksort

Randomized Quick Sort is considered better for sorting using the quicksort algorithm. The larger array is broken down into multiple subarrays recursively until all the elements are sorted, and then it's merged to give the sorted elements. Every time, the arrays are partitioned into subarrays, and new pivot elements are chosen, which determines the time complexity of the running program. When the pivot elements are n unfavorable, the worst-case scenario can reach O(n2). However, with proper pivot elements chosen, it can be brought down to O(nlogn). Whenever the pivot is chosen randomly, it is far less likely that the algorithm will give the worst case. In contrast, when the pivot is always taken from a certain index, then in case of the input being in an already sorted format, the pivot has to interact with n subarrays that need to be iterated n times. In the same scenario, if the pivot is randomly chosen from the subarrays, then it is less likely that the random variable is the lowest or highest in the subarray.

The given Randomized QuickSort can have various execution times based on the type of element's position in the array list. For the sorted array, if the pivot element was the first element, then it has to compare and swap the left and right elements with the pivot every time since we divide smaller values to the left and larger ones to the right of the pivot. We would always be adding n elements for n subarrays. However, for randomized quicksort, the pivot would be chosen randomly. So, the randomly chosen element can have its pivot anywhere in between, which reduces the chance of going through every element. For instance, the pivot of the sorted array can be anywhere between the substrates, creating less likelihood of pivot in the worst case. Although there is a chance that some of the subarrays have the pivot element as first or last, it would not affect the whole recurrence relation. Hence the time complexity of the randomized quicksort would be O(n log n).

The program was run for different datasets of elements using random pivots as well as the first element as a pivot. For the fairly small dataset where n=500, the execution time for randomized Quicksortsort was very similar for random numbers and repeated elements. For sorted and reverse sorted elements, randomized Quicksortsort was stated to show the efficient result where the randomized Quicksort for sorted number was 0.00771570205688476594 second and 0.00455188751220703125 second faster than the Deterministic Quicksort.

When using a larger dataset, the randomized Quicksortsort was sorting efficiency; however, the Deterministic Quicksort had a "RecursionError" since it was reaching the maximum recursion depth. To test a larger data set, the recursion limit was set to 3000. Upon observation, the random and repeated elements have similar time execution with time complexity of O(n log n). However, the Deterministic Quicksort took longer to sort the already sorted and reverse-sorted elements. 


```
For n=500 for Deterministic Quicksort ----------1
Execution time for random numbers is 0.0004532337188720703
Execution time for sorted numbers is 0.00819087028503418
Execution time for reverse sorted numbers is 0.005023956298828125
Execution time for repeated elemets is 3.5762786865234375e-05

For n=2000 for Deterministic Quicksort ----------2
Execution time for random numbers is 0.0014450550079345703
Execution time for sorted numbers is 0.11330986022949219
Execution time for reverse sorted numbers is 0.08390212059020996
Execution time for repeated elemets is 0.00014209747314453125

```


```
For n=500 for randomized Quicksortsort ----------1
Execution time for random numbers is 0.00041103363037109375
Execution time for sorted numbers is 0.00047516822814941406
Execution time for reverse sorted numbers is 0.00047206878662109375
Execution time for repeated elemets is 3.528594970703125e-05

For n=2000 for randomized sort ----------------2
Execution time for random numbers is 0.001425027847290039
Execution time for sorted numbers is 0.0022389888763427734
Execution time for reverse sorted numbers is 0.002137899398803711
Execution time for repeated elemets is 0.00012803077697753906
```

# Hashing with Chaining

Hashing with chaining is the strategy for processing key-value pairs in the data set. A hash table is widely used for this scenario since it provides better performance for searching and inserting the pair in the hash table. However, if the hash function is poorly distributed, the worst case for search, insert, and delete operations could be O(n), where n is the number of keys inserted for a particular hashed key. There are various factors that depend on when the operation is done for the value in the hash table.

When the key value pair is added to the hash table with simple uniform hashing, it will take O(1) time complexity since it will simple insert the key directly in the slot. Similarly, for searching a key, it takes constant time for the search operation with a time complexity of O(1). The delete operation operation also deletes in the linear constant time with a constant load factor.

However, hashing with chaining has a different time complexity when the load factor is different. In the implementation, the universal family of the hash function is used where k is the key of the hash table, and m is the size is the number of slots available for storage which is (( ak + b ) mod p ) mod m which gives the value for available slot less than the size of the hash table. This will ensure that the value would not exceed the size 'm'. In case of a higher load factor, the probability of hashed element repetition is higher which will result in collision unless handled with chaining the hash table. When there is more data to be inserted with a low load factor, each hashed key is chained with multiple key-value pairs. So when the slots are already occupied by at least one key-value pair, and if the load factor is less and more data is being inserted, it has to look up the value in each hashed key. The time complexity to insert an element to a chained hashed key would be O(n), where n is the number of key-value pairs in the hash table. 

Searching or deleting an element can have a worst case of O(n) as well when the element is at the end of the list in the hashed table. This can be prevented by implementing various methods. One would be changing the load factor, which is by spreading the size of the slot, which makes the load factor less, and the probability of adding a key-value pair in the same hashed key will decrease. However, this might cause the unnecessary use of more space when the data is less. To solve that issue, we can use the dynamic resizing of the hash table. This can be done by reducing the total number of values in the hash table to the number of slots in the table when the number of elements is more. This can be determined as the load factor, which is the ratio of the total number of pairs to the slot allocated for the key-value pair. It can be done by checking the load factor when inserting an element. This involves choosing a certain load factor where the worst-case scenario can be prevented. This way, whenever the elements exceed a certain load factor, the number of slots can be increased; this dynamically increasing hash table would be the best implementation to address lower the number of counts for different insertion, search, and delete operations.

