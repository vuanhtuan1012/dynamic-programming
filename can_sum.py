# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-09 13:36:50
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-09 23:40:09

from typing import Optional
from tlib import timer


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


@timer
def main():
    print(canSum(300, [7, 14]))


if __name__ == '__main__':
    main()
