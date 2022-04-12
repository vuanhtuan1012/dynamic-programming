# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-10 18:39:09
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-12 06:10:19

from typing import Optional
from tlib import timer


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


@timer
def main():
    print(bestSum(100, [1, 2, 5, 25]))


if __name__ == '__main__':
    main()
