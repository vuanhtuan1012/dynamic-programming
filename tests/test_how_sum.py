# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-10 16:33:14
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-10 17:04:51

import unittest
from how_sum import howSum


class HowSum(unittest.TestCase):
    def test_howSum_case1(self):
        self.assertEqual(howSum(7, [2, 3], dict()), [2, 2, 3])

    def test_howSum_case2(self):
        self.assertEqual(howSum(7, [5, 3, 4, 7], dict()), [3, 4])

    def test_howSum_case3(self):
        self.assertEqual(howSum(7, [2, 4], dict()), None)

    def test_howSum_case4(self):
        self.assertEqual(howSum(8, [2, 3, 5], dict()), [2, 2, 2, 2])

    def test_howSum_case5(self):
        self.assertEqual(howSum(300, [7, 14], dict()), None)


if __name__ == '__main__':
    unittest.main()
