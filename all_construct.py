# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-05-01 20:24:47
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-02 03:40:23

from typing import Optional
from tlib import timer


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


@timer
def main():
    target = 'purple'
    wordBank = ['purp', 'p', 'ur', 'le', 'purpl']
    print(allConstruct(target, wordBank))
    # print(allConstruct('hello', ['cat', 'dog', 'mouse']))
    # print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
    #                    ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
    # print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))


if __name__ == '__main__':
    main()