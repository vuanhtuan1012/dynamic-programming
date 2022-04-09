# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-04 22:03:48
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-09 23:37:36

import unittest
from fib_memorization import fib


class Fibonacci(unittest.TestCase):
    def test_fib6(self):
        self.assertEqual(fib(6, dict()), 8)

    def test_fib7(self):
        self.assertEqual(fib(7, dict()), 13)

    def test_fib8(self):
        self.assertEqual(fib(8, dict()), 21)

    def test_fib50(self):
        self.assertEqual(fib(50, dict()), 12586269025)


if __name__ == '__main__':
    unittest.main()
