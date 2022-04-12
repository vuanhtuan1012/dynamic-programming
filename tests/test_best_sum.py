# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-12 02:09:53
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-12 03:11:18

import unittest
from best_sum import bestSum


class BestSum(unittest.TestCase):
    def test_bestSum_case1(self):
        self.assertEqual(bestSum(7, [5, 3, 4, 7], dict()), [7])

    def test_bestSum_case2(self):
        self.assertEqual(bestSum(8, [2, 3, 5], dict()), [3, 5])

    def test_bestSum_case3(self):
        self.assertEqual(bestSum(8, [1, 4, 5], dict()), [4, 4])

    def test_bestSum_case4(self):
        self.assertEqual(bestSum(100, [1, 2, 5, 25], dict()),
                         [25, 25, 25, 25])


if __name__ == '__main__':
    unittest.main()
