# DS-Algo-interview-preparation in Python
<!-- TOC -->

- [DS-Algo-interview-preparation in Python](#ds-algo-interview-preparation-in-python)
  - [Sliding Window](#sliding-window)
  - [Two pointers](#two-pointers)
  - [Fast and slow pointers](#fast-and-slow-pointers)
  - [In-place reverse](#in-place-reverse)
  - [LinkedList](#linkedlist)
  - [Merge Intervals](#merge-intervals)
  - [Cyclic sort](#cyclic-sort)
  - [Trees](#trees)
  - [Subsets](#subsets)
  - [Modified Binary Search](#modified-binary-search)
  - [Bitwise XOR](#bitwise-xor)
  - [Top K elements](#top-k-elements)
  - [K-way merge](#k-way-merge)
  - [Dynamic Programming](#dynamic-programming)
  - [Topological sort](#topological-sort)
  - [Backtracking](#backtracking)

<!-- /TOC -->

### Sliding Window
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  |[Max sum subarray of size k/ Max subarray](https://leetcode.com/problems/maximum-subarray/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/max_sum_subarray.py) | Easy | |
| 2   |[Smallest Subarray with a given sum](https://leetcode.com/problems/minimum-size-subarray-sum/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/smallest_sub_array_with_given_sum.py)|  Easy |[Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Notes%20Smallest%20sub%20array%20with%20given%20sum.pdf) |
| 3   |[Longest Substring with at most K Distinct Characters *](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters) | [Sliding window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/Longest_substring_withK_distinct_characters.py) | Hard | |
|4  |[Fruits into Baskets](https://leetcode.com/problems/fruit-into-baskets/)|[Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/fruits_into_baskets.py) | Medium |[Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Fruits_into_baskets.pdf) |
|5  | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)| [Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/Longest_repeating_character_replacement.py)| Medium | |
|6  | [Permutation in String](https://leetcode.com/problems/permutation-in-string/)|[Sliding Window](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Sliding%20window/permutation_in_string.py)| Medium | |
|7  | [Longest Substring Without Repeating Characters ](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Sliding Window ]() | | |
|8   | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | [Sliding Window]() | Medium | |
|9   | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Sliding Window]() | Medium | |
|10 | [Minimum Window substring](https://leetcode.com/problems/minimum-window-substring/) | [Sliding Window]() || | |
|11  | [Concatenated words](https://leetcode.com/problems/concatenated-words/) | [Sliding Window ]() | | |
|12  | [Minimum Window substring](https://leetcode.com/problems/) | [Sliding Window ]() | Hard| |
|13   | [Sliding window maximum](https://leetcode.com/problems/sliding-window-maximum/) | [Sliding window]() | Hard |  | |
### Two pointers
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1 | [Two sum II ](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Two pointers]() | | |
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
|14  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Medium||
|15  |[Reverse string](https://leetcode.com/problems/reverse-string)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/reverse_vowels_string.py)| Easy||
|16| [Reverse vowels of a string](https://leetcode.com/problems/reverse-vowels-of-a-string/)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)| Easy ||
|17 | [Move zeros](https://leetcode.com/problems/move-zeroes)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Easy ||
|18  | [Minimum size subarray sum](https://leetcode.com/problems/minimum-size-subarray-sum)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)| Medium||
|19  | [Candy crush]()|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/)|Medium ||
|20   | [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Two pointers](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Two%20pointers/median-sorted-arrays.py) [Binary search](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BinarySearch/median-2sortedarrays.py)|Hard |Two pointers is O(n+m). Using binary search O(log(min(n,m)) [Algo](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Notes/Median-of-2sortedarrays.pdf)|

### Fast and slow pointers
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Linkedlist cycle](https://leetcode.com/problems/linked-list-cycle) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/linkedlist_cycle.py) | Easy | When slow and fast ptrs meet there is a cycle |
|2   | [Linkedlist cycle 2](https://leetcode.com/problems/linked-list-cycle-ii) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/) | Medium | After checking for a cycle, re-initialize fast ptr to 1st node and increment both slow and fast. The node at which they meet is the start of the cycle |
|3   | [Middle of Linkedlist](https://leetcode.com/problems/middle-of-the-linked-list) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/middle_linkedlist.py) |Easy | The node at which slow ptr stops |
|4   | [Palindrome LL ](https://leetcode.com/problems/palindrome-linked-list) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/palindrome_linkedlist.py) |Medium | Find middle and reverse the 2nd half of the list and compare both|
|5   | [Reorder List](https://leetcode.com/problems/reorder-list/) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/reorder-list.py) | Medium | Find middle, reverse 2nd half and merge one from 1st list and one from 2nd list|
|6   | [Circular array loop](https://leetcode.com/problems/circular-array-loop/) | [Fast & slow ptrs](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Fast_and_slow_pointers/) | Medium | |

### In-place reverse
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Reverse LL](https://leetcode.com/problems/reverse-linked-list) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverseLL.py) |Easy | Use prev and next to update the links |
|2   | [Reverse LL between](https://leetcode.com/problems/reverse-linked-list-ii) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverseLL-between.py) | Medium | loop till k-1th node and reverse |
|3   | [Rotate LL](https://leetcode.com/problems/rotate-list) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/rotateLL.py) | Medium| Move one ptr k times and then move start moving both ptrs. Update next of ptr1 to head and ptr2 to None |
|4   | [Reverse nodes in k-group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverse-nodes-k-groups.py) | Hard | Check if nodes are multiple of k then only reverse |
|5   | Reverse nodes in k-alternating subgroup | [In-place reverse](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/reverse-nodes-kgroups-alternatively.py) | Medium | Reverse k groups with a while loop to skip k nodes |

### LinkedList
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1   | [Flatten a multilevel doubly LL](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/flatten_doublylist.py) |Medium | |
|2   | [Odd Even list](https://leetcode.com/problems/odd-even-linked-list) | [Linkedlist](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/oddevenLL.py) | Medium | Initialize even_head & odd_head and update the links. Point the last node of oddlist to even head|
|3   | [Max points on a line](https://leetcode.com/problems/max-points-on-a-line) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/maxpoints-on-line.py) | Medium| |
|4   | [Copy list with random ptr](https://leetcode.com/problems/copy-list-with-random-pointer) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/copy-list-with-random-pointer.py) | Medium | |
| 5  | [Add two numbers ](https://leetcode.com/problems/add-two-numbers) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/add2numbers.py)|Medium | Create a new node after adding |
| 6  | [Add two numbers 2](https://leetcode.com/problems/add-two-numbers-ii) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/add-numbers-reverse.py)|Medium | |
| 7  | [Partition list](https://leetcode.com/problems/partition-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/partition-list.py)|Medium | Create two seperate nodes (smaller, larger). Link last of smaller to first of larger|
| 8  | [Plus one LL](https://leetcode.com/problems/plus-one-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/plus-one-LL.py)| Medium | Dummy nodes and move till non nine nodes and increment by 1. Set 9s to 0|
| 9  | [Flatten Binary tree to LL](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/)| | |
| 10  | [Insert into a sorted circular LL](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/)| | |
| 11  | [Convert a binary search tree to sorted doubly LL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | [Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/) | Medium | |
|12  | [Remove Nth node from the end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Linked List](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/LinkedList/remove-nth-node.py)| Medium | create dummy nodes (first & second) move first till k-1th node from start. Now, move both first and second. Second reaches k-1th node from start. Update the next ptr.|

### Merge Intervals
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Merge intervals](https://leetcode.com/problems/merge-intervals) | [Merge intervals]()|Easy | |
| 2  | [Insert intervals](https://leetcode.com/problems/insert-interval/) | [Merge intervals]()| Hard| |
| 3  | [Interval list intersections](https://leetcode.com/problems/interval-list-intersections/) | [Merge intervals]()| Medium| |
| 4  | [Non overlapping intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [Merge intervals]()| Medium| |
| 5  | [Meeting rooms ](https://leetcode.com/problems/meeting-rooms) | [Merge intervals]()| Easy| |
| 6  | [Meeting rooms 2](https://leetcode.com/problems/meeting-rooms-ii) | [Merge intervals]()| Medium| |
| 7  | [Employee free time](https://leetcode.com/problems/employee-free-time/) | [Merge intervals]()|Hard | |

### Cyclic sort
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Missing number](https://leetcode.com/problems/missing-number/) | [Cyclic sort]()| Easy| |
| 2  | [Find all missing numbers](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [Cyclic sort]()| Medium | |
| 3  | [Remove duplicates from a sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | [Cyclic sort]()| | |
| 4  | [Remove duplicates 2](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) | [Cyclic sort]()| | |
| 5  | [Missing positive](https://leetcode.com/problems/first-missing-positive/) | [Cyclic sort]()| | |
| 6  | [k Missing elements in sorted array](https://leetcode.com/problems/missing-element-in-sorted-array/) | [Cyclic sort]()| | |

### Trees
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1|[Same Tree](https://leetcode.com/problems/same-tree/)|[Recursion](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/same-tree.py)| Easy | |
|2|[Subtree](https://leetcode.com/problems/subtree-of-another-tree/)|[Tree](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/subtree.py)|Easy||
|3|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Recursion](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/diameter.py)|Easy | |
|4|[maximum-depth-of-n-ary-tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)|[]()| | |
|5|[maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[]()| | |
|6|[range-sum-of-bst](https://leetcode.com/problems/range-sum-of-bst/)|[]()| | |
|7|[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/)|[]()| | |
|8|[search-in-a-binary-search-tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)|[]()| | |
|9|[path-sum](https://leetcode.com/problems/path-sum/)|[]()| | |
|10|[minimum-depth-of-binary-tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|[](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/min_depth_BT.py)|Easy | |

|1 | [kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Tree DFS]() |  |  |
|2 | [all-nodes-distance-k-in-binary-tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | []() |  |  |
|3 | [lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | []() |  |  |
|4 | [diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Tree](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/diameter-BT.py) | Easy |  |
|5 | [serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | []() |  |  |
|6 | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values) | []() |  |  |
|7 | [subtree-of-another-tree](https://leetcode.com/problems/subtree-of-another-tree) | []() |  |  |
|8 | [binary-search-tree-iterator](https://leetcode.com/problems/binary-search-tree-iterator) | []() |  |  |
|9 | [serialize-and-deserialize-bst](https://leetcode.com/problems/serialize-and-deserialize-bst) | []() |  |  |
|10 | [convert-BST-to-sorted-doublyLL](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) | []() |  |  |
|11 | [construct-BT-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | []()
| 12  | [Valid BST](https://leetcode.com/problems/validate-binary-search-tree/) | [BST](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/Tree/valid-bst.py)| Medium| Use lower & upper, initialize them to extremes. Check val <= lower or val>= upper (recursively for all nodes) |
| 13  | [Binary tree level order traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | [Tree BFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BFS/binary-tree-level-order.py)| Medium|Use a queue |
| 14  | [Reverse level order traversal ](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) | [Tree BFS](https://github.com/saiharshithreddy/DS-Algo-practice/blob/master/Python/BFS/reverse-level-order-traversal.py)|Medium | |
| 15  | [Zigzag conversion](https://leetcode.com/problems/zigzag-conversion) | [Tree BFS]()| Medium| |
| 16  | [Average of levels in BT](https://leetcode.com/problems/average-of-levels-in-binary-tree) | [Tree BFS]()| Easy | |
| 17  | [max depth of binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [Tree BFS]()| | |
| 18  | [Populating next right ptrs in tree](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | [Tree BFS]()| | |
| 19  | [Binary tree right side view](https://leetcode.com/problems/binary-tree-right-side-view/) | [Tree BFS]()| | |
| 20  | [Tree boundary](https://leetcode.com/problems/boundary-of-binary-tree/) | [Tree BFS]()| | |
| 21  | [Path sum](https://leetcode.com/problems/path-sum/) | [Tree DFS]()| | |
| 22  | [Path sum 2](https://leetcode.com/problems/path-sum-ii) | [Tree DFS]()| | |
| 23  | [Path sum 3](https://leetcode.com/problems/path-sum-iii/) | [Tree DFS]()| | |
| 24  | [Binary tree paths](https://leetcode.com/problems/binary-tree-paths/) | [Tree DFS]()| | |
| 25  | [Diameter of binary tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Tree DFS]()| | |
| 26  | [Binary tree maximum path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Tree DFS]()| | |
| 27  | [find-median-from-data-stream](https://leetcode.com/problems/find-median-from-data-stream/) | [Tree DFS]()| | |
| 28  | [sliding-window-median](https://leetcode.com/problems/sliding-window-median/) | [Tree DFS]()| | |
| 29  | [ipo](https://leetcode.com/problems/ipo/) | [Tree DFS]()| | |
| 30  | Next interval | [Tree DFS]()| | |

### Subsets
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [Subsets](https://leetcode.com/problems/subsets/) | [Subsets]()| | |
| 2  | [Subsets 2](https://leetcode.com/problems/subsets-ii/) | [Subsets]()| | |
| 3  | [Permutations](https://leetcode.com/problems/permutations) | [Subsets]()| | |
| 4  | [Letter case permutation](https://leetcode.com/problems/letter-case-permutation/) | [Subsets]()| | |
| 5  | [Generate parentheses ](https://leetcode.com/problems/generate-parentheses/) | [Subsets]()| | |
| 6  | [Generalized abbreviation](https://leetcode.com/problems/generalized-abbreviation/) | [Subsets]()| | |
| 7  | [Evaluate reverse polish notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Subsets]()| | |
| 8  | [Uniquie BST](https://leetcode.com/problems/unique-binary-search-trees/) | [Subsets]()| | |
| 9  | [Unique BST 2](https://leetcode.com/problems/unique-binary-search-trees-ii/) | [Subsets]()| | |
| 10  | [Next permutation](https://leetcode.com/problems/next-permutation/) | [Subsets]()|Medium | |
| 11  | Order agnostic binary search | [Modified binary search]()| | |

### Modified Binary Search
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [round-numbers](https://leetcode.com/discuss/interview-question/125001/round-numbers/123813) | [Modified binary search]()| Easy| |
| 2  | [find-smallest-letter-greater-than-target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | [Modified binary search]()| Easy| |
| 3  | [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Modified binary search]()| | |
| 4  | [single-element-in-a-sorted-array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | [Modified binary search]()| | |
| 5  | [minimum-absolute-difference](https://leetcode.com/problems/minimum-absolute-difference/) | [Modified binary search]()| | |
| 6  | Search Bitonic Array | [Modified binary search]()| | |
| 7  | Bitonic array maximum[]() | [Modified binary search]()| | |
| 8  | [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Modified binary search]()| | |
| 9  | [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Modified binary search]()| | |
| 10  | Rotation count | [Modified binary search]()| | |

### Bitwise XOR
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [single-number](https://leetcode.com/problems/single-number/) | [bitwise xor]()| | |
| 2  | [single-number-ii](https://leetcode.com/problems/single-number-ii/) | [bitwise xor]()| | |
| 3  | [complement-of-base-10-integer](https://leetcode.com/problems/complement-of-base-10-integer/) | [bitwise xor]()| | |
| 4 | [rotate-image](https://leetcode.com/problems/rotate-image/) | [bitwise xor]()| | |
| 5  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) | [bitwise xor]()| | |
| 6  | [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [bitwise xor]()| | |
| 7  | [Min-Cost-to-Connect-Ropes](https://leetcode.com/discuss/interview-question/344677/Amazon-or-Online-Assessment-2019-or-Min-Cost-to-Connect-Ropes) | [bitwise xor]()| | |

### Top K elements
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Top k elements]()| | |
| 2  | [sort-characters-by-frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | [Top k elements]()| | |
| 3 | [kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Top k elements]()| | |
| 4  | [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/) | [Top k elements]()| | |
| 5  | [maximum-distinct-elements-removing-k-elements](https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/) | [Top k elements]()| | |
| 6  | [reorganize-string](https://leetcode.com/problems/reorganize-string/) | [Top k elements]()| | |
| 7  | [rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [Top k elements]()| | |
| 8  | [task-scheduler](https://leetcode.com/problems/task-scheduler/) | [Top k elements]()| | |
| 9  | [maximum-frequency-stack](https://leetcode.com/problems/maximum-frequency-stack/) | [Top k elements]()| | |

### K-way merge
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [k-way merge]()| | |
| 2  | [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [k-way merge]()| | |
| 3  | [smallest-range-i](https://leetcode.com/problems/smallest-range-i/) | [k-way merge]()| | |
| 4 | [find-k-pairs-with-smallest-sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [k-way merge]()| | |
| 5  | [partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [k-way merge]()| | |

### Dynamic Programming
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [Dynamic Programming]()| | |
| 2  | [coin-change](https://leetcode.com/problems/coin-change) | [Dynamic Programming]()| | |
| 3  | [frog-jump](https://leetcode.com/problems/frog-jump) | [Dynamic Programming]()| | |
| 4  | [longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring) | [Dynamic Programming]()| | |
| 5  | [word-break](https://leetcode.com/problems/word-break) | [Dynamic Programming]()| | |
| 6  | [cherry-pickup](https://leetcode.com/problems/cherry-pickup) | [Dynamic Programming]()| | |
| 7  | [decode-ways](https://leetcode.com/problems/decode-ways) | [Dynamic Programming]()| | |
| 8  | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values) | [Dynamic Programming]()| | |
| 9  | [maximal-rectangle](https://leetcode.com/problems/maximal-rectangle) | [Dynamic Programming]()| | |
| 10  | [maximal-square](https://leetcode.com/problems/maximal-square) | [Dynamic Programming]()| | |
| 11 | [longest-string-chain](https://leetcode.com/problems/longest-string-chain) | [Dynamic Programming]()| | |
| 12 | [regular-expression-matching](https://leetcode.com/problems/regular-expression-matching) | [Dynamic Programming]()| | |
| 13  | [longest-valid-parentheses](https://leetcode.com/problems/longest-valid-parentheses) | [Dynamic Programming]()| | |
| 14  | [burst-balloons](https://leetcode.com/problems/burst-balloons) | [Dynamic Programming]()| | |
| 15  | [word-break-ii](https://leetcode.com/problems/word-break-ii) | [Dynamic Programming]()| | |
| 16  | [edit-distance)](https://leetcode.com/problems/edit-distance) | [Dynamic Programming]()| | |
| 17  | [interleaving-string](https://leetcode.com/problems/interleaving-string) | [Dynamic Programming]()| | |
| 18  | [wildcard-matching](https://leetcode.com/problems/wildcard-matching) | [Dynamic Programming]()| | |
| 19  | [split-array-largest-sum](https://leetcode.com/problems/split-array-largest-sum) | [Dynamic Programming]()| | |
| 20  | [climbing-stairs](https://leetcode.com/problems/climbing-stairs) | [Dynamic Programming]()| | |
| 21  | [concatenated-words](https://leetcode.com/problems/concatenated-words) | [Dynamic Programming]()| | |
| 22  | [palindromic-substrings](https://leetcode.com/problems/palindromic-substrings) | [Dynamic Programming]()| | |
| 23  | [longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence) | [Dynamic Programming]()| | |
| 24  | [house-robber](https://leetcode.com/problems/house-robber) | [Dynamic Programming]()| | |
| 25  | [paint-house](https://leetcode.com/problems/paint-house) | [Dynamic Programming]()| | |
| 26  | [cheapest-flights-within-k-stops](https://leetcode.com/problems/cheapest-flights-within-k-stops) | [Dynamic Programming]()| | |
| 27  | [maximum-product-subarray](https://leetcode.com/problems/maximum-product-subarray) | [Dynamic Programming]()| | |
| 28  | [unique-binary-search-trees](https://leetcode.com/problems/unique-binary-search-trees) | [Dynamic Programming]()| | |
| 29  | [super-egg-drop](https://leetcode.com/problems/super-egg-drop) | [Dynamic Programming]()| | |
| 30  | [minimum-path-sum](https://leetcode.com/problems/minimum-path-sum) | [Dynamic Programming]()| | |
| 31  | [longest-arithmetic-sequence](https://leetcode.com/problems/longest-arithmetic-sequence) | [Dynamic Programming]()| | |
| 32  | [delete-and-earn](https://leetcode.com/problems/delete-and-earn) | [Dynamic Programming]()| | |
| 33  | [continuous-subarray-sum](https://leetcode.com/problems/continuous-subarray-sum) | [Dynamic Programming]()| | |
| 34  | [best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) | [Dynamic Programming]()| | |
| 35  | [knight-dialer](https://leetcode.com/problems/knight-dialer) | [Dynamic Programming]()| | |
| 36  | [shortest-way-to-form-string](https://leetcode.com/problems/shortest-way-to-form-string) | [Dynamic Programming]()| | |
| 37  | [unique-paths](https://leetcode.com/problems/unique-paths) | [Dynamic Programming]()| | |
| 38  | [best-time-to-buy-and-sell-stock-iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv) | [Dynamic Programming]()| | |
| 39  | [range-sum-query-2d-immutable](https://leetcode.com/problems/range-sum-query-2d-immutable) | [Dynamic Programming]()| | |
| 40  | [partition-to-k-equal-sum-subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets) | [Dynamic Programming]()| | |
| 41  | [count-vowels-permutation](https://leetcode.com/problems/count-vowels-permutation) | [Dynamic Programming]()| | |
| 42  | [minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence) | [Dynamic Programming]()| | |
| 43  | [unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii) | [Dynamic Programming]()| | |
| 44  | [best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | [Dynamic Programming]()| | |
| 45  | [longest-palindromic-subsequence](https://leetcode.com/problems/longest-palindromic-subsequence) | [Dynamic Programming]()| | |
| 46  | [longest-common-subsequence](https://leetcode.com/problems/longest-common-subsequence) | [Dynamic Programming]()| | |
| 47  | [tiling-a-rectangle-with-the-fewest-squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares) | [Dynamic Programming]()| | |
| 48  | [dice-roll-simulation](https://leetcode.com/problems/dice-roll-simulation) | [Dynamic Programming]()| | |
| 49  | [max-sum-of-rectangle-no-larger-than-k](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k) | [Dynamic Programming]()| | |
| 50  | [minimum-cost-to-merge-stones](https://leetcode.com/problems/minimum-cost-to-merge-stones) | [Dynamic Programming]()| | |
| 51  | [perfect-squares](https://leetcode.com/problems/perfect-squares) | [Dynamic Programming]()| | |
| 52  | [maximum-length-of-repeated-subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray) | [Dynamic Programming]()| | |
| 53  | [knight-probability-in-chessboard](https://leetcode.com/problems/knight-probability-in-chessboard) | [Dynamic Programming]()| | |
| 54  | [count-different-palindromic-subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences) | [Dynamic Programming]()| | |
| 55  | [best-time-to-buy-and-sell-stock-with-transaction-fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) | [Dynamic Programming]()| | |
| 56  | [minimum-swaps-to-make-sequences-increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing) | [Dynamic Programming]()| | |

### Topological sort
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
| 1  | [alien-dictionary](https://leetcode.com/problems/alien-dictionary) | [Topological sort]()| | |
| 2  | [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii) | [Topological sort]()| | |
| 3 | [course-schedule](https://leetcode.com/problems/course-schedule) | [Topological sort]()| | |
|  4 | [longest-increasing-path-in-a-matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix) | [Topological sort]()| | |
| 5  | [sort-items-by-groups-respecting-dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies) | [Topological sort]()| | |
| 6  | [sequence-reconstruction](https://leetcode.com/problems/sequence-reconstruction) | [Topological sort]()| | |

### Backtracking
| #   |Question| Solution |Difficulty | Notes |
| -|----- | ---------- |-----|-------|
|1  |[generate-parentheses](https://leetcode.com/problems/generate-parentheses)|[Backtracking]()|||
|2  |[letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)|[Backtracking]()|||
|3  |[word-search](https://leetcode.com/problems/word-search)|[Backtracking]()|||
|4  |[permutation](https://leetcode.com/problems/permutations)|[Backtracking]()|||
|5  |[regular-expression-matching](https://leetcode.com/problems/regular-expression-matching)|[Backtracking]()|||
|6  |[word-search-ii](https://leetcode.com/problems/word-search-ii)|[Backtracking]()|||
|7  |[word-break-ii](https://leetcode.com/problems/word-break-ii)|[Backtracking]()|||
|8  |[restore-ip-addresses](https://leetcode.com/problems/restore-ip-addresses)|[Backtracking]()|||
|9  |[wildcard-matching](https://leetcode.com/problems/wildcard-matching))|[Backtracking]()|||
|10  |[word-ladder-ii](https://leetcode.com/problems/word-ladder-ii)|[Backtracking]()|||
|11  |[subsets](https://leetcode.com/problems/subsets)|[Backtracking]()|||
|12  |[combination-sum](https://leetcode.com/problems/combination-sum)|[Backtracking]()|||
|13  |[sudoku-solver](https://leetcode.com/problems/sudoku-solver)|[Backtracking]()|||
|14  |[n-queens](https://leetcode.com/problems/n-queens)|[Backtracking]()|||
|15  |[add-and-search-word-data-structure-design](https://leetcode.com/problems/add-and-search-word-data-structure-design)|[Backtracking]()|||
|16  |[tiling-a-rectangle-with-the-fewest-squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares)|[Backtracking]()|||
|17  |[permutations-ii](https://leetcode.com/problems/permutations-ii)|[Backtracking]()|||
|18  |[unique-paths-iii](https://leetcode.com/problems/unique-paths-iii)|[Backtracking]()|||
|19  |[palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning)|[Backtracking]()|||
|20  |[word-pattern-ii](https://leetcode.com/problems/word-pattern-ii)|[Backtracking]()|||
|21  |[beautiful-arrangement](https://leetcode.com/problems/beautiful-arrangement)|[Backtracking]()|||
|22  |[factor-combinations](https://leetcode.com/problems/factor-combinations)|[Backtracking]()|||
|23  |[confusing-number-ii](https://leetcode.com/problems/confusing-number-ii)|[Backtracking]()|||
|24  |[combinations](https://leetcode.com/problems/combinations)|[Backtracking]()|||
|25  |[combination-sum-ii](https://leetcode.com/problems/combination-sum-ii)|[Backtracking]()|||
|26  |[path-with-maximum-gold](https://leetcode.com/problems/path-with-maximum-gold)|[Backtracking]()|||
|27  |[campus-bikes-ii](https://leetcode.com/problems/campus-bikes-ii)|[Backtracking]()|||
|28  |[brace-expansion](https://leetcode.com/problems/brace-expansion)|[Backtracking]()|||
|29  |[android-unlock-patterns](https://leetcode.com/problems/android-unlock-patterns)|[Backtracking]()|||
|30  |[n-queens-ii](https://leetcode.com/problems/n-queens-ii)|[Backtracking]()|||
