# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-09 23:07:15
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-09 23:36:09

import unittest
from can_sum import canSum


class CanSum(unittest.TestCase):
    def test_canSum_case1(self):
        self.assertEqual(canSum(7, [2, 3], dict()), True);

    def test_canSum_case2(self):
        self.assertEqual(canSum(7, [5, 3, 4, 7], dict()), True);

    def test_canSum_case3(self):
        self.assertEqual(canSum(7, [2, 4], dict()), False);

    def test_canSum_case4(self):
        self.assertEqual(canSum(8, [2, 3, 5], dict()), True);

    def test_canSum_case5(self):
        self.assertEqual(canSum(300, [7, 14], dict()), False);


if __name__ == '__main__':
    unittest.main()