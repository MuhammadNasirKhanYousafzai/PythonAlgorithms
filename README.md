# AlgorithmsInPython
## Algorithm
###### DEFINITION 
An algorithm is a sequence of unambiguous instructions for solving a problem.

### Selection sort
A sorting technique that is typically used for sequencing small lists. It starts by comparing the entire list for the lowest item and moves it to the #1 position. It then compares the rest of the list for the next-lowest item and places it in the #2 position and so on until all items are in the required order. Selection sorts perform numerous comparisons, but fewer data movements than other methods input values.

### Bubble sort
Sometimes referred to as sinking sort, is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order.

### Insertion sort
A sorting algorithm that inserts each item in the proper place into an initially empty list by comparing it with each item in the list until it finds the new element's successor or the end of the list. 

### Merge sort
A sorting technique that sequences data by continuously merging items in the list. Every single item in the original unordered list is merged with another, creating groups of two. Every two-item group is merged, creating groups of four and so on until there is one ordered list.


### Quick sort
A sorting technique that sequences a list by continuously dividing the list into two parts and moving the lower items to one side and the higher items to the other. It starts by picking one item in the entire list to serve as a pivot point. The pivot could be the first item or a randomly chosen one. All items that compare lower than the pivot are moved to the left of the pivot; all equal or higher items are moved to the right. It then picks a pivot for the left side and moves those items to left and right of the pivot and continues the pivot picking and dividing until there is only one item left in the group. It then proceeds to the right side and performs the same operation again. 



### Heap sort
A sorting algorithm that works by first organizing the data to be sorted into a special type of binary tree called a heap. The heap itself has, by definition, the largest value at the top of the tree, so the heap sort algorithm must also reverse the order input values.

### Tree data structure 
 A tree is a widely used abstract data type (ADT) or data structure implementing this ADT that simulates a hierarchical tree structure, with a root value and subtrees of children, represented as a set of linked nodes.

*Insertion Complexity:*	worst case O(logn), average best case O(logn)

*Searching Complexity:*	worst case O(logn), average best case O(logn)

*Deletion Complexity:*	worst case O(logn), average best case O(logn)

*Sorting Complexity:*  O(nlogn)
