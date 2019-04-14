# -*- coding: utf-8 -*-
"""
Main module for testing Table class

"""
import unittest
import ddt

from table import Table

__author__ = "tanmay.datta86@gmail.com"


@ddt.ddt
class TableTest(unittest.TestCase):

    def setUp(self):
        self.default_table = Table(5, 5)

    @ddt.data((4, 4), (6, 6), (9, 9))
    @ddt.unpack
    def test_if_table_created_properly(self, length, width):

        table = Table(length, width)
        self.assertEqual(table.width, width)
        self.assertEqual(table.length, length)

    @ddt.data((-4, 4), (6, -6), (-9, -9))
    @ddt.unpack
    def test_if_table_throws_valueerror(self, length, width):
        with self.assertRaises(ValueError):
            Table(length, width)

    @ddt.data((4, 4), (3, 3), (5, 4), (0, 0))
    @ddt.unpack
    def test_if_given_cordinates_are_on_table(self, x_pos, y_pos):
        self.assertTrue(self.default_table.coordinates_within_limits(x_pos,
                                                                     y_pos))

    @ddt.data((9, 9), (9, 3), (5, 7), (-7, 0))
    @ddt.unpack
    def test_if_given_cordinates_are_not_on_table(self, x_pos, y_pos):
        self.assertFalse(self.default_table.coordinates_within_limits(x_pos, y_pos))
