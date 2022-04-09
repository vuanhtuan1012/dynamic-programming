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

## Part 1. Memorization

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
- Unit tests: [tests/test_fib.py](tests/test_fib.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_fib.py
python -m unittest -v tests.test_fib
python -m pytest -v tests/test_fib.py
```

### gridTraveler problem
> Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.
> In how many ways can you travel to the goal on a grid with dimensions m*n ?
> Write a function `gridTraveler(m, n)`  that calculates this.

#### Brute force gridTraveler recursive function
```python
def gridTraveler(m: int, n: int) -> int:
    if (m <= 0) or (n <= 0):
        return 0
    if (m == 1) and (n == 1):
        return 1
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)
```
- Time complexity: O(2<sup>n+m</sup>)
- Space complexity: O(n+m)

#### gridTraveler memorized recursive function
```python
def gridTraveler(m: int, n: int,
                 memo: Optional[dict] = dict()) -> int:
    key = f'{m},{n}'
    if key in memo:
        return memo[key]
    if (m <= 0) or (n <= 0):
        return 0
    if (m == 1) or (n == 1):
        return 1
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    if m != n:
        memo[f'{n},{m}'] = memo[key]
    return memo[key]
```
- Time complexity: O(n*m)
- Space complexity: O(n+m)

#### Resources
- Code: [grid_traveler.py](grid_traveler.py)
- Unit tests: [tests/test_grid_traveler.py](tests/test_grid_traveler.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_grid_traveler.py
python -m unittest -v tests.test_grid_traveler
python -m pytest -v tests/test_grid_traveler.py
```

### Memorization recipe
> This is Alvin's guidelines for solving dynamic programing problems using a memorization strategy.

1. **Make it work**
    - Visualize the problem as a tree.
    -  Implement the tree using recursion.
    - Test it.
2. **Make it efficient**
    - Add a memo object:
        - keys represent arguments to our function, and values represent the return values for those function calls.
        - make sure memo object is shared among all of the recursive calls.
    - Add a base case to return memo values.
    - Store return values into the memo.

### canSum problem
> Write a function `canSum(targetSum, numbers)` that takes in a `targetSum` and an array of numbers as arguments.
> The function should return a boolean indicating whether or not it is possible to generate the `targetSum` using numbers from the array.
> You may use an element of the array as many times as needed.
> You may assume that all input numbers are non-negative.

#### Brute force canSum recursive function
```python
def canSum(targetSum: int, numbers: list) -> bool:
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers):
            return True
    return False
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers))```
- Time complexity: O(n<sup>m</sup>)
- Space complexity: O(m)

#### canSum memorized recursive function
```python
def canSum(targetSum: int, numbers: list,
           memo: Optional[dict] = dict()) -> bool:
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        memo[targetSum] = canSum(remainder, numbers, memo)
        if memo[targetSum] == True:
            return True
    memo[targetSum] = False
    return False
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers))```
- Time complexity: O(n*m)
- Space complexity: O(m)

## Part 2. Tabulation
:soon:

## Terminology
- **Dynamic programming:** decompose a large instance of problem into smaller instance of the same problem. Then we have an overlapping structure.
- **Memorization:** one of the overarching strategies we can use to solve any dynamic programming problem.
- **Tabulation:** :soon:

## :warning: Notes
- The directory `tests`  must have file `__init__.py` to call command `pytest -v tests/[filename].py`. If not, you have to call command `python -m pytest -v tests/[filename].py`.
- The difference between `pytest` and `python -m pytest` is the later adds current directory to `sys.path`.
- It seems that default dictionary argument which has the same name, but in different calls shares the same region of memory :exclamation: That's why I have to use calls like `canSum(7, [2, 3], dict())` instead of `canSum(7, [2, 3])`.