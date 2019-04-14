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

    def setup(self):
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
