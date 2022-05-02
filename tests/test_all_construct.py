# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-05-02 03:43:38
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-02 03:50:47

import unittest
from all_construct import allConstruct


class AllConstruct(unittest.TestCase):
    def test_countConstruct_case1(self):
        self.assertEqual(allConstruct('purple',
                                      ['purp', 'p', 'ur', 'le', 'purpl'],
                                      dict()),
                         [['purp', 'le'], ['p', 'ur', 'p', 'le']])

    def test_countConstruct_case2(self):
        self.assertEqual(allConstruct('abcdef',
                                      ['ab', 'abc', 'cd', 'def',
                                       'abcd', 'ef', 'c'], dict()),
                         [['ab', 'cd', 'ef'], ['ab', 'c', 'def'],
                          ['abc', 'def'], ['abcd', 'ef']])

    def test_countConstruct_case3(self):
        self.assertEqual(allConstruct('skateboard',
                                      ['bo', 'rd', 'ate', 't', 'ska',
                                       'sk', 'boar'], dict()), [])

    def test_countConstruct_case5(self):
        self.assertEqual(allConstruct(('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                                       'eeeeeeeeeeeef'),
                                      ['e', 'ee', 'eee', 'eeee', 'eeeee',
                                       'eeeeee'], dict()), [])


if __name__ == '__main__':
    unittest.main()
