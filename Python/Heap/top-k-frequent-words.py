'''
Approach: Heap to get the word with top frequency
TC: O(NlogK)
SC:O(N)
'''
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = {}
        for w in words:
            if w not in word_map:
                word_map[w] = 1
            else:
                word_map[w] += 1
        minheap = []

        for word, freq in word_map.items():
            heappush(minheap, (-freq, word))

        res = []
        for i in range(k):
            res.append(heappop(minheap)[1])
        return res
