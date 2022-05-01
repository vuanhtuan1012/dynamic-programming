# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-30 07:59:13
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-01 19:44:26

from typing import Optional
from tlib import timer


def canConstruct(target: str, wordBank: list,
                 memo: Optional[dict] = dict()) -> bool:
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


@timer
def main():
    target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    wordBank = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']
    print(canConstruct(target, wordBank))


if __name__ == '__main__':
    main()
