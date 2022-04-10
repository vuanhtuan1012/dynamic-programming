# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-10 01:37:21
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-10 17:06:00

from typing import Optional
from tlib import timer


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


@timer
def main():
    print(howSum(300, [7, 14]))


if __name__ == '__main__':
    main()
