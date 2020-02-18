'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N*C) N: num of items, C: capacity
Space complexity: O(N*C)

Algorithm:

'''
def knapsack(profits, weights, capacity):

    # create a matrix (N*Capacity)
    dp = [[-1]*len(profits)]* len(profits)

    return solve_knapsack(dp, profits, weights, capacity, 0)

def solve_knapsack(dp, profits, weights, capacity, index):

    # base cases
    if capacity <= 0 or index >= len(profits):
        return 0

    # get result from memory
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    cost = 0
    if weights[index] <= capacity:
        cost = profits[index] + solve_knapsack(dp, profits, weights, capacity - weights[index], index + 1)

    cost2 = solve_knapsack(dp, profits, weights, capacity, index+1)

    # answer
    dp[index][capacity] = max(cost, cost2)

    return dp[index][capacity]
