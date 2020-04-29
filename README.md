# DS-Algo-interview-preparation in Python

#### Cracking the coding interview in Python [Notebook](Notebooks/Ctci.ipynb)
#### Daily coding problems [Notebook](Notebooks/dailycodingproblem.ipynb)
---
**Install jupyter notebook extensions**
```
In Anaconda powershell prompt
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge jupyter_nbextensions_configurator
```
Enable these extensions [image](Notes/jupyter_extensions_screenshot.PNG) for easier navigation through the notebooks.

### Notebooks
1. [Arrays](Notebooks/Arrays.ipynb)
2. [Strings](Notebooks/Strings.ipynb)
3. [Sliding window](Notebooks/SlidingWindow.ipynb)
4. [Trees](Notebooks/Trees.ipynb)
5. [Graphs](Notebooks/Graphs.ipynb)
6. [Linked List](Notebooks/LinkedList.ipynb)
7. [Heap](Notebooks/Heap.ipynb)
8. [Backtracking](Notebooks/Backtracking.ipynb)
9. [DynamicProgramming](Notebooks/DynamicProgramming.ipynb)
10. [Design datastructures](Notebooks/DesignStructures.ipynb)
---
## Table of contents
- [DS-Algo-interview-preparation in Python](#ds-algo-interview-preparation-in-python)
  - [Math](#math)
  - [Arrays with unique approaches](#arrays-with-unique-approaches)
  - [Two pointers](#two-pointers)
  - [Design questions](#design-questions)
  - [Fast and slow pointers](#fast-and-slow-pointers)
  - [In-place reverse](#in-place-reverse)
  - [LinkedList](#linkedlist)
  - [Sliding Window](#sliding-window)
  - [Merge Intervals](#merge-intervals)
  - [Cyclic sort](#cyclic-sort)
  - [Modified Binary Search](#modified-binary-search)
  - [Bitwise XOR](#bitwise-xor)
  - [Top K elements (Heap)](#top-k-elements-heap)
  - [K-way merge](#k-way-merge)
  - [Trees](#trees)
  - [Graphs](#graphs)
  - [Topological sort](#topological-sort)
  - [Dynamic Programming](#dynamic-programming)
  - [Backtracking](#backtracking)
  - [Trie](#trie)
---
<!-- /TOC -->

### Array
| #   |Question| Solution |Difficulty | Tags |Notes |
| -|----- | ---------- |-----|-------|----|
|1    |[product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self)   | [Modified two pointers](Python/Arrays/product_except_self.py)  | Medium  |```Array``` ```Two pointers```|Follow up: O(N) Left product & right product  |

---
### 2D Array
| #   |Question| Solution |Difficulty | Tags |Notes |
| -|----- | ---------- |-----|-------|----|
|1   |[Spiral matrix](https://leetcode.com/problems/spiral-matrix)   |[Arrays](Python/Arrays/spiral-matrix.py)   | Medium  | ```Matrix``` | |
|2   |[Search in 2D matrix](https://leetcode.com/problems/search-a-2d-matrix-ii)   |[Matrix](Python/Arrays/search-in-2d-matrix.py)   |  Medium | ```BinarySearch``` ```Matrix``` | Tweak: Instead of performing a binary search check if the last row's first val is greater or lesser than the target|
|3   |[Game of life](https://leetcode.com/problems/game-of-life/)   |[Array](Python/Arrays/game-of-life.py)   |  Medium | ```Matrix```||
|4  |[Rotate Image](https://leetcode.com/problems/rotate-image)   | [Matrix transpose](Python/Arrays/rotate-image.py)  | Medium  |```Matrix```| Reverse rows and swap elements on either side of diagonals  |
|5   | [Diagonal traverse](https://leetcode.com/problems/diagonal-traverse)  | [Matrix](Python/Arrays/diagonal-traverse.py)  |  Medium  |  ```Matrix``` ```deque```|   |
|6   | [Set matrix to zeros](https://leetcode.com/problems/set-matrix-zeroes)  | [Matrix](Python/Arrays/set-matrix-zeroes.py)  | Medium   | ```Matrix```  | Get the position of 0s in the matrix and in another iteration update the values  |
|7   | [Generate spiral matrix](https://leetcode.com/problems/spiral-matrix-ii)  | [Matrix](Python/Arrays/spiral-matrix2.py)  | Medium  | ```Matrix```  | Similar to spiral matrix  |


---


### Math
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Reverese Integer](https://leetcode.com/problems/reverse-integer/)  |  [Math](Python/Math/reverse-integer.py) |  Easy |In Java, Overflow when the result is greater than 2147483647 or less than -2147483648.  not in Python |
|2   | [fraction-to-recurring-decimal](https://leetcode.com/problems/fraction-to-recurring-decimal)  | []()  |   |   |
|3   | [roman-to-integer](https://leetcode.com/problems/roman-to-integer)  | []()  |   |   |
|4   | [divide-two-integers](https://leetcode.com/problems/divide-two-integers)  | []()  |   |   |
|5   | [powx-n](https://leetcode.com/problems/powx-n)  | []()  |   |   |
|6   | [perfect-squares](https://leetcode.com/problems/perfect-squares)  | []()  |   |   |
|7   | [excel-sheet-column-number](https://leetcode.com/problems/excel-sheet-column-number)  | []()  |   |   |
|8   | [sqrtx](https://leetcode.com/problems/sqrtx)  | []()  |   |   |
|9   | [factorial-trailing-zeroes](https://leetcode.com/problems/factorial-trailing-zeroes)  | []()  |   |   |

---

### Two pointers
[Notes](Patterns/two_pointers_patterns.md)

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[Two sum ](https://leetcode.com/problems/two-sum/) | [Dictionary](Python/TwoPointers/twosum.py) [Two pointers](Python/TwoPointers/twosum_sorted.py) | Easy |  |
| 2  | [Two sum less than k](https://leetcode.com/problems/two-sum-less-than-k/)  | [Two pointers](Python/TwoPointers/twosum-lessthanK.py)  | Easy  |   |
|3   | [3 Sum](https://leetcode.com/problems/3sum/) | [Two pointers](Python/TwoPointers/3sum.py) | Medium | |
|4  | [3 Sum closest](https://leetcode.com/problems/3sum-closest/) | [Two pointers](Python/TwoPointers/3sum_closest.py) | Medium | |
|5   | [3 Sum smaller](https://leetcode.com/problems/3sum-smaller/) | [Two pointers](Python/TwoPointers/3-sum-smaller.py) | Medium | |
|6   | [Squaring of a sorted array](https://leetcode.com/problems/squares-of-a-sorted-array) | [Two pointers](Python/TwoPointers/Squares_of_sorted_array.py) |Easy | Insert largest square in the first of the array. list.insert(0,val)|
|7    | [Merge sorted array](https://leetcode.com/problems/merge-sorted-array) | [Two pointers](Python/TwoPointers/merge_sorted_array.py) | Easy | |
|8   | [Dutch national flag/Sort colors](https://leetcode.com/problems/sort-colors/) | [Two pointers](Python/TwoPointers/dutch_national_flag.py) | | |
|9   | [4sum](https://leetcode.com/problems/4sum) | [Two pointers](Python/TwoPointers/4sum.py) | Medium | Extension of 3sum |
|10| [Trapping water](https://leetcode.com/problems/trapping-rain-water)|[Two pointers](Python/TwoPointers/trapping_water.py)| Hard | Use left_max and right_max|
|11   | [Backspace string compare](https://leetcode.com/problems/backspace-string-compare/) | [Using stack](Python/Stack/backspace_string_compare.py) |Easy |  |
|12  |[k-diff-pairs](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|[Two pointers](Python/TwoPointers/k-diff-pairs-array.py)|Easy| |
|13   | [Shortest unsorted continuous subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | [Two pointers](Python/TwoPointers/Shortest-unsorted-continuous-subarray.py) | Easy| |
|14  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections)|[](Python/TwoPointers/)|Medium||
|15  |[Reverse string](https://leetcode.com/problems/reverse-string)|[Two pointers](Python/TwoPointers/reverse_vowels_string.py)| Easy||
|16| [Reverse vowels of a string](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[ ](Python/TwoPointers/)| Easy ||
|17 | [Move zeros](https://leetcode.com/problems/move-zeroes)|[Two pointers](Python/TwoPointers/move_zeroes.py)|Easy |  |
|18  | [Remove duplicates from sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Two pointers ](Python/TwoPointers/Remove_duplicates_from_sortedarray.py)|Easy |  |
|19  | [Candy crush](https://leetcode.com/problems/candy-crush)|[](Python/TwoPointers/)|Medium | |
|20   | [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Two pointers](Python/TwoPointers/median-sorted-arrays.py) [Binary search](Python/BinarySearch/median-2sortedarrays.py)|Hard |1. Two pointers is O(n+m).  2. Binary search O(log(min(n,m)) [Algo](Notes/Median-of-2sortedarrays.pdf)|


---

### Design datastructures questions

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Design lru-cache](https://leetcode.com/problems/lru-cache)  | [Solution](Python/DesignQuestions/LRUcache.py)  | Medium  | Use doubly LL  |
|2   | [insert-delete-getrandom-o1](https://leetcode.com/problems/insert-delete-getrandom-o1)  | [Solution](Python/DesignQuestions/insert-getrandom.py)  | Medium  |   |
|3   | [min-stack](https://leetcode.com/problems/min-stack)  | [Solution](Python/DesignQuestions/min-stack.py)  | Easy  |   |
|4   | [MaxStack](https://leetcode.com/problems/max-stack/)  | [Solution](Python/DesignQuestions/max-stack.py)  | Easy  |   |
|5   | [Design stack with increment operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)  | [Solution](Python/DesignQuestions/stack-with-increment.py)  | Medium  |   |
|6   | [lfu-cache](https://leetcode.com/problems/lfu-cache)  | []()  |   |   |
|7   | [design-tic-tac-toe](https://leetcode.com/problems/design-tic-tac-toe)  | []()  |   |   |
|8   | [design-in-memory-file-system](https://leetcode.com/problems/design-in-memory-file-system)  | []()  |   |   |
|9   | [design-hashmap](https://leetcode.com/problems/design-hashmap/)  | [Solution](Python/DesignQuestions/Design_Hashmap.py)  | Medium  | |
|10 | [Design HashSet](https://leetcode.com/problems/design-hashset)|[]() | | |
|11   |[design-hit-counter](https://leetcode.com/problems/design-hit-counter)   |   |   |   |
|12   |[add-and-search-word-data-structure-design](https://leetcode.com/problems/add-and-search-word-data-structure-design)   |   |   |   |
|13   |[design-log-storage-system](https://leetcode.com/problems/design-log-storage-system)   |   |   |   |
|14   |[design-circular-queue](https://leetcode.com/problems/design-circular-queue)   |   |   |   |
|15   |[design-file-system](https://leetcode.com/problems/design-file-system)   |   |   |   |
|16   |[implement-stack-using-queues](https://leetcode.com/problems/implement-stack-using-queues)   |   |   |   |
|17   |[design-skiplist](https://leetcode.com/problems/design-skiplist)   |   |   |   |
|18   |[design-circular-deque](https://leetcode.com/problems/design-circular-deque)   |   |   |   |
|19   |[design-linked-list](https://leetcode.com/problems/design-linked-list)   |   |   |   |
|20   |[design-twitter](https://leetcode.com/problems/design-twitter/)   |   |   |   |
|21   |[design-snake-game](https://leetcode.com/problems/design-snake-game)   |   |   |   |
|22   |[all-oone-data-structure](https://leetcode.com/problems/all-oone-data-structure)   |   |   |   |
|23   |[flatten-nested-list-iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)   |   |   |   |
|24   |[design-search-autocomplete-system](https://leetcode.com/problems/design-search-autocomplete-system)   |   |   |   |
|25   |[time-based-key-value-store](https://leetcode.com/problems/time-based-key-value-store/)   |   |   |   |


---

### Fast and slow pointers

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Linkedlist cycle](https://leetcode.com/problems/linked-list-cycle) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/linkedlist_cycle.py) | Easy | When slow and fast ptrs meet there is a cycle |
|2   | [Linkedlist cycle 2](https://leetcode.com/problems/linked-list-cycle-ii) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/) | Medium | After checking for a cycle, re-initialize fast ptr to 1st node and increment both slow and fast. The node at which they meet is the start of the cycle |
|3   | [Middle of Linkedlist](https://leetcode.com/problems/middle-of-the-linked-list) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/middle_linkedlist.py) |Easy | The node at which slow ptr stops |
|4   | [Palindrome LL ](https://leetcode.com/problems/palindrome-linked-list) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/palindrome_linkedlist.py) |Medium | Find middle and reverse the 2nd half of the list and compare both|
|5   | [Reorder List](https://leetcode.com/problems/reorder-list/) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/reorder-list.py) | Medium | Find middle, reverse 2nd half and merge one from 1st list and one from 2nd list|
|6   | [Circular array loop](https://leetcode.com/problems/circular-array-loop/) | [ ](Python/Fast_and_slow_pointers/) | Medium | |

---

### In-place reverse


| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Reverse LL](https://leetcode.com/problems/reverse-linked-list) | [In-place reverse](Python/LinkedList/reverseLL.py) |Easy | Use prev and next to update the links |
|2   | [Reverse LL between](https://leetcode.com/problems/reverse-linked-list-ii) | [In-place reverse](Python/LinkedList/reverseLL-between.py) | Medium | loop till k-1th node and reverse |
|3   | [Rotate LL](https://leetcode.com/problems/rotate-list) | [In-place reverse](Python/LinkedList/rotateLL.py) | Medium| Move one ptr k times and then move start moving both ptrs. Update next of ptr1 to head and ptr2 to None |
|4   | [Reverse nodes in k-group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [In-place reverse](Python/LinkedList/reverse-nodes-k-groups.py) | Hard | Check if nodes are multiple of k then only reverse |
|5   | Reverse nodes in k-alternating subgroup | [In-place reverse](Python/LinkedList/reverse-nodes-kgroups-alternatively.py) | Medium | Reverse k groups with a while loop to skip k nodes |
|6   | [Swap nodes in pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)  | []()  | Medium  |   |

---

### LinkedList
[pattern]()

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Flatten a multilevel doubly LL](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) | [ ](Python/LinkedList/flatten_doublylist.py) |Medium | |
|2   | [Odd Even list](https://leetcode.com/problems/odd-even-linked-list) | [Linkedlist](Python/LinkedList/oddevenLL.py) | Medium | Initialize even_head & odd_head and update the links. Point the last node of oddlist to even head|
|3   | [Max points on a line](https://leetcode.com/problems/max-points-on-a-line) | [   ](Python/LinkedList/maxpoints-on-line.py) | Medium| |
|4   | [Copy list with random ptr](https://leetcode.com/problems/copy-list-with-random-pointer) | [hashmap ](Python/LinkedList/copy-list-with-random-ptr.py) | Medium | |
| 5  | [Add two numbers ](https://leetcode.com/problems/add-two-numbers) | [Linked List](Python/LinkedList/add2numbers.py)|Medium | Take care of carry. Create a new node after adding |
| 6  | [Add two numbers 2](https://leetcode.com/problems/add-two-numbers-ii) | [Linked List](Python/LinkedList/add-numbers-reverse.py)|Medium | |
| 7  | [Partition list](https://leetcode.com/problems/partition-list) | [Linked List](Python/LinkedList/partition-list.py)|Medium | Create two seperate nodes (smaller, larger). Link last of smaller to first of larger|
| 8  | [Plus one LL](https://leetcode.com/problems/plus-one-linked-list) | [Linked List](Python/LinkedList/plus-one-LL.py)| Medium | Dummy nodes and move till non nine nodes and increment by 1. Set 9s to 0|
| 9  | [Insert into a sorted circular LL](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list) | [ ](Python/LinkedList/insert-sorted-circularLL.py)| | |
|10  | [Remove Nth node from the end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Linked List](Python/LinkedList/remove-nth-node.py)| Medium | create dummy nodes (first & second) move first till k-1th node from start. Now, move both first and second. Second reaches k-1th node from start. Update the next ptr.|
| 11  | [Remove duplicates from LinkedList](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | [ ](Python/LinkedList/)|Medium | |
|12   | [Sort list](https://leetcode.com/problems/sort-list)  |   |   |   |

---

### Sliding Window

[Notes](Patterns/sliding_window_patterns.md)

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[Max sum subarray of size k/ Max subarray](https://leetcode.com/problems/maximum-subarray/)| [Sliding Window](Python/SlidingWindow/max_sum_subarray.py) | Easy | |
| 2   |[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)| [Sliding Window](Python/SlidingWindow/smallest_sub_array_with_given_sum.py)|  Easy |[Algo](Notes/Notes%20Smallest%20sub%20array%20with%20given%20sum.pdf) |
| 3   |[Longest Substring with at most K Distinct Characters *](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters) | [Sliding window](Python/SlidingWindow/Longest_substring_withK_distinct_characters.py) | Hard | |
|4  |[Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)|[Sliding Window](Python/SlidingWindow/fruits_into_baskets.py) | Medium |[Algo](Notes/Fruits_into_baskets.pdf) |
|5  | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)| [Sliding Window](Python/SlidingWindow/Longest_repeating_character_replacement.py)| Medium | |
|6  | [Permutation in String](https://leetcode.com/problems/permutation-in-string/)|[Sliding Window](Python/SlidingWindow/permutation_in_string.py)| Medium | |
|7  | [Longest Substring Without Repeating Characters ](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Sliding Window ](Python/SlidingWindow/longest-substring-without-repeating-characters.py) |Medium | |
|8   | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | [Sliding Window ](Python/SlidingWindow/max-consecutive-ones.py) | Medium | |
|9   | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | []() | Medium | |
|10 | [Minimum Window substring](https://leetcode.com/problems/minimum-window-substring/) | []() || | |
|11  | [Concatenated words](https://leetcode.com/problems/concatenated-words/) | [ ]() | | |
|12  | [Minimum Window substring](https://leetcode.com/problems/) | []() | Hard| |
|13   | [Sliding window maximum](https://leetcode.com/problems/sliding-window-maximum/) | [ ]() | Hard | Use max heap |
|14   | [consecutive-numbers-sum](https://leetcode.com/problems/consecutive-numbers-sum/)  | [Sliding window & Math](Python/SlidingWindow/consecutive-numbers-sum.py)  | Hard  |   |
|15   | [grumpy-bookstore-owner](https://leetcode.com/problems/grumpy-bookstore-owner/)  |   |   |   |
|16   | [minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence/)  |   |   |   |
|17   | [sliding-window-median](https://leetcode.com/problems/sliding-window-median/)  |   |   |   |
|18   | [subarrays-with-k-different-integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)  |   |   |   |
|19   | [number-of-submatrices-that-sum-to-target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)  |   |   |   |
|20   | [subarray-product-less-than-k](https://leetcode.com/problems/subarray-product-less-than-k/)  | [Sliding Window](Python/SlidingWindow/subarray_prod_less_thanK.py)  | Medium  |   |


---

### Merge Intervals
[Notes](Patterns/merge-intervals.md)
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Merge intervals](https://leetcode.com/problems/merge-intervals) | [Merge intervals](Python/MergeIntervals/merge_intervals.py)|Medium | |
| 2  |[Non overlapping intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [Merge intervals](Python/MergeIntervals/non-overlapping-intervals.py)| Medium| |
| 3  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections/) | [Merge intervals](Python/MergeIntervals/interval-list-intersections.py)| Medium| |
| 4  |[Meeting rooms ](https://leetcode.com/problems/meeting-rooms) | [Merge intervals](Python/MergeIntervals/meeting-rooms.py)| Easy| |
| 5  |[Meeting rooms 2](https://leetcode.com/problems/meeting-rooms-ii) | [Merge intervals](Python/MergeIntervals/meeting-rooms2.py)| Medium| |
| 6  |[Insert intervals](https://leetcode.com/problems/insert-interval/) | [Merge intervals ](Python/MergeIntervals/insert-intervals.py)| Hard| |
| 7  | [Employee free time](https://leetcode.com/problems/employee-free-time/) | [ ](Python/MergeIntervals/employee-free-time.py)|Hard | |

---
### Cyclic sort
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Missing number](https://leetcode.com/problems/missing-number/) | [Cyclic sort](Python/CyclicSort/)| Easy| n*n+1/2|
| 2  | [Find all missing numbers](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [Cyclic sort](Python/CyclicSort/find-all-missing-nos.py)| Medium |index + 1 == nums[index]? |
| 3  |[First missing positive](https://leetcode.com/problems/first-missing-positive/) | [Cyclic sort](Python/CyclicSort/first-missing-positive.py)| Hard | TC: O(N), SC: O(1) |

---
### Modified Binary Search
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Modified binary search](Python/BinarySearch/find-first-last-in-sortedarray.py)| Medium |  |
| 2  | [single-element-in-a-sorted-array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | [Modified BinarySearch ](Python/BinarySearch/single-num-in-sortedarray.py)| Medium | |
| 3  | [kth Missing element in sorted array](https://leetcode.com/problems/missing-element-in-sorted-array/) | [ ](Python/)| Medium | |
| 4  | Search Bitonic Array | [ ]()| | |
| 5  | Bitonic array maximum[]() | [ ]()| | |
| 6  | [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Modified BinarySearch ](Python/BinarySearch/search-rotated-sortedarray.py)|Medium | |
| 7  | [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Modified BinarySearch ](Python/BinarySearch/min-rotated-sortedarray.py)| Medium | 1. O(N) updating minimum    2. O(logN) Binary search|
|8   | [Search in rotated sorted array with duplicates ](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)  | []()  |  Medium |   |
|9   | [Find min in rotated sorted array with duplicates](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)  | []()  | Hard   |   |
| 8  | Rotation count | [ ]()| | |
| 9  | Order agnostic binary search | [ ]()| | |
| 10  | [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/) | [Binary search + Two pointers](Python/BinarySearch/k-closest-elements.py)|Medium | |

---
### Bitwise XOR
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [single-number](https://leetcode.com/problems/single-number/) | [ ]()| | |
| 2  | [single-number-ii](https://leetcode.com/problems/single-number-ii/) | [ ]()| | |
| 3  | [complement-of-base-10-integer](https://leetcode.com/problems/complement-of-base-10-integer/) | []()| | |
| 4 | [rotate-image](https://leetcode.com/problems/rotate-image/) | [ ]()| | |
| 5  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) | [ ]()| | |
| 6  | [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [ ]()| | |
| 7  | [Min-Cost-to-Connect-Ropes](https://leetcode.com/discuss/interview-question/344677/Amazon-or-Online-Assessment-2019-or-Min-Cost-to-Connect-Ropes) | [ ]()| | |

---
### Top K elements (Heap)
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Dictionary](Python/Heap/top-k-elements.py) | Medium | Use dictionary O(nlogn). Quickselect O(N) |
| 2  | [sort-characters-by-frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | [Top k elements](Python/Heap/sort-characters-freq.py)| Medium | Use dictionary |
| 3 | [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/)   |[Top k elements](Python/Heap/kth-smallest-in-list.py)   |Medium   | Use heapq  |
| 4  | [maximum-frequency-stack](https://leetcode.com/problems/maximum-frequency-stack/) | [Top k elements]()| | |
| 5  | [maximum-distinct-elements-removing-k-elements](https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/) | [Top k elements]()| | |
| 6  | [reorganize-string](https://leetcode.com/problems/reorganize-string/) | [Top k elements]()| | |
| 7  | [rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [Top k elements]()| | |
| 8  | [task-scheduler](https://leetcode.com/problems/task-scheduler/) | [Top k elements]()| | |
|9   | [kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)  | []()  |   |   |

---
### K-way merge
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [heap](Python/k-way-merge/merge-k-sortedlist.py)|Hard | |
| 2  | [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [Heap](Python/Heap/kth-smallest-in-matrix.py)|Medium | |
| 3  | [smallest-range-i](https://leetcode.com/problems/smallest-range-i/) | []()| | |
| 4 | [find-k-pairs-with-smallest-sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | []()| | |
| 5  | [partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum/) | []()| | |

---
### DFS
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | []()  | []()  |   |   |
|2   | []()  | []()  |   |   |

---
### BFS
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [rotting-oranges](https://leetcode.com/problems/rotting-oranges/)  | [BFS](Python/Tree/rotting-oranges.py)  | Medium  |   |

---
### Trees
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1|[Same Tree](https://leetcode.com/problems/same-tree/)|[Recursion](Python/Tree/same-tree.py)| Easy | |
|2|[Subtree](https://leetcode.com/problems/subtree-of-another-tree/)|[Tree](Python/Tree/subtree.py)|Easy||
|3|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Recursion](Python/Tree/diameter.py)|Easy | |
|4|[maximum-depth-of-n-ary-tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[Tree DFS](Python/Tree/max_depth-nary-tree.py)|Easy | Get the max depth of subtrees|
|5|[maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[DFS](Python/Tree/max_depth_BT.py)|Easy | |
|6|[range-sum-of-bst](https://leetcode.com/problems/range-sum-of-bst/)|[](Python/Tree/range_sum.py)|Easy | |
|7|[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/)|[DFS](Python/Tree/merge_BT.py)|Easy | |
|8|[search-in-a-binary-search-tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[DFS](Python/Tree/search-bst.py)| | |
|9|[path-sum](https://leetcode.com/problems/path-sum/)|[DFS](Python/Tree/path_sum.py)| Easy |  |
|10|[diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Tree](Python/Tree/diameter-BT.py) | Easy |  |
|11 | [kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Tree DFS](Python/Tree/kth-smallest.py) | Medium | Push left tree nodes into stack and pop them by decrementing k. when k=0 return node.val  |
|12 | [all-nodes-distance-k-in-binary-tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [](Python/Tree/nodes-k-distance.py) | Medium |  |
|13 | [lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [DFS](Python/Tree/lowest_common-ancestor.py) | Medium |  |
|14 |[minimum-depth-of-binary-tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[DFS](Python/Tree/min_depth_BT.py)|Easy | |
|15 | [serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [](Python/Tree/) |  |  |
|16 | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values) | [](Python/Tree/) |  |  |
|17 | [Iterative postorderTraversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)  |[DFS](Python/Tree/postorder_iterative.py)   | Hard  | Using stack |
|18 | [binary-search-tree-iterator](https://leetcode.com/problems/binary-search-tree-iterator) | [](Python/Tree/) |  |  |
|19 | [serialize-and-deserialize-bst](https://leetcode.com/problems/serialize-and-deserialize-bst) | [](Python/Tree/) |  |  |
|20 | [convert-BST-to-sorted-doublyLL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | [](Python/Tree/) |  |  |
|21 | [construct-BT-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | [](Python/Tree/)| | |
| 22  | [Valid BST](https://leetcode.com/problems/validate-binary-search-tree/) | [BST](Python/Tree/valid-bst.py)| Medium| Use lower & upper, initialize them to extremes. Check val <= lower or val>= upper (recursively for all nodes) |
| 23  | [Binary tree level order traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | [Tree BFS](Python/Tree/binary-tree-level-order.py)| Medium|Use a queue |
| 24  | [Reverse level order traversal ](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) | [Tree BFS](Python/Tree/reverse-level-order-traversal.py)|Medium | |
| 25  | [Zigzag conversion](https://leetcode.com/problems/zigzag-conversion) | [](Python/Tree/)| Medium| |
| 26  | [Average of levels in BT](https://leetcode.com/problems/average-of-levels-in-binary-tree) | [](Python/Tree/)| Easy | |
| 27  | Next interval | [Tree DFS](Python/Tree/)| | |
| 28  | [Populating next right ptrs in tree](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | [](Python/Tree/)| | |
| 29  | [Binary tree right side view](https://leetcode.com/problems/binary-tree-right-side-view/) | [](Python/Tree/)| | |
| 30  | [Tree boundary](https://leetcode.com/problems/boundary-of-binary-tree/) | [](Python/Tree/)| | |
| 31  | [ipo](https://leetcode.com/problems/ipo/) | [](Python/Tree/)|
| 32  | [Path sum 2](https://leetcode.com/problems/path-sum-ii) | [](Python/Tree/)| | |
| 33  | [Path sum 3](https://leetcode.com/problems/path-sum-iii/) | [](Python/Tree/)| | |
| 34  | [Binary tree paths](https://leetcode.com/problems/binary-tree-paths/) | [](Python/Tree/)| | |
| 35  | [Diameter of binary tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [](Python/Tree/)| | |
| 36  | [Binary tree maximum path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [](Python/Tree/)| | |
| 37  | [find-median-from-data-stream](https://leetcode.com/problems/find-median-from-data-stream/) | [](Python/Tree/)| | |
| 38  | [sliding-window-median](https://leetcode.com/problems/sliding-window-median/) | [](Python/Tree/)| | |

---
### Graphs
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | Breadth first search  | [Using queue](Python/Graphs/bfs-graph.py)  | Easy  |   |
|2   | Depth first search  |[Recursion](Python/Graphs/dfs-graph.py)   | Easy  |   |
|3   |Remove Edge  | [](Python/Graphs/)  |   |   |
|4   | Find mother vertex  | [](Python/Graphs/)  |   |   |
|5   | Count num of edges  | [](Python/Graphs/)  |   |   |
|6   | Path exists   | [](Python/Graphs/)  |   |   |
|7   | [Graph valid tree](https://leetcode.com/problems/graph-valid-tree)  |  [Cycle detection in undirected](Python/Graph/graph-valid-tree.py) | Medium  |   |
|8   | Shortest path between two vertices  |[](Python/Graphs/)   |   |   |
|9   | [evaluate-division](https://leetcode.com/problems/evaluate-division)  |   | [](Python/Graphs/)  |   |
|10   | [clone-graph](https://leetcode.com/problems/clone-graph)  |  [BFS + hashmap](Python/Graph/clone-graph.py) | Medium  | [Notes](Notes/CloneGraph.pdf)  |
|11   | [is-graph-bipartite](https://leetcode.com/problems/is-graph-bipartite)  |   |  [BFS](Python/Graphs/bipartite-graph.py) |  Graph coloring |
|12   | Detect cycle in a directed graph  | []()  | Medium  |   |
|13   | Detect cycle in an undirected graph  | [DFS](Python/Graphs/cycle-undirected.py)  | Medium  |   |
|14   | [Reconstruct itinerary](https://leetcode.com/problems/reconstruct-itinerary)  | [Eulerian path](Python/Graphs/reconstruct-itinerary.py)  | Medium  | [Notes](Notes/Reconstruct-itinerary.pdf)  |
|15   |[Number of connected components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)   | [DFS](Python/Graphs/connected-components.py)   | Medium  |   |
|16   |[Alien dictionary](https://leetcode.com/problems/alien-dictionary/)   |  [Topological sort + cycle detection](Python/Graphs/) | Hard  |   |


---
### Topological sort
[Topological sort code](Python/Graphs/topological-sort.py)

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[course-schedule](https://leetcode.com/problems/course-schedule) | [Topological sort ](Python/Graphs/course-schedule.py)|Medium | Cycle detection with Indegree idea |
| 2  | [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii) | [Topological sort ](Python/Graphs/course-schedule-2.py)| | |
| 3 |  [sequence-reconstruction](https://leetcode.com/problems/sequence-reconstruction) | [ ]()| | |
| 4 | [longest-increasing-path-in-a-matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix) | [ ]()| | |
| 5  | [sort-items-by-groups-respecting-dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies) | [ ]()| | |
| 6  | [alien-dictionary](https://leetcode.com/problems/alien-dictionary) | [ ]()| | |

---
### Dynamic Programming
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | 0/1 knapsack  | [DP with memoization](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/0-1-knapsack.py)  | Easy  |   |
|2   |  [Partition equal  subset sum](https://leetcode.com/problems/partition-equal-subset-sum) | []()  | Medium  |   |
|3   | [Climbing stairs](https://leetcode.com/problems/climbing-stairs/)  | [DP](Python/DynamicProgramming/climbing-stairs.py)  | Easy  |   |
|4   | [Fibonacci number](https://leetcode.com/problems/fibonacci-number/)  | [Bottom up DP](Python/DynamicProgramming/fibonaci.py)  |  Easy |   |
|5   | [Min cost climbing stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)  |   |   |   |


---
###  Backtracking
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   |[Permutations](https://leetcode.com/problems/permutations/)   | [Backtracking](Python/Backtracking/permutations.py)  | Medium  | DFS  |
|2   |[Permutations 2](https://leetcode.com/problems/permutations-ii/)   |[Backtracking](Python/Backtracking/permutations-ii.py)   | Medium  |   |
|3   |[Combinations](https://leetcode.com/problems/combinations/)   | [Backtracking](Python/Backtracking/combinations.py)  | Medium  |   |
|4   |[Combination sum I](https://leetcode.com/problems/combination-sum/)   | [Backtracking](Python/Backtracking/combination-sum.py)  | Medium  |   |
|5   |[Combination sum II](https://leetcode.com/problems/combination-sum-ii/)   | [Backtracking](Python/Backtracking/combination-sum-2.py)  | Medium  |   |
|6   | [combination-sum-iii](https://leetcode.com/problems/combination-sum-iii/)  | [Backtracking](Python/Backtracking/combination-sum-3.py)  | Medium  |   |
|7   | [Generate Parenthesis](https://leetcode.com/problems/generate-parentheses/)  | [Backtracking](Python/Backtracking/generate-parentheses.py)  | Medium  |   |
|8   | [Subsets](https://leetcode.com/problems/subsets)  | [Subsets](Python/Backtracking/subsets.py)  |   |   |
|9   | [Word search](https://leetcode.com/problems/word-search)  | [Backtracking](Python/Backtracking/word-search.py)  | Medium  |   |
|10   | [Word search 2](https://leetcode.com/problems/word-search-ii)  | []()  |   |   |
|11   | [regular-expression-matching](https://leetcode.com/problems/regular-expression-matching)  | []()  |   |   |
|12   | [word-break](https://leetcode.com/problems/word-break)  | [Backtracking/word-break.py]()  |   |   |
|13  | [word-break-ii](https://leetcode.com/problems/word-break-ii)  | []()  |   |   |
|14   |[wildcard-matching](https://leetcode.com/problems/wildcard-matching)   | [](Python/Backtracking/)  |   |   |
|15   |[letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)   | [](Python/Backtracking/)  |   |   |
|16   |[palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning)   | [](Python/Backtracking/)  |   |   |
|17   |[n-queens](https://leetcode.com/problems/n-queens)   |   |   |   |
|18   |[sudoku-solver](https://leetcode.com/problems/sudoku-solver)   |   |   |   |
|19   |[subsets-ii](https://leetcode.com/problems/subsets-ii)   | [Subsets](Python/Backtracking/subsets-2.py)  |   |   |
|20   |[n-queens-ii](https://leetcode.com/problems/n-queens-ii)   |   |   |   |
|21   | [android-unlock-patterns](https://leetcode.com/problems/android-unlock-patterns)  |   |   |   |
|22   | [permutation-sequence](https://leetcode.com/problems/permutation-sequence)  |   |   |   |

---
### Trie
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   |[Implement trie](https://leetcode.com/problems/implement-trie-prefix-tree/)   | [Solution](Python/Trie/implement-trie.py)   |  Medium |   |
|2   |[design-search-autocomplete-system](https://leetcode.com/problems/design-search-autocomplete-system)   | []()  |   |   |
|3   |[word-search-ii](https://leetcode.com/problems/word-search-ii)   | []()  |   |   |
|4   |[top-k-frequent-words](https://leetcode.com/problems/top-k-frequent-words)   | []()  |   |   |
|5   |[palindrome-pairs](https://leetcode.com/problems/palindrome-pairs)   | []()  |   |   |
|6   |[concatenated-words](https://leetcode.com/problems/concatenated-words)   | []()  |   |   |
|7   |[longest-word-in-dictionary](https://leetcode.com/problems/longest-word-in-dictionary)   | []()  |   |   |
