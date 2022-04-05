# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-04 21:21:27
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-05 08:11:26

from typing import Optional
from tlib import timer


def fib(n: int, memo: Optional[dict] = dict()) -> int:
    """Find the n-th number of the Fibonacci sequence

    Args:
        n (int): index of number in Fibonacci sequence
        memo (Optional[dict], optional): Description

    Returns:
        int: value of n-th number in Fibonacci sequence
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


@timer
def main():
    n = int(input('n = '))
    print(f'fib(n) = {fib(n)}')


if __name__ == '__main__':
    main()
