# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-05-01 02:11:26
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-01 19:48:27

import unittest
from can_construct import canConstruct


class CanConstruct(unittest.TestCase):
    def test_canConstruct_case1(self):
        self.assertEqual(canConstruct('abcdef',
                                      ['ab', 'abc', 'cd', 'def', 'abcd'],
                                      dict()), True)

    def test_canConstruct_case2(self):
        self.assertEqual(canConstruct('skateboard',
                                      ['bo', 'rd', 'ate', 't', 'ska',
                                       'sk', 'boar'], dict()), False)

    def test_canConstruct_case3(self):
        self.assertEqual(canConstruct('enterapotentpot',
                                      ['a', 'p', 'ent', 'enter', 'ot',
                                       'o', 't'], dict()), True)

    def test_canConstruct_case4(self):
        self.assertEqual(canConstruct(('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                                       'eeeeeef'),
                                      ['e', 'ee', 'eee', 'eeee', 'eeeee',
                                       'eeeeee'], dict()), False)


if __name__ == '__main__':
    unittest.main()
