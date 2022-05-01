# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-05-01 19:48:00
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-05-01 19:53:52

import unittest
from count_construct import countConstruct


class CountConstruct(unittest.TestCase):
    def test_countConstruct_case1(self):
        self.assertEqual(countConstruct('abcdef',
                                        ['ab', 'abc', 'cd', 'def', 'abcd'],
                                        dict()), 1)

    def test_countConstruct_case2(self):
        self.assertEqual(countConstruct('purple',
                                        ['purp', 'p', 'ur', 'le', 'purpl'],
                                        dict()), 2)

    def test_countConstruct_case3(self):
        self.assertEqual(countConstruct('skateboard',
                                        ['bo', 'rd', 'ate', 't', 'ska',
                                         'sk', 'boar'], dict()), 0)

    def test_countConstruct_case4(self):
        self.assertEqual(countConstruct('enterapotentpot',
                                        ['a', 'p', 'ent', 'enter', 'ot',
                                         'o', 't'], dict()), 4)

    def test_countConstruct_case5(self):
        self.assertEqual(countConstruct(('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                                         'eeeeeeeeeeeef'),
                                        ['e', 'ee', 'eee', 'eeee', 'eeeee',
                                         'eeeeee'], dict()), 0)


if __name__ == '__main__':
    unittest.main()
