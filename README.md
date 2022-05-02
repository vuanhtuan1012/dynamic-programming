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

Test cases:
```python
gridTraveler(1, 1)   # 1
gridTraveler(2, 3)   # 3
gridTraveler(3, 2)   # 3
gridTraveler(3, 3)   # 6
```

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

Test cases:
```python
canSum(7, [2, 3])   # True
canSum(7, [5, 3, 4, 7])   # True
canSum(7, [2, 4])   # False
canSum(8, [2, 3, 5])   # True
canSum(300, [7, 14])   # False
```

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
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` (_in notion of bigO_)
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
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` (_in notion of bigO_)
- Time complexity: O(n*m)
- Space complexity: O(m)

#### Resources
- Code: [can_sum.py](can_sum.py)
- Unit tests: [tests/test_can_sum.py](tests/test_can_sum.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_can_sum.py
python -m unittest -v tests.test_can_sum
python -m pytest -v tests/test_can_sum.py
```

### howSum problem
> Write a function `howSum(targetSum, numbers)` that takes in a `targetSum` and an array of numbers as arguments.
> The function should return an array containing any combination of elements that add up to exactly the `targetSum`. If there is no combination that adds up to the `targetSum`, then return `null`.
> If there are multiple combinations possible. you may return any single one.

Test cases:
```python
howSum(7, [2, 3])   # [2, 2, 3]
howSum(7, [5, 3, 4, 7])   # [3, 4]
howSum(7, [2, 4])   # None
howSum(8, [2, 3, 5])   # [2, 2, 2, 2]
howSum(300, [7, 14])   # None
```

#### Brute force howSum recursive function
```python
def howSum(targetSum: int, numbers: list) -> list:
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        res = howSum(remainder, numbers)
        if res is not None:
            return [num, *res]
    return None
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` (_in notion of bigO_)
- Time complexity: O(m*n<sup>m</sup>)
- Space complexity: O(m)

#### howSum memorized recursive function
```python
def howSum(targetSum: int, numbers: list,
           memo: Optional[dict] = dict()) -> list:
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        res = howSum(remainder, numbers, memo)
        if res is not None:
            memo[targetSum] = [num, *res]
            return memo[targetSum]
    memo[targetSum] = None
    return None
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` (_in notion of bigO_)
- Time complexity: O(n*m<sup>2</sup>)
- Space complexity: O(m<sup>2</sup>)

#### Resources
- Code: [how_sum.py](how_sum.py)
- Unit tests: [tests/test_how_sum.py](tests/test_how_sum.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_how_sum.py
python -m unittest -v tests.test_how_sum
python -m pytest -v tests/test_how_sum.py
```

### bestSum problem
> Write a function `bestSum(targetSum, numbers)` that takes in a `targetSum` and an array of numbers as arguments.
> The function should return an array containing the **shortest** combination of numbers that add up to exactly the `targetSum`.
> If there is a tie for the shortest combination, you may return any one of the shortest.

Test cases:
```python
bestSum(7, [5, 3, 4, 7])   # [7]
bestSum(8, [2, 3, 5])   # [3, 5]
bestSum(8, [1, 4, 5])   # [4, 4]
bestSum(100, [1, 2, 5, 25])   # [25, 25, 25, 25]
```

#### Brute force bestSum recursive function
```python
def bestSum(targetSum: int, numbers: list) -> list:
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        res = bestSum(remainder, numbers)
        if res is not None:
            combination = [num, *res]
            cond = shortestCombination is None
            cond = cond or (len(combination) < len(shortestCombination))
            if cond:
                shortestCombination = combination
    return shortestCombination
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` (_in notion of bigO_)
- Time complexity: O(m*n<sup>m</sup>)
- Space complexity: O(m)

#### bestSum memorized recursive function
```python
def bestSum(targetSum: int, numbers: list,
            memo: Optional[dict] = dict()) -> list:
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        res = bestSum(remainder, numbers, memo)
        if res is not None:
            combination = [num, *res]
            cond = shortestCombination is None
            cond = cond or (len(combination) < len(shortestCombination))
            if cond:
                shortestCombination = combination
    memo[targetSum] = shortestCombination
    return memo[targetSum]
```
- large of the tree: ```n = len(numbers)```
- height of the tree: ```m = ceil(targetSum/min(numbers)) = targetSum``` _(in notion of bigO)_
- Time complexity: O(n*m<sup>2</sup>)
- Space complexity: O(m<sup>2</sup>)

#### Resources
- Code: [best_sum.py](best_sum.py)
- Unit tests: [tests/test_best_sum.py](tests/test_best_sum.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_best_sum.py
python -m unittest -v tests.test_best_sum
python -m pytest -v tests/test_best_sum.py
```

### canConstruct problem
> Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
> The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordBank` array.
> You may reuse an element of `wordBank` as many times as needed.

Test cases:
```python
canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])  # True
canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])  # False
canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])  # True
canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
             ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])  # False
```

#### Brute force canConstruct recursive function
```python
def canConstruct(target: str, wordBank: list) -> bool:
    if target == '':
        return True
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank):
                return True
    return False
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(m*n<sup>m</sup>)
- Space complexity: O(m<sup>2</sup>)

#### canConstruct memorized recursive function
```python
def canConstruct(target: str, wordBank: list,
                 memo: Optional[dict] = {}) -> bool:
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(n*m<sup>2</sup>)
- Space complexity: O(m<sup>2</sup>)

#### Resources
- Code: [can_construct.py](can_construct.py)
- Unit tests: [tests/test_can_construct.py](tests/test_can_construct.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_can_construct.py
python -m unittest -v tests.test_can_construct
python -m pytest -v tests/test_can_construct.py
```

### countConstruct problem
> Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.
> The function should return the number of ways that the `target` can be constructed by concatenating elements of the `wordBank` array.
> You may reuse an element of `wordBank` as many times as needed.

Test cases:
```python
countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])  # 1
countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])  # 2
countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])  # 0
countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])  # 4
countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
               ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])  # 0
```

#### Brute force countConstruct recursive function
```python
def countConstruct(target: str, wordBank: list) -> bool:
    if target == '':
        return 1
    nb_of_ways = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if countConstruct(suffix, wordBank):
                nb_of_ways += 1
    return nb_of_ways
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(m*n<sup>m</sup>)
- Space complexity: O(m<sup>2</sup>)

#### countConstruct memorized recursive function
```python
def countConstruct(target: str, wordBank: list,
                   memo: Optional[dict] = dict()) -> int:
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    nb_of_ways = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            nb_of_ways += countConstruct(suffix, wordBank, memo)
    memo[target] = nb_of_ways
    return memo[target]
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(n*m<sup>2</sup>)
- Space complexity: O(m<sup>2</sup>)

#### Resources
- Code: [count_construct.py](count_construct.py)
- Unit tests: [tests/test_count_construct.py](tests/test_count_construct.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_count_construct.py
python -m unittest -v tests.test_count_construct
python -m pytest -v tests/test_count_construct.py
```

### allConstruct problem
> Write a function `allConstruct(target, wordBank)` that accepts a target string and an array of strings.
> The function should return a 2D array containing all of the ways that the `target` can be constructed by concatenating elements of the `wordBank` array. Each element of the 2D array should represent one combination that constructs the `target`.
> You may reuse an element of `wordBank` as many times as needed.

Test cases:
```python
allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])  # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])  # []
allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
             ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])  # []
```

#### Brute force allConstruct recursive function
```python
def allConstruct(target: str, wordBank: list) -> list:
    if target == '':
        return [[]]
    result = list()
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = allConstruct(suffix, wordBank)
            target_ways = map(lambda way: [word, *way], suffix_ways)
            result.extend(target_ways)
    return result
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(m*n<sup>m</sup>)
- Space complexity: O(m<sup>2</sup>)

#### allConstruct memorized recursive function
```python
def allConstruct(target: str, wordBank: list,
                 memo: Optional[dict] = {}) -> list:
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = list()
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_ways = allConstruct(suffix, wordBank, memo)
            target_ways = map(lambda way: [word, *way], suffix_ways)
            result.extend(target_ways)
    memo[target] = result
    return memo[target]
```
- large of the tree: ```n = len(wordBank)```
- height of the tree: ```m = len(target)``` (_in notion of bigO_)
- Time complexity: O(n*m<sup>2</sup>)
- Space complexity: O(m<sup>2</sup>)

#### Resources
- Code: [all_construct.py](all_construct.py)
- Unit tests: [tests/test_all_construct.py](tests/test_all_construct.py). To run tests, in the root directory use one of these commands below
```sh
pytest -v tests/test_all_construct.py
python -m unittest -v tests.test_all_construct
python -m pytest -v tests/test_all_construct.py
```


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
