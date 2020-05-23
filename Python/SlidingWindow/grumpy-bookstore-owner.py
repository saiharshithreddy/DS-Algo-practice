

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        num_customers_satisfied = 0
        win = 0
        max_minutes = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                num_customers_satisfied += customers[i]

            else:
                win += customers[i]

            if i >= X:
                win -= customers[i-X] * grumpy[i-X]
            max_minutes = max(max_minutes, win)
        return max_minutes + num_customers_satisfied
