# Dynamic Programming

Redo examples of course Dynamic Programming at [freeCodeCamp](https://youtu.be/oBt53YbR9Kk) in Python.

> Learn how to use Dynamic Programming in this course for beginners. It
> can help you solve complex programming problems, such as those often
> seen in programming interview questions about data structures and
> algorithms.
>
> This course was developed by Alvin Zablan from Coderbyte.
> Coderbyte is one of the top websites for technical interview prep and
> coding challenges.

## Part 1. Memoization

### Fibonacci problem
> Write a function `fib(n)` that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence.
- The 1st and 2nd number of the sequence is 1.
- To generate the next number of the sequence, we sum the previous two.

|n|1|2|3|4|5|6|7|8|9|...|
|--|--|--|--|--|--|--|--|--|--|--|
|fib(n)| 1|1|2|3|5|8|13|21|24|...|

#### Classic Fibonacci recursive function
```python
def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
```
- Time complexity: O(2<sup>n</sup>)
- Space complexity: O(n)

#### Fibonacci memorized recursive function
```python
def fib(n: int, memo: Optional[dict] = dict()) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```
- Time complexity: O(n)
- Space complexity: O(n)

#### Resources
- Code: [fib_memorization.py](fib_memorization.py)
- Unit tests: [tests/fib.py](tests/fib.py). To run tests, in the root directory use the command below
```sh
python -m unittest -v tests.fib
```

## Part 2. Tabulation
:soon:

## Terminology
- **Dynamic programming:** decompose a large instance of problem into smaller instance of the same problem. Then we have an overlapping structure.
- **Memorization:** one of the overarching strategies we can use to solve any dynamic programming problem.
- **Tabulation:** :soon: