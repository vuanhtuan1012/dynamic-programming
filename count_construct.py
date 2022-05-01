# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-05-01 19:29:26
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-01 19:56:41

from typing import Optional
from tlib import timer


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


@timer
def main():
    target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    wordBank = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']
    print(countConstruct(target, wordBank))


if __name__ == '__main__':
    main()
