# -*- coding: utf-8 -*-
"""
Main module for driving the toy robot

"""
from cmd import Cmd
import logging.config

from robot import Robot

__author__ = "tanmay.datta86@gmail.com"
logging.config.fileConfig('logging.config',
                          disable_existing_loggers=False)


class RobotPrompt(Cmd):
    intro = """Welcome to the toy robot shell.
    To quit you can just type q and enter or just press Ctrl+C
    Type help or ? to list commands.\n"""
    prompt = '(Toy robot) '

    def do_place(self, x_coord, y_coord, face):
        """
        Places a robot on the the defaul 5X5 table.
        Position (x,y) and facing "F"

        Syntax is place[PLACE] x,y,f(acing)
        example place 4,4,EAST => place at 4,4 facing EAST
        """
        print("okay this works nicely {}".format(x_coord))

    def do_move(self):
        """
        Moves the robot in the direction it is facing
        | x |  |
        Move
        |   | x |
        (Given it is facing East)
        """
        pass

    def do_left(self):
        """
        Moves robot to it's left direction
        ----->
        Issued Left
        ^
        |
        |
        |
        """
        pass

    def do_right(self):
        """
        Moves robot to it's right direction
        ----->
        Issued Right
        |
        |
        |
        V
        """
        pass

    def do_report(self):
        """
        Prints the location of robot
        Prints nothing if robot is not "placed" yet
        """
        pass

    def precmd(self, line):
            line = line.lower()
            if line == "q":
                print("quitting")
                exit(0)
            return line


if __name__ == "__main__":
    prompt = RobotPrompt()
    prompt.robot = Robot()
    prompt.cmdloop()
