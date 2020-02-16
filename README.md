# DS-Algo-interview-preparation in Python
<!-- TOC -->

- [DS-Algo-interview-preparation in Python](#ds-algo-interview-preparation-in-python)
  - [Sliding Window](#sliding-window)
  - [Arrays with unique approaches](#arrays-with-unique-approaches)
  - [Math](#math)
  - [Two pointers](#two-pointers)
  - [Fast and slow pointers](#fast-and-slow-pointers)
  - [In-place reverse](#in-place-reverse)
  - [LinkedList](#linkedlist)
  - [Merge Intervals](#merge-intervals)
  - [Cyclic sort](#cyclic-sort)
  - [Modified Binary Search](#modified-binary-search)
  - [Bitwise XOR](#bitwise-xor)
  - [Top K elements (Heap)](#top-k-elements-heap)
  - [K-way merge](#k-way-merge)
  - [Trees](#trees)
  - [Subsets](#subsets)
  - [Graphs](#graphs)
  - [Topological sort](#topological-sort)
  - [Dynamic Programming](#dynamic-programming)
  - [Backtracking](#backtracking)

<!-- /TOC -->


### Sliding Window

[Notes](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Patterns/sliding_window_patterns.md)
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[Max sum subarray of size k/ Max subarray](https://leetcode.com/problems/maximum-subarray/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/max_sum_subarray.py) | Easy | |
| 2   |[Smallest Subarray with a given sum](https://leetcode.com/problems/minimum-size-subarray-sum/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/smallest_sub_array_with_given_sum.py)|  Easy |[Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Notes%20Smallest%20sub%20array%20with%20given%20sum.pdf) |
| 3   |[Longest Substring with at most K Distinct Characters *](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters) | [Sliding window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/Longest_substring_withK_distinct_characters.py) | Hard | |
|4  |[Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)|[Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/fruits_into_baskets.py) | Medium |[Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Fruits_into_baskets.pdf) |
|5  | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/Longest_repeating_character_replacement.py)| Medium | |
|6  | [Permutation in String](https://leetcode.com/problems/permutation-in-string/)|[Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/permutation_in_string.py)| Medium | |
|7  | [Longest Substring Without Repeating Characters ](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [ ]() | | |
|8   | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | [ ]() | Medium | |
|9   | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | []() | Medium | |
|10 | [Minimum Window substring](https://leetcode.com/problems/minimum-window-substring/) | []() || | |
|11  | [Concatenated words](https://leetcode.com/problems/concatenated-words/) | [ ]() | | |
|12  | [Minimum Window substring](https://leetcode.com/problems/) | []() | Hard| |
|13   | [Sliding window maximum](https://leetcode.com/problems/sliding-window-maximum/) | [ ]() | Hard | Use max heap |

### Arrays with unique approaches
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   |[Rotate Image](https://leetcode.com/problems/rotate-image)   | [Matrix transpose](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/UniqueApproach/rotate-image.py)  | Medium  | Reverse rows and swap elements on either side of diagonals  |
|2    |[product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self)   | [Modified two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/UniqueApproach/product_except_self.py)  | Medium  | Left product & right product  |

### Math
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Reverese Integer](https://leetcode.com/problems/reverse-integer/)  |  [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Math/reverse-interger.py) |  Easy |Overflow when the result is greater than 2147483647 or less than -2147483648.   |

### Two pointers
[Notes](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Patterns/two_pointers_patterns.md)

| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[Two sum ](https://leetcode.com/problems/two-sum/) | [Dictionary](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/twosum.py) [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/twosum_sorted.py) | Easy |  |
|2  | [Remove duplicates from sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Two pointers ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/Remove_duplicates_from_sortedarray.py)|Easy |  |
|3   | [3 Sum](https://leetcode.com/problems/3sum/) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/3sum.py) | Medium | |
|4  | [3 Sum closest](https://leetcode.com/problems/3sum-closest/) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/3sum_closest.py) | Medium | |
|5   | [3 Sum smaller](https://leetcode.com/problems/3sum-smaller/) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/3-sum-smaller.py) | Medium | |
|6   | [Squaring of a sorted array](https://leetcode.com/problems/squares-of-a-sorted-array) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/Squares_of_sorted_array.py) |Easy | Insert largest square in the first of the array. list.insert(0,val)|
|7    | [Merge sorted array](https://leetcode.com/problems/merge-sorted-array) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/merge_sorted_array.py) | Easy | |
|8   | [Dutch national flag/Sort colors](https://leetcode.com/problems/sort-colors/) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/dutch_national_flag.py) | | |
|9   | [4sum](https://leetcode.com/problems/4sum) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/4sum.py) | Medium | Extension of 3sum |
|10| [Trapping water](https://leetcode.com/problems/trapping-rain-water)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/trapping_water.py)| Hard | Use left_max and right_max|
|11   | [Backspace string compare](https://leetcode.com/problems/backspace-string-compare/) | [Using stack](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Stack/backspace_string_compare.py) |Easy |  |
|12  |[k-diff-pairs](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/k-diff-pairs-array.py)|Easy| |
|13   | [Shortest unsorted continuous subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | [Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/Shortest-unsorted-continuous-subarray.py) | Easy| |
|14  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Medium||
|15  |[Reverse string](https://leetcode.com/problems/reverse-string)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/reverse_vowels_string.py)| Easy||
|16| [Reverse vowels of a string](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)| Easy ||
|17 | [Move zeros](https://leetcode.com/problems/move-zeroes)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Easy ||
|18  | [Minimum size subarray sum](https://leetcode.com/problems/minimum-size-subarray-sum)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)| Medium| |
|19  | [Candy crush](https://leetcode.com/problems/candy-crush)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Medium | |
|20   | [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/median-sorted-arrays.py) [Binary search](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/median-2sortedarrays.py)|Hard |1. Two pointers is O(n+m).  2. Binary search O(log(min(n,m)) [Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Median-of-2sortedarrays.pdf)|

### Fast and slow pointers
[Notes]()
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Linkedlist cycle](https://leetcode.com/problems/linked-list-cycle) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/linkedlist_cycle.py) | Easy | When slow and fast ptrs meet there is a cycle |
|2   | [Linkedlist cycle 2](https://leetcode.com/problems/linked-list-cycle-ii) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/) | Medium | After checking for a cycle, re-initialize fast ptr to 1st node and increment both slow and fast. The node at which they meet is the start of the cycle |
|3   | [Middle of Linkedlist](https://leetcode.com/problems/middle-of-the-linked-list) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/middle_linkedlist.py) |Easy | The node at which slow ptr stops |
|4   | [Palindrome LL ](https://leetcode.com/problems/palindrome-linked-list) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/palindrome_linkedlist.py) |Medium | Find middle and reverse the 2nd half of the list and compare both|
|5   | [Reorder List](https://leetcode.com/problems/reorder-list/) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/reorder-list.py) | Medium | Find middle, reverse 2nd half and merge one from 1st list and one from 2nd list|
|6   | [Circular array loop](https://leetcode.com/problems/circular-array-loop/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/) | Medium | |

### In-place reverse
[Pattern]()
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Reverse LL](https://leetcode.com/problems/reverse-linked-list) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverseLL.py) |Easy | Use prev and next to update the links |
|2   | [Reverse LL between](https://leetcode.com/problems/reverse-linked-list-ii) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverseLL-between.py) | Medium | loop till k-1th node and reverse |
|3   | [Rotate LL](https://leetcode.com/problems/rotate-list) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/rotateLL.py) | Medium| Move one ptr k times and then move start moving both ptrs. Update next of ptr1 to head and ptr2 to None |
|4   | [Reverse nodes in k-group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverse-nodes-k-groups.py) | Hard | Check if nodes are multiple of k then only reverse |
|5   | Reverse nodes in k-alternating subgroup | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverse-nodes-kgroups-alternatively.py) | Medium | Reverse k groups with a while loop to skip k nodes |

### LinkedList
[pattern]()
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Flatten a multilevel doubly LL](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/flatten_doublylist.py) |Medium | |
|2   | [Odd Even list](https://leetcode.com/problems/odd-even-linked-list) | [Linkedlist](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/oddevenLL.py) | Medium | Initialize even_head & odd_head and update the links. Point the last node of oddlist to even head|
|3   | [Max points on a line](https://leetcode.com/problems/max-points-on-a-line) | [   ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/maxpoints-on-line.py) | Medium| |
|4   | [Copy list with random ptr](https://leetcode.com/problems/copy-list-with-random-pointer) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/copy-list-with-random-pointer.py) | Medium | |
| 5  | [Add two numbers ](https://leetcode.com/problems/add-two-numbers) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/add2numbers.py)|Medium | Take care of carry. Create a new node after adding |
| 6  | [Add two numbers 2](https://leetcode.com/problems/add-two-numbers-ii) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/add-numbers-reverse.py)|Medium | |
| 7  | [Partition list](https://leetcode.com/problems/partition-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/partition-list.py)|Medium | Create two seperate nodes (smaller, larger). Link last of smaller to first of larger|
| 8  | [Plus one LL](https://leetcode.com/problems/plus-one-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/plus-one-LL.py)| Medium | Dummy nodes and move till non nine nodes and increment by 1. Set 9s to 0|
| 9  | [Flatten Binary tree to LL](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/flatten_bt-LL.py)| | |
| 10  | [Insert into a sorted circular LL](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/insert-sorted-circularLL.py)| | |
| 11  | [Convert a binary search tree to sorted doubly LL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/BST-to-sorted-doublyLL.py) | Medium | |
|12  | [Remove Nth node from the end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/remove-nth-node.py)| Medium | create dummy nodes (first & second) move first till k-1th node from start. Now, move both first and second. Second reaches k-1th node from start. Update the next ptr.|
| 13  | [Remove duplicates from LinkedList](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/CyclicSort/)|Medium | |

### Merge Intervals
[Notes](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Patterns/merge-intervals.md)
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Merge intervals](https://leetcode.com/problems/merge-intervals) | [Merge intervals](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/merge_intervals.py)|Medium | |
| 2  |[Non overlapping intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [Merge intervals](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/non-overlapping-intervals.py)| Medium| |
| 3  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections/) | [Merge intervals](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/interval-list-intersections.py)| Medium| |
| 4  |[Meeting rooms ](https://leetcode.com/problems/meeting-rooms) | [Merge intervals](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/meeting-rooms.py)| Easy| |
| 5  |[Meeting rooms 2](https://leetcode.com/problems/meeting-rooms-ii) | [Merge intervals](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/meeting-rooms2.py)| Medium| |
| 6  |[Insert intervals](https://leetcode.com/problems/insert-interval/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/insert-intervals.py)| Hard| |
| 7  | [Employee free time](https://leetcode.com/problems/employee-free-time/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/MergeIntervals/employee-free-time.py)|Hard | |

### Cyclic sort
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Missing number](https://leetcode.com/problems/missing-number/) | [Cyclic sort](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/CyclicSort/)| Easy| n*n+1/2|
| 2  | [Find all missing numbers](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [Cyclic sort](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/CyclicSort/find-all-missing-nos.py)| Medium |index + 1 == nums[index]? |
| 3  |[First missing positive](https://leetcode.com/problems/first-missing-positive/) | [Cyclic sort](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/CyclicSort/first-missing-positive.py)| Hard | TC: O(N), SC: O(1) |


### Modified Binary Search
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Modified binary search](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/find-first-last-in-sortedarray.py)| Medium |  |
| 2  | [single-element-in-a-sorted-array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | [Modified BinarySearch ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/single-num-in-sortedarray.py)| Medium | |
| 3  | [kth Missing element in sorted array](https://leetcode.com/problems/missing-element-in-sorted-array/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/)| Medium | |
| 4  | Search Bitonic Array | [ ]()| | |
| 5  | Bitonic array maximum[]() | [ ]()| | |
| 6  | [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/search-rotated-sortedarray.py)|Medium | |
| 7  | [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [ ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/min-rotated-sortedarray.py)| Medium | 1. O(N) updating minimum  2. O(logN) Binary search|
| 8  | Rotation count | [ ]()| | |
| 9  | Order agnostic binary search | [ ]()| | |



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

### Top K elements (Heap)
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Dictionary](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Heap/top-k-elements.py) []()| Medium | Use dictionary O(nlogn). Quickselect O(N) |
| 2  | [sort-characters-by-frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | [Top k elements](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Heap/sort-characters-freq.py)| Medium | Use dictionary |
| 3 | [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/)   |[Top k elements](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Heap/kth-smallest-in-list.py)   |Medium   | Use heapq  |
| 4  | [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/) | [Top k elements](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/k-closest-elements.py)|Medium | |
| 5  | [maximum-distinct-elements-removing-k-elements](https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/) | [Top k elements]()| | |
| 6  | [reorganize-string](https://leetcode.com/problems/reorganize-string/) | [Top k elements]()| | |
| 7  | [rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [Top k elements]()| | |
| 8  | [task-scheduler](https://leetcode.com/problems/task-scheduler/) | [Top k elements]()| | |
| 9  | [maximum-frequency-stack](https://leetcode.com/problems/maximum-frequency-stack/) | [Top k elements]()| | |

### K-way merge
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) | []()| | |
| 2  | [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | []()| | |
| 3  | [smallest-range-i](https://leetcode.com/problems/smallest-range-i/) | []()| | |
| 4 | [find-k-pairs-with-smallest-sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | []()| | |
| 5  | [partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum/) | []()| | |

### Trees
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1|[Same Tree](https://leetcode.com/problems/same-tree/)|[Recursion](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/same-tree.py)| Easy | |
|2|[Subtree](https://leetcode.com/problems/subtree-of-another-tree/)|[Tree](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/subtree.py)|Easy||
|3|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Recursion](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/diameter.py)|Easy | |
|4|[maximum-depth-of-n-ary-tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[Tree DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/max_depth-nary-tree.py)|Easy | Get the max depth of subtrees|
|5|[maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/max_depth_BT.py)|Easy | |
|6|[range-sum-of-bst](https://leetcode.com/problems/range-sum-of-bst/)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/range_sum.py)|Easy | |
|7|[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/)|[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/merge_BT.py)|Easy | |
|8|[search-in-a-binary-search-tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/search-bst.py)| | |
|9|[path-sum](https://leetcode.com/problems/path-sum/)|[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/path_sum.py)| Easy |  |
|10|[diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Tree](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/diameter-BT.py) | Easy |  |
|11 | [kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Tree DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/kth-smallest.py) | Medium | Push left tree nodes into stack and pop them by decrementing k. when k=0 return node.val  |
|12 | [all-nodes-distance-k-in-binary-tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/nodes-k-distance.py) | Medium |  |
|13 | [lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/lowest_common-ancestor.py) | Medium |  |
|14 |[minimum-depth-of-binary-tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/min_depth_BT.py)|Easy | |
|15 | [serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/) |  |  |
|16 | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/) |  |  |
|17 | [Iterative postorderTraversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)  |[DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/postorder_iterative.py)   | Hard  | Using stack |
|18 | [binary-search-tree-iterator](https://leetcode.com/problems/binary-search-tree-iterator) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/) |  |  |
|19 | [serialize-and-deserialize-bst](https://leetcode.com/problems/serialize-and-deserialize-bst) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/) |  |  |
|20 | [convert-BST-to-sorted-doublyLL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/) |  |  |
|21 | [construct-BT-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 22  | [Valid BST](https://leetcode.com/problems/validate-binary-search-tree/) | [BST](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/valid-bst.py)| Medium| Use lower & upper, initialize them to extremes. Check val <= lower or val>= upper (recursively for all nodes) |
| 23  | [Binary tree level order traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | [Tree BFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BFS/binary-tree-level-order.py)| Medium|Use a queue |
| 24  | [Reverse level order traversal ](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) | [Tree BFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BFS/reverse-level-order-traversal.py)|Medium | |
| 25  | [Zigzag conversion](https://leetcode.com/problems/zigzag-conversion) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| Medium| |
| 26  | [Average of levels in BT](https://leetcode.com/problems/average-of-levels-in-binary-tree) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| Easy | |
| 27  | Next interval | [Tree DFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 28  | [Populating next right ptrs in tree](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 29  | [Binary tree right side view](https://leetcode.com/problems/binary-tree-right-side-view/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 30  | [Tree boundary](https://leetcode.com/problems/boundary-of-binary-tree/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 31  | [ipo](https://leetcode.com/problems/ipo/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)|
| 32  | [Path sum 2](https://leetcode.com/problems/path-sum-ii) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 33  | [Path sum 3](https://leetcode.com/problems/path-sum-iii/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 34  | [Binary tree paths](https://leetcode.com/problems/binary-tree-paths/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 35  | [Diameter of binary tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 36  | [Binary tree maximum path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 37  | [find-median-from-data-stream](https://leetcode.com/problems/find-median-from-data-stream/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |
| 38  | [sliding-window-median](https://leetcode.com/problems/sliding-window-median/) | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/)| | |




### Subsets
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Subsets](https://leetcode.com/problems/subsets/) | [ ]()| | |
| 2  | [Subsets 2](https://leetcode.com/problems/subsets-ii/) | [ ]()| | |
| 3  | [Permutations](https://leetcode.com/problems/permutations) | [ ]()| | |
| 4  | [Letter case permutation](https://leetcode.com/problems/letter-case-permutation/) | [ ]()| | |
| 5  | [Generate parentheses ](https://leetcode.com/problems/generate-parentheses/) | [ ]()| | |
| 6  | [Generalized abbreviation](https://leetcode.com/problems/generalized-abbreviation/) | [  ]()| | |
| 7  | [Evaluate reverse polish notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [ ]()| | |
| 8  | [Uniquie BST](https://leetcode.com/problems/unique-binary-search-trees/) | [ ]()| | |
| 9  | [Unique BST 2](https://leetcode.com/problems/unique-binary-search-trees-ii/) | [ ]()| | |
| 10  | [Next permutation](https://leetcode.com/problems/next-permutation/) | [ ]()|Medium | |

### Graphs
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | Breadth first search  | [Using queue](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/bfs-graph.py)  | Easy  |   |
|2   | Depth first search  |[Recursion](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/dfs-graph.py)   | Easy  |   |
|3   | Detect cycle in a graph  |[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)   | Easy  |   |
|4   | Find mother vertex  | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)  |   |   |
|5   | Count num of edges  | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)  |   |   |
|6   | Path exists   | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)  |   |   |
|7   | Graph is a tree?  |  [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/) |   |   |
|8   | Shortest path between two vertices  |[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)   |   |   |
|9   | Remove Edge  | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)  |   |   |
|10   | [clone-graph](https://leetcode.com/problems/clone-graph)  |  [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/) |   |   |
|11   | [is-graph-bipartite](https://leetcode.com/problems/is-graph-bipartite)  |   |  [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/) |   |
|12   | [evaluate-division](https://leetcode.com/problems/evaluate-division)  |   | [](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Graph/)  |   |

### Topological sort
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [alien-dictionary](https://leetcode.com/problems/alien-dictionary) | [ ]()| | |
| 2  | [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii) | [ ]()| | |
| 3 | [course-schedule](https://leetcode.com/problems/course-schedule) | [ ]()| | |
|  4 | [longest-increasing-path-in-a-matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix) | [ ]()| | |
| 5  | [sort-items-by-groups-respecting-dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies) | [ ]()| | |
| 6  | [sequence-reconstruction](https://leetcode.com/problems/sequence-reconstruction) | [ ]()| | |

### Dynamic Programming
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 2  | [coin-change](https://leetcode.com/problems/coin-change) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 3  | [frog-jump](https://leetcode.com/problems/frog-jump) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 4  | [longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 5  | [word-break](https://leetcode.com/problems/word-break) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 6  | [cherry-pickup](https://leetcode.com/problems/cherry-pickup) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 7  | [decode-ways](https://leetcode.com/problems/decode-ways) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 8  | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 9  | [maximal-rectangle](https://leetcode.com/problems/maximal-rectangle) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 10  | [maximal-square](https://leetcode.com/problems/maximal-square) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 11 | [longest-string-chain](https://leetcode.com/problems/longest-string-chain) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 12 | [regular-expression-matching](https://leetcode.com/problems/regular-expression-matching) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 13  | [longest-valid-parentheses](https://leetcode.com/problems/longest-valid-parentheses) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 14  | [burst-balloons](https://leetcode.com/problems/burst-balloons) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 15  | [word-break-ii](https://leetcode.com/problems/word-break-ii) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 16  | [edit-distance)](https://leetcode.com/problems/edit-distance) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 17  | [interleaving-string](https://leetcode.com/problems/interleaving-string) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 18  | [wildcard-matching](https://leetcode.com/problems/wildcard-matching) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 19  | [split-array-largest-sum](https://leetcode.com/problems/split-array-largest-sum) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 20  | [climbing-stairs](https://leetcode.com/problems/climbing-stairs) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 21  | [concatenated-words](https://leetcode.com/problems/concatenated-words) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 22  | [palindromic-substrings](https://leetcode.com/problems/palindromic-substrings) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 23  | [longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence) | [ Iterative DP ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/longest-increasing-subsequence.py)| Medium | Use an array to store the longest sequence|
| 24  | [house-robber](https://leetcode.com/problems/house-robber) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 25  | [paint-house](https://leetcode.com/problems/paint-house) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 26  | [cheapest-flights-within-k-stops](https://leetcode.com/problems/cheapest-flights-within-k-stops) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 27  | [maximum-product-subarray](https://leetcode.com/problems/maximum-product-subarray) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 28  | [unique-binary-search-trees](https://leetcode.com/problems/unique-binary-search-trees) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 29  | [super-egg-drop](https://leetcode.com/problems/super-egg-drop) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 30  | [minimum-path-sum](https://leetcode.com/problems/minimum-path-sum) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 31  | [longest-arithmetic-sequence](https://leetcode.com/problems/longest-arithmetic-sequence) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 32  | [delete-and-earn](https://leetcode.com/problems/delete-and-earn) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 33  | [continuous-subarray-sum](https://leetcode.com/problems/continuous-subarray-sum) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 34  | [best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 35  | [knight-dialer](https://leetcode.com/problems/knight-dialer) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 36  | [shortest-way-to-form-string](https://leetcode.com/problems/shortest-way-to-form-string) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 37  | [unique-paths](https://leetcode.com/problems/unique-paths) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 38  | [best-time-to-buy-and-sell-stock-iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 39  | [range-sum-query-2d-immutable](https://leetcode.com/problems/range-sum-query-2d-immutable) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 40  | [partition-to-k-equal-sum-subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 41  | [count-vowels-permutation](https://leetcode.com/problems/count-vowels-permutation) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 42  | [minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 43  | [unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 44  | [best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | [  ]()| | |
| 45  | [longest-palindromic-subsequence](https://leetcode.com/problems/longest-palindromic-subsequence) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 46  | [longest-common-subsequence](https://leetcode.com/problems/longest-common-subsequence) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 47  | [tiling-a-rectangle-with-the-fewest-squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 48  | [dice-roll-simulation](https://leetcode.com/problems/dice-roll-simulation) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 49  | [max-sum-of-rectangle-no-larger-than-k](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 50  | [minimum-cost-to-merge-stones](https://leetcode.com/problems/minimum-cost-to-merge-stones) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 51  | [perfect-squares](https://leetcode.com/problems/perfect-squares) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 52  | [maximum-length-of-repeated-subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 53  | [knight-probability-in-chessboard](https://leetcode.com/problems/knight-probability-in-chessboard) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 54  | [count-different-palindromic-subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |
| 55  | [best-time-to-buy-and-sell-stock-with-transaction-fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | [  ]()| | |
| 56  | [minimum-swaps-to-make-sequences-increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing) | [  ](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/DynamicProgramming/)| | |


###  Backtracking
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1  |[generate-parentheses](https://leetcode.com/problems/generate-parentheses)|[ ]()|||
|2  |[letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)|[ ]()|||
|3  |[word-search](https://leetcode.com/problems/word-search)|[ ]()|||
|4  |[permutation](https://leetcode.com/problems/permutations)|[ ]()|||
|5  |[regular-expression-matching](https://leetcode.com/problems/regular-expression-matching)|[ ]()|||
|6  |[word-search-ii](https://leetcode.com/problems/word-search-ii)|[ ]()|||
|7  |[word-break-ii](https://leetcode.com/problems/word-break-ii)|[ ]()|||
|8  |[restore-ip-addresses](https://leetcode.com/problems/restore-ip-addresses)|[ ]()|||
|9  |[wildcard-matching](https://leetcode.com/problems/wildcard-matching))|[ ]()|||
|10  |[word-ladder-ii](https://leetcode.com/problems/word-ladder-ii)|[ ]()|||
|11  |[subsets](https://leetcode.com/problems/subsets)|[ ]()|||
|12  |[combination-sum](https://leetcode.com/problems/combination-sum)|[ ]()|||
|13  |[sudoku-solver](https://leetcode.com/problems/sudoku-solver)|[ ]()|||
|14  |[n-queens](https://leetcode.com/problems/n-queens)|[ ]()|||
|15  |[add-and-search-word-data-structure-design](https://leetcode.com/problems/add-and-search-word-data-structure-design)|[ ]()|||
|16  |[tiling-a-rectangle-with-the-fewest-squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares)|[ ]()|||
|17  |[permutations-ii](https://leetcode.com/problems/permutations-ii)|[ ]()|||
|18  |[unique-paths-iii](https://leetcode.com/problems/unique-paths-iii)|[ ]()|||
|19  |[palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning)|[ ]()|||
|20  |[word-pattern-ii](https://leetcode.com/problems/word-pattern-ii)|[ ]()|||
|21  |[beautiful-arrangement](https://leetcode.com/problems/beautiful-arrangement)|[ ]()|||
|22  |[factor-combinations](https://leetcode.com/problems/factor-combinations)|[ ]()|||
|23  |[confusing-number-ii](https://leetcode.com/problems/confusing-number-ii)|[ ]()|||
|24  |[combinations](https://leetcode.com/problems/combinations)|[ ]()|||
|25  |[combination-sum-ii](https://leetcode.com/problems/combination-sum-ii)|[ ]()|||
|26  |[path-with-maximum-gold](https://leetcode.com/problems/path-with-maximum-gold)|[ ]()|||
|27  |[campus-bikes-ii](https://leetcode.com/problems/campus-bikes-ii)|[ ]()|||
|28  |[brace-expansion](https://leetcode.com/problems/brace-expansion)|[ ]()|||
|29  |[android-unlock-patterns](https://leetcode.com/problems/android-unlock-patterns)|[ ]()|||
|30  |[n-queens-ii](https://leetcode.com/problems/n-queens-ii)|[ ]()|||
