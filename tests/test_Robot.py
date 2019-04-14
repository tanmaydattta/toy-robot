# -*- coding: utf-8 -*-
"""
Main module for testing Robot class

"""
import unittest
from ddt import ddt, data, unpack

from robot import Robot
from table import Table

__author__ = "tanmay.datta86@gmail.com"


@ddt
class RobotTest(unittest.TestCase):
    """
    Tests for Robot goes here
    """

    def setUp(self):
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_robot_created_properly(self):
        self.assertFalse(self.robot.ready)
        self.assertEqual(self.robot.direction, None)
        self.assertEqual(self.robot.position, (None, None))
        self.assertEqual(self.robot.table, self.table)

    def test_robot_not_on_table(self):
        pass

    def test_placing_robot_correctly(self):
        pass

    def test_discard_until_placing_robot(self):
        pass

    def test_placing_robot_trying_to_fall_down(self):
        pass

    def test_placing_robot_incorrectly(self):
        pass

    def test_move_robot(self):
        pass

    def test_move_robot_try_to_fall(self):
        pass

    def test_rotate_robot(self):
        pass

    def test_report_robot_position(self):
        pass
