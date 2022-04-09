# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-09 10:16:28
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-09 10:19:48

import unittest
from grid_traveler import gridTraveler


class GridTraveler(unittest.TestCase):
    def test_gridTraveler11(self):
        self.assertEqual(gridTraveler(1, 1), 1)

    def test_gridTraveler23(self):
        self.assertEqual(gridTraveler(2, 3), 3)

    def test_gridTraveler32(self):
        self.assertEqual(gridTraveler(3, 2), 3)

    def test_gridTraveler33(self):
        self.assertEqual(gridTraveler(3, 3), 6)

    def test_gridTraveler1818(self):
        self.assertEqual(gridTraveler(18, 18), 2333606220)


if __name__ == '__main__':
    unittest.main()
