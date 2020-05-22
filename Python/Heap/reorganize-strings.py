'''
Brainstorming: I cannot think of a way to solve this question. 
If I get the frequency of each character, how does that help in knowing if a string can be formed. 
What am I missing here?
In the example: 'aaab'. a:3 b:1 total: 4. a > total + 1 /2 so not possible


'''
class Solution:
        def reorganizeString(self, S: str) -> str:
           letter_freq = collections.Counter(S)
           max_heap = []
           for word, freq in letter_freq.items():
               heapq.heappush(max_heap, [-freq, word])

            res = ""
            pre = heapq.heappop(max_heap)
            res += pre[1]

            while max_heap:
                curr = heapq.heappop(max_heap)
                res += curr[1]
                pre[0] += 1
                if pre[0] < 0:
                    heapq.heappush(max_heap, pre)
                pre = curr 
            return res if len(res) == les(S) else ""


