# -*- coding: utf-8 -*-
"""
Main module for testing Robot class

"""
import logging
import unittest

from ddt import data, ddt, unpack

from robot import Robot
from table import Table

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


@ddt
class RobotTest(unittest.TestCase):
    """
    Tests for Robot goes here
    """

    def setUp(self):
        self.terrain = Table(5, 5)
        self.robot = Robot(self.terrain)

    def test_robot_created_properly(self):
        self.assertFalse(self.robot.ready)
        self.assertEqual(self.robot.position(), (None, None, None))
        self.assertEqual(self.robot.terrain, self.terrain)

    def test_robot_not_on_table(self):
        robot_in_air = Robot()
        self.assertFalse(robot_in_air.ready)
        self.robot.navigation_system.move()
        self.robot.navigation_system.left()
        self.robot.navigation_system.right()
        self.assertEqual(self.robot.position(), (None, None, None))

    @data((0, 0, "NORTH"), (1, 2, "EAST"), (3, 3, "NORTH"))
    @unpack
    def test_placing_robot_correctly(self, x_coord, y_coord, direction):
        self.robot.place(x_coord, y_coord, direction)
        self.assertEqual(self.robot.ready, True)
        self.assertEqual(self.robot.position(), (x_coord, y_coord, direction))
        logger.debug(self.robot.report())

    def test_discard_until_placing_robot(self):
        new_robot = Robot(self.terrain)
        new_robot.navigation_system.move()
        new_robot.navigation_system.move()
        new_robot.navigation_system.left()
        self.assertEqual(self.robot.position(), (None, None, None))

    @data((0, 0, "NORTH"), (1, 2, "EAST"), (3, 3, "NORTH"))
    @unpack
    def test_placing_robot_trying_to_fall_down(self, x_coord,
                                               y_coord, direction):
        self.robot.place(x_coord, y_coord, direction)
        self.assertEqual(self.robot.ready, True)
        # any time it moves more than 5 times  same diretionit would fall 
        for x in range(0, 10):
            self.robot.navigation_system.move()
        (x, y, _d) = self.robot.position()
        self.assertTrue(self.terrain.coordinates_within_limits(x,y))

    @data((0, 0, "NORTHWrong"),
          (-1, 2, "EAST"),
          (3, -3, "Sky"), (2, 2, "WATER"))
    @unpack
    def test_placing_robot_incorrectly(self, x, y, direction):
        self.robot.place(x, y, direction)
        self.assertEqual(self.robot.position(), (None, None, None))

    @data((100, "NORTH", "NORTH", "NORTH"),
          (1080, "NORTH", "NORTH", "NORTH"),
          (101, "NORTH", "WEST", "EAST"))
    @unpack
    def test_rotate_robot(self, times, start_d, end_d_l, end_d_r):
        self.robot.place(0, 0, start_d)
        for m in range(0, times):
            self.robot.navigation_system.left()
        self.assertEqual(self.robot.position()[2], end_d_l)
        # right rotations
        self.robot.place(0, 0, start_d)
        for m in range(0, times):
            self.robot.navigation_system.right()
        self.assertEqual(self.robot.position()[2], end_d_r)

    @data((0, 0, "NORTH"), (1, 2, "EAST"), (3, 3, "WEST"), (2, 2, "SOUTH"))
    @unpack
    def test_report_robot_position(self, x, y, d):
        self.robot.place(x, y, d)
        exp = "Coordinate(x,y): {x}, {y}. Position {direction}".format(x=x,
                                                                       y=y,
                                                                       direction=d)
        self.assertEqual(self.robot.report(), exp)
