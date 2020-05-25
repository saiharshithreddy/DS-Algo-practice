# Coding interview-preparation

![Language](https://img.shields.io/badge/language-Python%20-orange.svg)&nbsp;
![Progress](https://img.shields.io/badge/progress-310%20%2F%20350-green4.svg)&nbsp;


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

<!-- TOC -->

- [Coding interview-preparation](#coding-interview-preparation)

  - [Arrays](#arrays)
  - [Matrix](#matrix)
  - [Strings](#strings)
  - [Math](#math)
  - [TwoPointers](#twopointers)
  - [Stack](#stack)
  - [Greedy](#greedy)
  - [DesignQuestions](#designquestions)
  - [LinkedList](#linkedlist)
  - [SlidingWindow](#slidingwindow)
  - [Merge_Intervals](#merge_intervals)
  - [CyclicSort](#cyclicsort)
  - [BinarySearch](#binarysearch)
  - [Heap](#heap)
  - [Tree](#tree)
  - [DFS](#dfs)
  - [BFS](#bfs)
  - [Graphs](#graphs)
  - [TopologicalSort](#topologicalsort)
  - [DynamicProgramming](#dynamicprogramming)
  - [Backtracking](#backtracking)
  - [Trie](#trie)

<!-- /TOC -->

### Arrays
| #   |Question| Solution |Difficulty | Tags |Notes |
| -|----- | ---------- |-----|-------|----|
|1    |[product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self)   | [Modified two pointers](Python/Arrays/product_except_self.py)  | Medium  |```Array``` ```Two pointers```|Follow up: O(N) Left product & right product  |
|2   | [Right rotate array](https://leetcode.com/problems/rotate-array/)  | [Reverse array](Python\Arrays\right_rotate.py)  | Easy  |   |   |
| 3| [find all numbers disappeared in an array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array) |[Arrays](Python/Arrays/find-all-numbers-disappeared-in-an-array.py) |Easy |  | |
| 4| [find-all-duplicates-in-an-array](https://leetcode.com/problems/find-all-duplicates-in-an-array) |[Arrays](Python/Arrays/find-all-duplicates-in-an-array.py) |Medium| | Hint: Multiply -1 to the num at index (A[i]-1) |
| 5| [subarray-sum-equals-k](https://leetcode.com/problems/subarray-sum-equals-k) :star:|[Arrays](Python/Arrays/subarray-sum-equals-k.py) |Medium|```hashmap``` | |
| 6| [max consecutive ones](https://leetcode.com/problems/max-consecutive-ones) |[Arrays](Python/Arrays/max-consecutive-ones.py) |Easy| | |
| 7| [majority element](https://leetcode.com/problems/majority-element) |[Arrays](Python/Arrays/majority-element.py) |Easy| ```boyre moore voting```| |
| 8| [analyze user website visit pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern) |[Arrays](Python/Arrays/analyze-user-website-visit-pattern.py) |Medium |  | |
| 9| [maximum swap](https://leetcode.com/problems/maximum-swap) |[Arrays](Python/Arrays/maximum-swap.py) |Medium |  | |


---



### Matrix
| #   |Question| Solution |Difficulty | Tags |Notes |
| -|----- | ---------- |-----|-------|----|
|1   |[Spiral matrix](https://leetcode.com/problems/spiral-matrix)   |[Arrays](Python/Matrix/spiral-matrix.py)   | Medium  | ```Matrix``` | |
|2   |[Search in 2D matrix](https://leetcode.com/problems/search-a-2d-matrix-ii)   |[Matrix](Python/Matrix/search-in-2d-matrix.py)   |  Medium | ```BinarySearch``` ```Matrix``` | Tweak: Instead of performing a binary search check if the last row's first val is greater or lesser than the target|
|3   |[Game of life](https://leetcode.com/problems/game-of-life/)   |[Array](Python/Matrix/game-of-life.py)   |  Medium | ```Matrix```||
|4  |[Rotate Image](https://leetcode.com/problems/rotate-image)   | [Matrix transpose](Python/Matrix/rotate-image.py)  | Medium  |```Matrix```| Reverse rows and swap elements on either side of diagonals  |
|5   | [Diagonal traverse](https://leetcode.com/problems/diagonal-traverse)  | [Matrix](Python/Matrix/diagonal-traverse.py)  |  Medium  |  ```Matrix``` ```deque```|   |
|6   | [Set matrix to zeros](https://leetcode.com/problems/set-matrix-zeroes)  | [Matrix](Python/Matrix/set-matrix-zeroes.py)  | Medium   | ```Matrix```  | Get the position of 0s in the matrix and in another iteration update the values  |
|7   | [Generate spiral matrix](https://leetcode.com/problems/spiral-matrix-ii)  | [Matrix](Python/Matrix/spiral-matrix2.py)  | Medium  | ```Matrix```  | Similar to spiral matrix  |
| 8| [sort the matrix diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally) |[Matrix](Python/Matrix/sort-the-matrix-diagonally.py) |Medium| | Hint: Any Diagonal elemements i-j is 0 |


---

### Strings
| #   |Question| Solution |Difficulty | Tags |Notes |
| -|----- | ---------- |-----|-------|----|
| 1| [group-anagrams](https://leetcode.com/problems/group-anagrams.py) |[String](Python/String/group-anagrams.py) |Medium| | |
| 2| [reverse words in a string](https://leetcode.com/problems/reverse-words-in-a-string) |[Strings](Python/Strings/reverse-words-in-a-string.py) |Medium| ```Two pointers``` | |
| 3| [longest palindromic substring](https://leetcode.com/problems/longest-palindromic-substring) |[Strings](Python/Strings/longest-palindromic-substring.py) |Medium |  | |





---

### Math
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [Reverese Integer](https://leetcode.com/problems/reverse-integer/)  |  [Math](Python/Math/reverse-integer.py) |  Easy | |In Java, Overflow when the result is greater than 2147483647 or less than -2147483648.  not in Python |
|2   | [fraction-to-recurring-decimal](https://leetcode.com/problems/fraction-to-recurring-decimal)  | []()  |   |  | |
|3   | [roman-to-integer](https://leetcode.com/problems/roman-to-integer)  | []()  |   |   ||
|4   | [divide-two-integers](https://leetcode.com/problems/divide-two-integers)  | []()  |   ||   |
|5   | [powx-n](https://leetcode.com/problems/powx-n)  | []()  |   |   ||
| -2| [perfect squares](https://leetcode.com/problems/perfect-squares) |[DynamicProgramming](Python/DynamicProgramming/perfect-squares.py) |Medium |  | |
|7   | [excel-sheet-column-number](https://leetcode.com/problems/excel-sheet-column-number)  | []()  |   |   ||
| 8| [sqrtx](https://leetcode.com/problems/sqrtx) |[BinarySearch](Python/BinarySearch/sqrtx.py) |Easy| | |
|9   | [factorial-trailing-zeroes](https://leetcode.com/problems/factorial-trailing-zeroes)  | []()  |   |   ||
| 10| [count primes](https://leetcode.com/problems/count-primes) |[Math](Python/Math/count-primes.py) |Easy | ```sieve_of_erathenoses```| |
|11   | [Max points on a line](https://leetcode.com/problems/max-points-on-a-line) | [   ](Python/LinkedList/maxpoints-on-line.py) | Hard| | |

---

### TwoPointers
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  |[Two sum ](https://leetcode.com/problems/two-sum/) | [Dictionary](Python/TwoPointers/twosum.py) <br> [Two pointers](Python/TwoPointers/twosum_sorted.py) | Easy |  ||
| 2  | [Two sum less than k](https://leetcode.com/problems/two-sum-less-than-k/)  | [Two pointers](Python/TwoPointers/twosum-lessthanK.py)  | Easy  |   ||
|3   | [3 Sum](https://leetcode.com/problems/3sum/) | [Two pointers](Python/TwoPointers/3sum.py) | Medium | ||
|4  | [3 Sum closest](https://leetcode.com/problems/3sum-closest/) | [Two pointers](Python/TwoPointers/3sum_closest.py) | Medium | ||
|5   | [3 Sum smaller](https://leetcode.com/problems/3sum-smaller/) | [Two pointers](Python/TwoPointers/3-sum-smaller.py) | Medium | ||
|6   | [Squaring of a sorted array](https://leetcode.com/problems/squares-of-a-sorted-array) | [Two pointers](Python/TwoPointers/Squares_of_sorted_array.py) |Easy || Insert largest square in the first of the array. list.insert(0,val)|
|7    | [Merge sorted array](https://leetcode.com/problems/merge-sorted-array) | [Two pointers](Python/TwoPointers/merge_sorted_array.py) | Easy | ||
|8   | [Dutch national flag/Sort colors](https://leetcode.com/problems/sort-colors/) | [Two pointers](Python/TwoPointers/dutch_national_flag.py) | | ||
|9   | [4sum](https://leetcode.com/problems/4sum) | [Two pointers](Python/TwoPointers/4sum.py) | Medium || Extension of 3sum |
|10| [Trapping water](https://leetcode.com/problems/trapping-rain-water)|[Two pointers](Python/TwoPointers/trapping_water.py)| Hard |```Two pointers``` <br> ```Stack```| Use left_max and right_max|
|11   | [Backspace string compare](https://leetcode.com/problems/backspace-string-compare/) | [Using stack](Python/Stack/backspace_string_compare.py) |Easy |  ||
|12  |[k-diff-pairs](https://leetcode.com/problems/k-diff-pairs-in-an-array/)|[Two pointers](Python/TwoPointers/k-diff-pairs-array.py)|Easy| | |
|13   | [Shortest unsorted continuous subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | [Two pointers](Python/TwoPointers/Shortest-unsorted-continuous-subarray.py) | Easy| ||
|14  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections)|[](Python/TwoPointers/)|Medium|||
|15  |[Reverse string](https://leetcode.com/problems/reverse-string)|[Two pointers](Python/TwoPointers/reverse_vowels_string.py)| Easy|||
|16| [Reverse vowels of a string](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[ ](Python/TwoPointers/)| Easy |||
|17 | [Move zeros](https://leetcode.com/problems/move-zeroes)|[Two pointers](Python/TwoPointers/move_zeroes.py)|Easy |  ||
|18  | [Remove duplicates from sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Two pointers ](Python/TwoPointers/Remove_duplicates_from_sortedarray.py)|Easy |  ||
|19  | [Candy crush](https://leetcode.com/problems/candy-crush)|[](Python/TwoPointers/)|Medium | ||
|20   | [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Two pointers](Python/TwoPointers/median-sorted-arrays.py) [Binary search](Python/BinarySearch/median-2sortedarrays.py)|Hard ||1. Two pointers is O(n+m)<br>  2. Binary search O(log(min(n,m)) [Algo](Notes/Median-of-2sortedarrays.pdf)|
| 21| [valid-triangle-number](https://leetcode.com/problems/valid-triangle-number) |[TwoPointers](Python/TwoPointers/valid-triangle-number.py) |Medium|```BinarySearch``` ```TwoPointers``` | Similar to 3 sum closest |

---

### Stack
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [Daily temperatures](https://leetcode.com/problems/daily-temperatures) :star: | [Stack](Python/Stack/daily-temperatures.py)  |  Medium |```MDS``` | logic: Next greater element in a stack, Store (day, temp) in stack  |
|2   | Evaluate Postfix Expression Using a Stack  | []()  |   |   |
| 3| [next greater element i](https://leetcode.com/problems/next-greater-element-i) |[Stack](Python/Stack/next-greater-element-i.py) |Easy|```MDS``` | |
| 4| [next greater element ii](https://leetcode.com/problems/next-greater-element-ii) |[Stack](Python/Stack/next-greater-element-ii.py) |Medium| ```MDS```| |
| 5| [132 pattern](https://leetcode.com/problems/132-pattern) |[Stack](Python/Stack/132-pattern.py) |Medium| | |
| 6| [basic calculator](https://leetcode.com/problems/basic-calculator) :star: |[Stack](Python/Stack/basic-calculator.py) |Hard| | |
| 7| [minimum remove to make valid parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses) |[Stack](Python/Stack/minimum-remove-to-make-valid-parentheses.py) |Medium| | |
| 8| [basic calculator ii](https://leetcode.com/problems/basic-calculator-ii) |[Stack](Python/Stack/basic-calculator-ii.py) |Hard| | |
| 9|[remove k digits](https://leetcode.com/problems/remove-k-digits) |[Stack](Python/Stack/remove-k-digits.py) |Medium | ```MIS```| |
| 10| [minimum add to make parentheses valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid) |[Stack](Python/Stack/minimum-add-to-make-parentheses-valid.py) |Medium| | |


---

### Greedy
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1| [walking robot simulation](https://leetcode.com/problems/walking-robot-simulation) |[Greedy](Python/Greedy/walking-robot-simulation.py) |Easy| | |


### DesignQuestions
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [Design lru-cache](https://leetcode.com/problems/lru-cache) :star: | [Solution](Python/DesignQuestions/LRUcache.py)  | Medium|  | Use doubly LL  and hashmap |
|2   | [insert-delete-getrandom-o1](https://leetcode.com/problems/insert-delete-getrandom-o1)  | [Solution](Python/DesignQuestions/insert-getrandom.py)  | Medium  |   ||
|3   | [min-stack](https://leetcode.com/problems/min-stack)  | [Solution](Python/DesignQuestions/min-stack.py)  | Easy  |   ||
|4   | [MaxStack](https://leetcode.com/problems/max-stack/)  | [Solution](Python/DesignQuestions/max-stack.py)  | Easy  |   ||
|5   | [Design stack with increment operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/)  | [Solution](Python/DesignQuestions/stack-with-increment.py)  | Medium  |   ||
|6   | [lfu-cache](https://leetcode.com/problems/lfu-cache)  | []()  |   |   ||
|7   | [design-tic-tac-toe](https://leetcode.com/problems/design-tic-tac-toe)  | []()  |   |   ||
|8   | [design-in-memory-file-system](https://leetcode.com/problems/design-in-memory-file-system)  | []()  |   |   ||
|9   | [design-hashmap :star:](https://leetcode.com/problems/design-hashmap/)  | [Solution](Python/DesignQuestions/Design_Hashmap.py)  | Medium  | ||
|10 | [Design HashSet](https://leetcode.com/problems/design-hashset) :star:|[]() | | ||
|11   |[design-hit-counter](https://leetcode.com/problems/design-hit-counter)   |   |   |   ||
|12   |[add-and-search-word-data-structure-design](https://leetcode.com/problems/add-and-search-word-data-structure-design)   |   |   |   ||
|13   |[design-log-storage-system](https://leetcode.com/problems/design-log-storage-system)   |   |   |   ||
|14   |[design-circular-queue](https://leetcode.com/problems/design-circular-queue)   |   |   |   ||
|15   |[design-file-system](https://leetcode.com/problems/design-file-system)   |   |   |   ||
|16   |[implement-stack-using-queues](https://leetcode.com/problems/implement-stack-using-queues)   |   |   |   ||
|17   |[design-skiplist](https://leetcode.com/problems/design-skiplist)   |   |   |   ||
|18   |[design-circular-deque](https://leetcode.com/problems/design-circular-deque)   |   |   |   ||
|19   |[design-linked-list](https://leetcode.com/problems/design-linked-list)   |   |   |   ||
|20   |[time-based-key-value-store](https://leetcode.com/problems/time-based-key-value-store/)   |   |   |   ||
|21   |[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) :star:  | [Solution](Python\DesignQuestions\implement-queue-two-stacks.py)  | Easy  |   ||

---

### LinkedList
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [Linkedlist cycle](https://leetcode.com/problems/linked-list-cycle) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/linkedlist_cycle.py) | Easy | |When slow and fast ptrs meet there is a cycle |
|2   | [Linkedlist cycle 2](https://leetcode.com/problems/linked-list-cycle-ii) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/) | Medium | |After checking for a cycle, re-initialize fast ptr to 1st node and increment both slow and fast. The node at which they meet is the start of the cycle |
|3   | [Middle of Linkedlist](https://leetcode.com/problems/middle-of-the-linked-list) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/middle_linkedlist.py) |Easy | |The node at which slow ptr stops |
|4   | [Palindrome LL ](https://leetcode.com/problems/palindrome-linked-list) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/palindrome_linkedlist.py) |Medium || Find middle and reverse the 2nd half of the list and compare both|
|5   | [Reorder List](https://leetcode.com/problems/reorder-list/) | [Fast & slow ptrs](Python/Fast_and_slow_pointers/reorder-list.py) | Medium | |Find middle, reverse 2nd half and merge one from 1st list and one from 2nd list|
|6   | [Reverse LL](https://leetcode.com/problems/reverse-linked-list) | [In-place reverse](Python/LinkedList/reverseLL.py) |Easy || Use prev and next to update the links |
|7   | [Reverse LL between](https://leetcode.com/problems/reverse-linked-list-ii) | [In-place reverse](Python/LinkedList/reverseLL-between.py) | Medium ||loop till k-1th node and reverse |
|8   | [Rotate LL](https://leetcode.com/problems/rotate-list) | [In-place reverse](Python/LinkedList/rotateLL.py) | Medium| |Move one ptr k times and then move start moving both ptrs. Update next of ptr1 to head and ptr2 to None |
|9   | [Reverse nodes in k-group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [In-place reverse](Python/LinkedList/reverse-nodes-k-groups.py) | Hard | |Check if nodes are multiple of k then only reverse |
|10   | Reverse nodes in k-alternating subgroup | [In-place reverse](Python/LinkedList/reverse-nodes-kgroups-alternatively.py) | Medium|| Reverse k groups with a while loop to skip k nodes |
|11   | [Swap nodes in pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)  | [In-place reverse](Python\LinkedList\swap-nodes-in-pairs.py)  | Medium  | ||
|12   | [Flatten a multilevel doubly LL](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) | [ ](Python/LinkedList/flatten_doublylist.py) |Medium | ||
|13   | [Odd Even list](https://leetcode.com/problems/odd-even-linked-list) | [Linkedlist](Python/LinkedList/oddevenLL.py) | Medium || Initialize even_head & odd_head and update the links. Point the last node of oddlist to even head|
|14  | [Sort list](https://leetcode.com/problems/sort-list)  | []()  | Medium  | |Merge sort  |
|15   | [Copy list with random ptr](https://leetcode.com/problems/copy-list-with-random-pointer) | [hashmap ](Python/LinkedList/copy-list-with-random-ptr.py) | Medium |```hashmap``` | |
| 16  | [Add two numbers ](https://leetcode.com/problems/add-two-numbers) :star: | [Linked List](Python/LinkedList/add2numbers.py)|Medium| | Take care of carry. Create a new node after adding |
| 17  | [Add two numbers 2](https://leetcode.com/problems/add-two-numbers-ii) | [Linked List](Python/LinkedList/add-numbers-reverse.py)|Medium | ||
| 18  | [Partition list](https://leetcode.com/problems/partition-list) | [Linked List](Python/LinkedList/partition-list.py)|Medium | |Create two seperate nodes (smaller, larger). Link last of smaller to first of larger|
| 19  | [Plus one LL](https://leetcode.com/problems/plus-one-linked-list) | [Linked List](Python/LinkedList/plus-one-LL.py)| Medium || Dummy nodes and move till non nine nodes and increment by 1. Set 9s to 0|
| 20  | [Insert into a sorted circular LL](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list) | [ ](Python/LinkedList/insert-sorted-circularLL.py)| | ||
|21  | [Remove Nth node from the end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Linked List](Python/LinkedList/remove-nth-node.py)| Medium| | create dummy nodes (first & second) move first till k-1th node from start. Now, move both first and second. Second reaches k-1th node from start. Update the next ptr.|
| 22  | [Remove duplicates from LinkedList](https://leetcode.com/problems/remove-duplicates-from-sorted-list) | [Linked List ](Python/LinkedList/remove-dup.py)|Easy | ||
| 23  | [Remove duplicates from LinkedList 2](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | [Linked List ](Python/LinkedList/remove-dup-2.py)|Medium | ||


---

### SlidingWindow
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  |[Max sum subarray of size k/ Max subarray](https://leetcode.com/problems/maximum-subarray/)| [Sliding Window](Python/SlidingWindow/max_sum_subarray.py) | Easy | ||
| 2   |[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)| [Sliding Window](Python/SlidingWindow/smallest_sub_array_with_given_sum.py)|  Easy | |[Algo](Notes/Notes%20Smallest%20sub%20array%20with%20given%20sum.pdf) |
| 3| [longest-substring-with-at-most-k-distinct-characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters) :star:|[SlidingWindow](Python/SlidingWindow/longest-substring-with-at-most-k-distinct-characters.py) |Hard| | |
|4  |[Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)|[Sliding Window](Python/SlidingWindow/fruits_into_baskets.py) | Medium |```array``` |[Algo](Notes/Fruits_into_baskets.pdf) |
|5  | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)| [Sliding Window](Python/SlidingWindow/Longest_repeating_character_replacement.py)| Medium |```Hashmap``` | |
| 6| [permutation in string](https://leetcode.com/problems/permutation-in-string) |[SlidingWindow](Python/SlidingWindow/permutation-in-string.py) |Medium|```Hashmap``` ```Two strings``` | |
|7  | [Longest Substring Without Repeating Characters ](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Sliding Window ](Python/SlidingWindow/longest-substring-without-repeating-characters.py) |Medium | | |
| 8| [max consecutive ones iii](https://leetcode.com/problems/max-consecutive-ones-iii) |[SlidingWindow](Python/SlidingWindow/max-consecutive-ones-iii.py) |Medium| | |
| 9| [find all anagrams in a string](https://leetcode.com/problems/find-all-anagrams-in-a-string) :star:|[SlidingWindow](Python/SlidingWindow/find-all-anagrams-in-a-string.py) |Medium|```Hashmap``` ```Two strings``` | |
| 10| [minimum window substring](https://leetcode.com/problems/minimum-window-substring) |[SlidingWindow](Python/SlidingWindow/minimum-window-substring.py) |Hard| | |
| 11| [substring with concatenation of all words](https://leetcode.com/problems/substring-with-concatenation-of-all-words) |[SlidingWindow](Python/SlidingWindow/substring-with-concatenation-of-all-words.py) |Hard| | |
| 12| subarrays-with-at-most-k-different-integers |[SlidingWindow](Python/SlidingWindow/subarrays-with-at-most-k-different-integers.py) |Medium| | |
| 13| [count-number-of-nice-subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays) |[SlidingWindow](Python/SlidingWindow/count-number-of-nice-subarrays.py) |Medium| | |
|14   | [consecutive-numbers-sum](https://leetcode.com/problems/consecutive-numbers-sum/)  | [Sliding window & Math](Python/SlidingWindow/consecutive-numbers-sum.py)  | Hard  |   | |
| 15| [grumpy bookstore owner](https://leetcode.com/problems/grumpy-bookstore-owner) |[SlidingWindow](Python/SlidingWindow/grumpy-bookstore-owner.py) |Medium| | |
| 16| [binary-subarrays-with-sum](https://leetcode.com/problems/binary-subarrays-with-sum) |[SlidingWindow](Python/SlidingWindow/binary-subarrays-with-sum.py) |Medium| ```atmostK - atmostk-1 concept``` | |

| 18| [subarrays-with-k-different-integers](https://leetcode.com/problems/subarrays-with-k-different-integers) |[SlidingWindow](Python/SlidingWindow/subarrays-with-k-different-integers.py) |Hard| | |
|19   | [number-of-submatrices-that-sum-to-target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)  |   ||   |   |
|20   | [subarray-product-less-than-k](https://leetcode.com/problems/subarray-product-less-than-k/)  :star:| [Sliding Window](Python/SlidingWindow/subarray_prod_less_thanK.py)  | Medium  |   ||
| 21| [longest-substring-with-at-most-two-distinct-characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters) |[SlidingWindow](Python/SlidingWindow/longest-substring-with-at-most-two-distinct-characters.py) |Medium| | |
| 22| subarrays-with-at-most-k-different-integers |[SlidingWindow](Python/SlidingWindow/subarrays-with-at-most-k-different-integers.py) |Medium| | |






---

### Merge_Intervals
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  | [Merge intervals](https://leetcode.com/problems/merge-intervals) :star: | [Merge intervals](Python/MergeIntervals/merge_intervals.py)|Medium |```sort``` | |
| 2  |[Non overlapping intervals](https://leetcode.com/problems/non-overlapping-intervals/) :star:| [Merge intervals](Python/MergeIntervals/non-overlapping-intervals.py)| Medium|```sort``` | |
| 3  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections/) | [Merge intervals](Python/MergeIntervals/interval-list-intersections.py)| Medium|```sort``` | |
| 4  |[Meeting rooms ](https://leetcode.com/problems/meeting-rooms) | [Merge intervals](Python/MergeIntervals/meeting-rooms.py)| Easy|```sort``` | |
| 5  |[Meeting rooms 2](https://leetcode.com/problems/meeting-rooms-ii) :star: | [Merge intervals](Python/MergeIntervals/meeting-rooms2.py)| Medium|```sort``` | |
| 6  |[Insert intervals](https://leetcode.com/problems/insert-interval/) | [Merge intervals ](Python/MergeIntervals/insert-intervals.py)| Hard|```sort``` | |
| 7  | [Employee free time](https://leetcode.com/problems/employee-free-time/) | [ ](Python/MergeIntervals/employee-free-time.py)|Hard |```sort``` | |



---
### CyclicSort
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  | [Missing number](https://leetcode.com/problems/missing-number/) | [Cyclic sort](Python/CyclicSort/)| Easy| | n*n+1/2|
| 2  |[First missing positive](https://leetcode.com/problems/first-missing-positive/) | [Cyclic sort](Python/CyclicSort/first-missing-positive.py)| Hard | | Works only for 1 - N range numbers. TC: O(N), SC: O(1) |



---
### BinarySearch
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  | [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Modified binary search](Python/BinarySearch/find-first-last-in-sortedarray.py)| Medium |  | |
| 2  | [single-element-in-a-sorted-array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | [Modified BinarySearch ](Python/BinarySearch/single-num-in-sortedarray.py)| Medium | | |
| 3  | [kth Missing element in sorted array](https://leetcode.com/problems/missing-element-in-sorted-array/) | [ ](Python/)| Medium | |
| 4  | Search Bitonic Array | [ ]()| | | |
| 5  | Bitonic array maximum[]() | [ ]()| | | |
| 6  | [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) :star: | [Modified BinarySearch ](Python/BinarySearch/search-rotated-sortedarray.py) :star:|Medium | | |
| 7  | [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Modified BinarySearch ](Python/BinarySearch/min-rotated-sortedarray.py)| Medium | |1. O(N) updating minimum    2. O(logN) Binary search|
|8   | [Search in rotated sorted array with duplicates ](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)  | []()  |  Medium |   | |
|9   | [Find min in rotated sorted array with duplicates](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)  | []()  | Hard   |   | |
| 10  | [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/) | [Solution](Python/BinarySearch/k-closest-elements.py)|Medium |```1. BS with heap``` <br> ```2. BS with 2 pts``` | 1. O(logN + klogk) <br> 2. O(logN + k)|
| 11| [first-bad-version](https://leetcode.com/problems/first-bad-version) |[BinarySearch](Python/BinarySearch/first-bad-version.py) |Easy| | |
| 12| [search-insert-position](https://leetcode.com/problems/search-insert-position) |[BinarySearch](Python/BinarySearch/search-insert-position.py) |Easy| | |
| 13| [valid-triangle-number](https://leetcode.com/problems/valid-triangle-number) |[TwoPointers](Python/TwoPointers/valid-triangle-number.py) |Medium| | |
| 14| [valid-perfect-square](https://leetcode.com/problems/valid-perfect-square) |[BinarySearch](Python/BinarySearch/valid-perfect-square.py) |Easy| | |
| 15| [sqrtx](https://leetcode.com/problems/sqrtx) |[BinarySearch](Python/BinarySearch/sqrtx.py) |Easy| | |
| 16| [search-insert-position](https://leetcode.com/problems/search-insert-position) |[BinarySearch](Python/BinarySearch/search-insert-position.py) |Easy| | |
| 17| [find peak element](https://leetcode.com/problems/find-peak-element) |[BinarySearch](Python/BinarySearch/find-peak-element.py) |Medium| | |
| 18| [find peak element in matrix](https://www.geeksforgeeks.org/find-peak-element-2d-array/) |[BinarySearch](Python/BinarySearch/find-peak-element-in-matrix.py) |Medium |  | |

---

### Heap
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) :star: | [Heap](Python/Heap/top-k-elements.py) | Medium | | Use dictionary O(nlogn). Quickselect O(N) |
| 2  | [sort-characters-by-frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | [Top k elements](Python/Heap/sort-characters-freq.py)| Medium | | Use dictionary |
| 3 | [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/)   |[Top k elements](Python/Heap/kth-smallest-in-list.py)   |Medium    | | Use heapq  |
| 4| [maximum frequency stack](https://leetcode.com/problems/maximum-frequency-stack) |[Stack](Python/Stack/maximum-frequency-stack.py) |Hard| | |
| 5  | [maximum-distinct-elements-removing-k-elements](https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/) | [Top k elements]()| | | |
| 6  | [reorganize-string](https://leetcode.com/problems/reorganize-string/) :star: | [Heap](Python\Heap\reorganize-strings.py)|Medium | | |
| 7  | [rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [Top k elements]()| | | |
| 8  | [task-scheduler](https://leetcode.com/problems/task-scheduler/) | [Top k elements]()| | | |
|9   | [kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)  | [Heap](Python\Heap\kth-largest-element-in-stream.py)  | Easy  |   | |
|10   |[top-k-frequent-words](https://leetcode.com/problems/top-k-frequent-words)  :star: | [Heap](Python\Heap\top-k-frequent-words.py)  | Medium  |   | | |
| 11| [find median from data stream](https://leetcode.com/problems/find-median-from-data-stream) :star: |[Heap](Python/Heap/find-median-from-data-stream.py) |Hard| ```two heaps``` | |
| 12| [sliding window median](https://leetcode.com/problems/sliding-window-median) |[Heap](Python/Heap/sliding-window-median.py) |Hard | ```Two_heaps```| |
| 13  | [merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) :star: | [heap](Python/k-way-merge/merge-k-sortedlist.py)|Hard | | |
| 14  | [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [Heap](Python/Heap/kth-smallest-in-matrix.py)|Medium | | |
| 15  | [smallest-range-i](https://leetcode.com/problems/smallest-range-i/) | []()| | | |
| 16| [find k pairs with smallest sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums) |[Heap](Python/Heap/find-k-pairs-with-smallest-sums.py) |Medium |  | |
| 17| [minimum cost to connect sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks) |[Heap](Python/Heap/minimum-cost-to-connect-sticks.py) |Medium |  | |


---


### Tree
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1|[Same Tree](https://leetcode.com/problems/same-tree/)|[Recursion](Python/Tree/same-tree.py)| Easy | | |
|2|[Subtree](https://leetcode.com/problems/subtree-of-another-tree/)|[Tree](Python/Tree/subtree.py)|Easy|| |
|3|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Recursion](Python/Tree/diameter.py)|Easy | ||
|4|[maximum-depth-of-n-ary-tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[Tree DFS](Python/Tree/max_depth-nary-tree.py)|Easy | |Get the max depth of subtrees|
|5|[maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[DFS](Python/Tree/max_depth_BT.py)|Easy | ||
|6|[range-sum-of-bst](https://leetcode.com/problems/range-sum-of-bst/)|[DFS](Python/Tree/range_sum.py)|Easy | |
|7|[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/)|[DFS](Python/Tree/merge_BT.py)|Easy | |
|8|[search-in-a-binary-search-tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[DFS](Python/Tree/search-bst.py)| | |
|9|[path-sum](https://leetcode.com/problems/path-sum/) :star: |[DFS](Python/Tree/path_sum.py)| Easy |  ||
|10|[diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Tree](Python/Tree/diameter-BT.py) | Easy | | |
|11 | [kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Tree DFS](Python/Tree/kth-smallest.py) | Medium | | Push left tree nodes into stack and pop them by decrementing k. when k=0 return node.val  |
|12 | [all-nodes-distance-k-in-binary-tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) :star: | [Graph](Python/Tree/nodes-k-distance.py) | Medium |  ||
|13 | [lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) :star: | [DFS](Python/Tree/lowest_common-ancestor.py) | Medium |  ||
|14 |[minimum-depth-of-binary-tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[DFS](Python/Tree/min_depth_BT.py)|Easy | ||
|15 | [serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) :star: | [Solution](Python\Tree\serialize-deserialize-bt.py) | Hard  || same as BST |
| 16| [convert sorted list to binary search tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree) |[Tree](Python/Tree/convert-sorted-list-to-binary-search-tree.py) |Medium| | |
| 17| [binary tree postorder traversal](https://leetcode.com/problems/binary-tree-postorder-traversal) |[Tree](Python/Tree/binary-tree-postorder-traversal.py) |Medium |  | |
|18 | [binary-search-tree-iterator](https://leetcode.com/problems/binary-search-tree-iterator) | [](Python/Tree/) | | |  |
|19 | [serialize-and-deserialize-bst](https://leetcode.com/problems/serialize-and-deserialize-bst) | [Solution](Python\Tree\serialize-deserialize-BST.py) | Medium| | same as BT |
|20 | [convert-BST-to-sorted-doublyLL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | [inorder](Python\Tree\convert-bst-to-doublyLL.py) |  | | |
|21 | [construct-BT-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | [Solution](Python\Tree\construct-bt-from-preandin.py)| Medium | ||
| 22  | [Valid BST](https://leetcode.com/problems/validate-binary-search-tree/) | [BST](Python/Tree/valid-bst.py)| Medium| |Use lower & upper, initialize them to extremes. Check val <= lower or val>= upper (recursively for all nodes) |
| 23  | [Binary tree level order traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | [Tree BFS](Python/Tree/binary-tree-level-order.py)| Medium||Use a queue |
| 24  | [Reverse level order traversal ](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) | [Tree BFS](Python/Tree/reverse-level-order-traversal.py)|Medium | ||
| 25  | [Zigzag conversion](https://leetcode.com/problems/zigzag-conversion) | [](Python/Tree/)| Medium| ||
| 26  | [Average of levels in BT](https://leetcode.com/problems/average-of-levels-in-binary-tree) | [BFS](Python\Tree\average-of-levels-BT.py)| Easy | ||
| 27  | Next interval | [Tree DFS](Python/Tree/)| | ||
| 28| [populating next right pointers in each node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) |[Tree](Python/Tree/populating-next-right-pointers-in-each-node.py) |Medium |  | |
| 29  | [Binary tree right side view](https://leetcode.com/problems/binary-tree-right-side-view/) :star:| [BFS](Python\Tree\binary-tree-right-side-view.py)|Medium | ||
| 30  | [boundary of a tree](https://leetcode.com/problems/boundary-of-binary-tree/) :star: | [Solution](Python\Tree\boundary-tree.py)| Medium|| Left: Preorder, leaves: Inorder, right: Postorder |
| 31  |[maximum binary tree](https://leetcode.com/problems/maximum-binary-tree) |[Tree](Python/Tree/maximum-binary-tree.py) |Medium |  | |
| 32  | [Path sum 2](https://leetcode.com/problems/path-sum-ii) | [DFS](Python\Tree\path_sum2.py)|Medium | ||
| 33| [path sum iii](https://leetcode.com/problems/path-sum-iii) |[Tree](Python/Tree/path-sum-iii.py) |Easy | ```subarray_sum_equals_k```| |
| 34  | [Binary tree paths](https://leetcode.com/problems/binary-tree-paths/) | [](Python/Tree/)| | ||
| 35  | [Diameter of binary tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [](Python/Tree/)| | ||
| 36  | [Binary tree maximum path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) :lock:| [](Python/Tree/)| | ||
| 37| [recover binary search tree](https://leetcode.com/problems/recover-binary-search-tree) |[Tree](Python/Tree/recover-binary-search-tree.py) |Hard| | |
| 38| [maximum width of binary tree](https://leetcode.com/problems/maximum-width-of-binary-tree) |[Tree](Python/Tree/maximum-width-of-binary-tree.py) |Medium |  | |
| 39| [vertical order traversal of a binary tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree) |[Tree](Python/Tree/vertical-order-traversal-of-a-binary-tree.py) |Medium |  | |
| 40| [binary tree preorder traversal](https://leetcode.com/problems/binary-tree-preorder-traversal) |[Tree](Python/Tree/binary-tree-preorder-traversal.py) |Medium |  | |
| 41| [binary tree inorder traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) |[Tree](Python/Tree/binary-tree-inorder-traversal.py) |Medium |  | |





---

### DFS
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [Number of islands](https://leetcode.com/problems/number-of-islands) :star: | [DFS](Python\DFS\NumOfIslands.py)  | Medium  |   | |
|2   | [Number of distinct islands](https://leetcode.com/problems/number-of-distinct-islands)  | [DFS](Python\DFS\NumofDistinctIslands.py)  | Medium  |   | |
| 3| [friends circles](https://leetcode.com/problems/friends-circles) |[DFS](Python/DFS/friends-circles.py) |Medium| | |
| 4| [max area of island](https://leetcode.com/problems/max-area-of-island) |[DFS](Python/DFS/max-area-of-island.py) |Medium| | |
| 5| [surrounded regions](https://leetcode.com/problems/surrounded-regions) :star: |[DFS](Python/DFS/surrounded-regions.py) |Medium| | |
| 6| [number of closed islands](https://leetcode.com/problems/number-of-closed-islands) |[DFS](Python/DFS/number-of-closed-islands.py) |Medium| | |
| 7| [making a large island](https://leetcode.com/problems/making-a-large-island) |[DFS](Python/DFS/making-a-large-island.py) |Hard| | |
| 8| [island perimeter](https://leetcode.com/problems/island-perimeter) |[DFS](Python/DFS/island-perimeter.py) |Easy| | |
| 9| [flood fill](https://leetcode.com/problems/flood-fill) |[DFS](Python/DFS/flood-fill.py) |Easy| | |

---

### BFS
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | [rotting-oranges](https://leetcode.com/problems/rotting-oranges/) :star: | [BFS](Python/Tree/rotting-oranges.py)  | Medium  |   | |
| 2| [word ladder](https://leetcode.com/problems/word-ladder) |[BFS](Python/BFS/word-ladder.py) |Medium| | |
| 3| [shortest path in binary matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix) |[BFS](Python/BFS/shortest-path-in-binary-matrix.py) |Medium| | |
| 4| [shortest bridge](https://leetcode.com/problems/shortest-bridge) :star: |[BFS](Python/BFS/shortest-bridge.py) |Medium| ```dfs + bfs```| [Video](https://www.youtube.com/watch?v=KiCBXu4P-2Y) 7:45|
| 5| [as far from land as possible](https://leetcode.com/problems/as-far-from-land-as-possible) |[BFS](Python/BFS/as-far-from-land-as-possible.py) |Medium| | |
| 6| [walls and gates](https://leetcode.com/problems/walls-and-gates) |[BFS](Python/BFS/walls-and-gates.py) |Medium |  | |
| 7| [the maze](https://leetcode.com/problems/the-maze) |[BFS](Python/BFS/the-maze.py) |Medium |  | |
| 8| [the maze ii](https://leetcode.com/problems/the-maze-ii) |[BFS](Python/BFS/the-maze-ii.py) |Medium |  | |
| 9| [minimum knight moves](https://leetcode.com/problems/minimum-knight-moves) |[BFS](Python/BFS/minimum-knight-moves.py) |Medium |  | |
| 10| [cut off trees for golf event](https://leetcode.com/problems/cut-off-trees-for-golf-event) |[BFS](Python/BFS/cut-off-trees-for-golf-event.py) |Hard |  | |

---

### Graphs
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   | Breadth first search  | [Solution](Python/Graphs/bfs-graph.py)  | Easy  | ```Recursion```<br> ```Iterative```  ||
|2   | Depth first search  |[Solution](Python/Graphs/dfs-graph.py)   | Easy  | ```Recursion```<br> ```Iterative```  | |
|3   | Topological sort | [Solution](Python/Graphs/topological-sort.py)   | Medium  |  | |
|4   | Path that covers all nodes | [Solution](Python/Graphs/path.py) | Easy | | |
|5   | Unique paths between two nodes | [Solution](Python/Graphs/unique_paths.py) | Medium | ```dfs``` ```backtrack``` | |
|6   | Path exists   | [](Python/Graphs/)  |   |   ||
|7   | Detect cycle in a directed graph  | [Solution](Python/Graphs/cycle-directed.py)  | Medium | ```DFS```| exploring explored  |
|8   | Detect cycle in an undirected graph  | [Solution](Python/Graphs/cycle-undirected.py)  | Medium  | ```DFS```| nei != parent and nei in visited |
|9   |Shortest path between two vertices  |[](Python/Graphs/)   | |  |   |
|10   | [clone-graph](https://leetcode.com/problems/clone-graph)  |  [BFS + hashmap](Python/Graph/clone-graph.py) | Medium  |```hashmap``` | [Notes](Notes/CloneGraph.pdf)  |
|11   | [is-graph-bipartite](https://leetcode.com/problems/is-graph-bipartite)  | [BFS](Python/Graphs/bipartite-graph.py)  | Medium  | ```BFS``` | Graph coloring |
|12   |[Graph valid tree](https://leetcode.com/problems/graph-valid-tree)  |  [Cycle detection in undirected](Python/Graph/graph-valid-tree.py) | Medium  | |check for cycle and disconnected components  |
|13   |[course-schedule](https://leetcode.com/problems/course-schedule) :star: | [Topological sort ](Python/Graphs/course-schedule.py)|Medium |```dfs``` ```bfs``` ```cycle detection``` |1. Explored & exploring <br> 2. Cycle detection with Indegree idea |
|14   | [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii) :star: | [Topological sort ](Python/Graphs/course-schedule-2.py)|Medium |```dfs``` ```bfs``` ```cycle detection``` | |
| 15| [number of connected components in an undirected graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) :star:|[Graphs](Python/Graphs/number-of-connected-components-in-an-undirected-graph.py) |Medium| | |
| 16| [alien-dictionary](https://leetcode.com/problems/alien-dictionary) :star: |[Graphs](Python/Graphs/alien-dictionary.py) |Hard|```cycle detection``` ```topological sort``` | |
| 17| [cheapest flights within k stops](https://leetcode.com/problems/cheapest-flights-within-k-stops) |[Graphs](Python/Graphs/cheapest-flights-within-k-stops.py) |Medium | ```dijkstra```| |
| 18| [critical connections](https://leetcode.com/problems/critical-connections) :star: |[Graphs](Python/Graphs/critical-connections.py) |Hard | ```Articulation point``` | Tarjan's Algo <br> [Video](https://www.youtube.com/watch?v=RYaakWv5m6o)|
| 19| [accounts merge](https://leetcode.com/problems/accounts-merge) |[Graphs](Python/Graphs/accounts-merge.py) |Medium | ```unconnected components``` | |
| 20| [redundant connection](https://leetcode.com/problems/redundant-connection) |[Graphs](Python/Graphs/redundant-connection.py) |Medium |  ```cycle detection```| |
| 21| [connecting cities with minimum cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost) |[Graphs](Python/Graphs/connecting-cities-with-minimum-cost.py) |Medium | ```Dijkstra```| |
| 22  |[evaluate-division](https://leetcode.com/problems/evaluate-division) :star: |   | [](Python/Graphs/)  |  | |
| 23  | [Reconstruct itinerary](https://leetcode.com/problems/reconstruct-itinerary) :star: | [Eulerian path](Python/Graphs/reconstruct-itinerary.py)  | Medium  | | [Notes](Notes/Reconstruct-itinerary.pdf)  |






---

### DynamicProgramming
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
| 1| [house robber](https://leetcode.com/problems/house-robber) :star:|[DynamicProgramming](Python/DynamicProgramming/house-robber.py) |Easy|```Decision making``` | |
| 2| [best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) :star:|[DynamicProgramming](Python/DynamicProgramming/best-time-to-buy-and-sell-stock.py) |Easy|```Decision making``` | |
| 3| [best time to buy and sell stock ii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) |[DynamicProgramming](Python/DynamicProgramming/best-time-to-buy-and-sell-stock-ii.py) |Easy|```Decision making``` | |
| 4| [maximal square](https://leetcode.com/problems/maximal-square) |[DynamicProgramming](Python/DynamicProgramming/maximal-square.py) |Medium| | |
| 5| [minimum path sum](https://leetcode.com/problems/minimum-path-sum) |[DynamicProgramming](Python/DynamicProgramming/minimum-path-sum.py) |Medium |  | |
| 6| [climbing stairs](https://leetcode.com/problems/climbing-stairs) |[DynamicProgramming](Python/DynamicProgramming/climbing-stairs.py) |Easy |  | |
| 7| [word break](https://leetcode.com/problems/word-break) |[DynamicProgramming](Python/DynamicProgramming/word-break.py) |Medium |  | |
| 8| [maximum product subarray](https://leetcode.com/problems/maximum-product-subarray) |[DynamicProgramming](Python/DynamicProgramming/maximum-product-subarray.py) |Medium |  | |
| 9| [perfect squares](https://leetcode.com/problems/perfect-squares) |[DynamicProgramming](Python/DynamicProgramming/perfect-squares.py) |Medium |  | |
| 10| [coin change](https://leetcode.com/problems/coin-change) |[DynamicProgramming](Python/DynamicProgramming/coin-change.py) |Medium |  | |
| 11| [minimum falling path sum](https://leetcode.com/problems/minimum-falling-path-sum) |[DynamicProgramming](Python/DynamicProgramming/minimum-falling-path-sum.py) |Medium |  | |
| 12| [unique paths](https://leetcode.com/problems/unique-paths) |[DynamicProgramming](Python/DynamicProgramming/unique-paths.py) |Medium |  | |
| 13| [unique binary search tree](https://leetcode.com/problems/unique-binary-search-tree) |[DynamicProgramming](Python/DynamicProgramming/unique-binary-search-tree.py) |Medium |  |[Video](https://photos.app.goo.gl/eG6z1uaM6QAjBkrb7) |



---



###  Backtracking
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   |[Permutations](https://leetcode.com/problems/permutations/)  :star: | [Backtracking](Python/Backtracking/permutations.py)  | Medium | | DFS  |
|2   |[Permutations 2](https://leetcode.com/problems/permutations-ii/)   |[Backtracking](Python/Backtracking/permutations-ii.py)   | Medium  |   ||
|3   |[Combinations](https://leetcode.com/problems/combinations/)   :star: | [Backtracking](Python/Backtracking/combinations.py)  | Medium  |  | |
|4   |[Combination sum I](https://leetcode.com/problems/combination-sum/) :star:  | [Backtracking](Python/Backtracking/combination-sum.py)  | Medium  |  | |
|5   |[Combination sum II](https://leetcode.com/problems/combination-sum-ii/)   | [Backtracking](Python/Backtracking/combination-sum-2.py)  | Medium  | |  |
|6   | [combination-sum-iii](https://leetcode.com/problems/combination-sum-iii/)  | [Backtracking](Python/Backtracking/combination-sum-3.py)  | Medium  |   ||
|7   | [Generate Parenthesis](https://leetcode.com/problems/generate-parentheses/) :star: | [Backtracking](Python/Backtracking/generate-parentheses.py)  | Medium  |   ||
|8   | [Subsets](https://leetcode.com/problems/subsets) :star:  | [Subsets](Python/Backtracking/subsets.py)  |   |   ||
|9   | [Word search](https://leetcode.com/problems/word-search) :star: | [Backtracking](Python/Backtracking/word-search.py)  | Medium  |   ||
|10   | [Word ladder]()  | []()  |   |   ||
|11   | [regular-expression-matching](https://leetcode.com/problems/regular-expression-matching) :star: | []()  |   |   ||
| -2| [word break](https://leetcode.com/problems/word-break) |[DynamicProgramming](Python/DynamicProgramming/word-break.py) |Medium |  | |
| -2| [word break](https://leetcode.com/problems/word-break) |[DynamicProgramming](Python/DynamicProgramming/word-break.py) |Medium |  | |
|14   |[wildcard-matching](https://leetcode.com/problems/wildcard-matching)   | [](Python/Backtracking/)  |   |   ||
|15   |[letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) :star:  | [Backtracking](Python/Backtracking/letter-combinations-of-number.py)  | Medium   |   ||
|16   |[palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning)   | [](Python/Backtracking/)  |   |   ||
|17   |[n-queens](https://leetcode.com/problems/n-queens)   |   |   |   ||
|18   |[sudoku-solver](https://leetcode.com/problems/sudoku-solver)   |   |   |   ||
|19   |[subsets-ii](https://leetcode.com/problems/subsets-ii)   | [Subsets](Python/Backtracking/subsets-2.py)  |   |   ||
| | [n-queens-ii](https://leetcode.com/problems/n-queens-ii.py) |[Backtracking](Python/Backtracking/n-queens-ii.py) |Hard| ||
|21   | [android-unlock-patterns](https://leetcode.com/problems/android-unlock-patterns)  |   |   |   ||
|22   | [permutation-sequence](https://leetcode.com/problems/permutation-sequence)  |   |   |   ||
|23   | [Word ladder 2]()  | []()  |   |   ||



---


### Trie
| #   |Question| Solution |Difficulty | Tags| Notes |
| -|----- | ---------- |-----|---|----|
|1   |[Implement trie](https://leetcode.com/problems/implement-trie-prefix-tree/)  :star: | [Solution](Python/Trie/implement-trie.py)   |  Medium |   ||
|2   |[design-search-autocomplete-system](https://leetcode.com/problems/design-search-autocomplete-system)   | []()  |   ||   |
| 3| [word search ii](https://leetcode.com/problems/word-search-ii) |[Trie](Python/Trie/word-search-ii.py) |Hard |  | |
|4   |[palindrome-pairs](https://leetcode.com/problems/palindrome-pairs)   | []()  |   |   ||
|5   |[concatenated-words](https://leetcode.com/problems/concatenated-words)   | []()  |   |   ||
| | [longest-word-in-dict](https://leetcode.com/problems/longest-word-in-dict.py) |[Trie](Python/Trie/longest-word-in-dict.py) |Easy| ||
|7   | [Search Suggestions System ](https://leetcode.com/problems/search-suggestions-system) :star: | [Trie](Python\Trie\search-suggestions.py)  |  Medium |   || |
