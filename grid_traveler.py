# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-06 21:27:31
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-09 12:18:14

from typing import Optional
from tlib import timer


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


@timer
def main():
    x = input('m, n = ')
    m, n = map(int, x.split(','))
    print(gridTraveler(m, n))


if __name__ == '__main__':
    main()
