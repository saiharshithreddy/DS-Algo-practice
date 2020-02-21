# Dynamic Programming
When to use DP?
When the problems have optimal substructure and subproblems
Minimization, Maximization. Optimization or counting?
## Fibonacci numbers
#### Naive algorithm
```python
def fib(n):
  if n<= 2: return 1
  else:
    f = fib(n-1) + fib(n-2)
    return f
```
Disadvantages:
1. Exponential Time complexity O(2^n)
```
T(n) = T(n-1) + T(n-2) + O(1)
    >= 2T(n-2)
    = O(2^n/2)
```
*How to make this algorithm faster?*
Dynamic Programming = Recursion + Memoization
Time = num of subproblems * time taken for each subproblem.
Two ways:
1. Top down approach
2. Bottom up approach

1. Memoization (store already computed values in a dictionary)
#### Memoized algo (Top down)
```python
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n<=2: return 1
    else: f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f
```
#### Bottom up approach
```python
fib = []
for k in range(1, n+1):
  if k<=2: f=1
  else: f= fib(k-1) + fib(k-2)
  fib[k] = f
  return fib[n]
```
**Time complexity: O(N)** (N memoized calls and each call costs O(1))
Exactly same computation as top down approach.
Topological sort of subproblems dependancy DAG


## Shortest paths
Shortest path in a graph
Infinite time if the graph has cycle.
DAG: O(V+E)
time for a subproblem = indegree(V)+1
Total time = sum of time taken for all subproblems
O(E+V)
