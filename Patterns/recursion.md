# Recursion

## Advantages of Recursion

* Recursive functions make the code look clean and elegant.
* A complex task can be broken down into simpler sub-problems using recursion.
* Sequence generation is easier with recursion than using some nested iteration.

## Disadvantages of Recursion

* Sometimes the logic behind recursion is hard to follow through.
* Recursive calls are expensive (inefficient) as they take up a lot of memory (call stack) and time .
* Recursive functions are hard to debug.

## Types

1. Linear recursion
2. Tail recursion
3. Binary recursion
4. Exponential recursion
5. Nested recursion
6. Mutual recursion

### Linear recursion

single call to itself each time the function runs

```python
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
```

### Binary recursion

Some recursive functions don't just have one call to themself, they have two (or more). Functions with two recursive calls are referred to as binary recursive functions

```python

def fibonaci(n):
    if n<=1:
        return n
    else:
        fibonaci(n-1)+fibonaci(n-2)
```
### Exponential recursion

An exponential recursive function is one that, if you were to draw out a representation of all the function calls, would have an exponential number of calls in relation to the size of the data set (exponential meaning if there were n elements, there would be O(an) function calls where a is a positive number)

### Nested recursion

In nested recursion, one of the arguments to the recursive function is the recursive function itself! These functions tend to grow extremely fast.

### Mutual recursion

func_A( ) -> func_B( ) -> func_C( ) -> func_A( )

When to use Recursion?
If you know the number of loops that need to be nested, use the iterative approach. If you do not know the number of loops that need to be nested, use the recursive method.
example: In graphs and trees 
