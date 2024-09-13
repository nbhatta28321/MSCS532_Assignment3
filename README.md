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