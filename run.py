# -*- coding: utf-8 -*-
"""
Main module for driving the toy robot

"""
import logging.config
from cmd import Cmd

from robot import Robot
from table import Table

__author__ = "tanmay.datta86@gmail.com"
logging.config.fileConfig('logging.config',
                          disable_existing_loggers=False)


class RobotPrompt(Cmd):
    """
    New shiny prompt for our robot
    """
    intro = """Welcome to the toy robot shell.
    To quit you can just type q and enter or just press Ctrl+C
    Type help or ? to list commands.\n"""
    prompt = '(Toy robot) '
    robot = Robot(Table(5, 5))

    def do_place(self, place_cmd):
        """
        Places a robot on the the defaul 5X5 table.
        Position (x,y) and facing "F"

        Syntax is place[PLACE] x,y,f(acing)
        example place 4,4,EAST => place at 4,4 facing EAST
        """
        x_coord, y_coord, direction = place_cmd.split(",")
        x_coord = int(x_coord)
        y_coord = int(y_coord)
        direction = direction.upper()
        self.robot.place(x_coord, y_coord, direction)
        print("okay this works nicely {}".format(direction))

    def do_move(self, line):
        """
        Moves the robot in the direction it is facing
        | x |  |
        Move
        |   | x |
        (Given it is facing East)
        """
        print(line)
        self.robot.navigation_system.move()

    def do_left(self, _line):
        """
        Moves robot to it's left direction
        ----->
        Issued Left
        ^
        |
        |
        |
        """
        self.robot.navigation_system.left()

    def do_right(self, _line):
        """
        Moves robot to it's right direction
        ----->
        Issued Right
        |
        |
        |
        V
        """
        self.robot.navigation_system.right()

    def do_report(self, _line):
        """
        Prints the location of robot
        Prints nothing if robot is not "placed" yet
        """
        print(_line)
        print(self.robot.report())

    def precmd(self, line):
        line = line.lower()
        if line == "q":
            print("quitting")
            exit(0)
        return line


if __name__ == "__main__":
    PROMPT = RobotPrompt()
    PROMPT.cmdloop()
