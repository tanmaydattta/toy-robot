# -*- coding: utf-8 -*-
"""
Main module for testing Robot class

"""
import unittest
from ddt import ddt, data, unpack

from robot import Robot
from table import Table
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


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

    @data((0, 0, "NORTH"), (1, 2, "EAST"), (3, 3, "NORTH"))
    @unpack
    def test_placing_robot_correctly(self, x_coord, y_coord, direction):
        self.robot.place(x_coord, y_coord, direction)
        self.assertEqual(self.robot.ready, True)
        self.assertEqual(self.robot.direction, direction)
        self.assertEqual(self.robot.position, (x_coord, y_coord))
        logger.debug(self.robot.report())

    def test_discard_until_placing_robot(self):
        new_robot = Robot(self.table)
        new_robot.move()
        new_robot.move()
        new_robot.left()

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
