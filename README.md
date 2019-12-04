
# toy-robot


Toy Robot Code Challenge
Which I wrote for some firm (Similar to biological name for the circular strucure in human eye) , The final response was a no :), as there was a need for some "out of the box" dev, from the looks of their stocks [Dec 2019 12.70 AUD -2% from yesterday] they are still searching for that "out of box" thinking rather than doing something productive in the box. 


Feel free to use the code abuse the code. (this code is an overkill anyways for the kind of work it is doing). 
Suggestions to make it more over engineered are --> 
Add more object orientation

Decorators always impress people. 

Try checking monads and implementing them to do something pretty useless somewhere. 

Finally --> 

Find a dot net (visual studio specially) devleoper and ask him/her how he will refactor the code. 



... happy coding

# CI (Build status) by Travis
[![Build Status](https://travis-ci.com/tanmaydattta/toy-robot.svg?branch=master)](https://travis-ci.com/tanmaydattta/toy-robot)

* Written in Python3

## Setup
- Manual
    - `virtualenv venv`
    - source `venv\bin\activate`
    - `pip install -r requirements.txt`
    - All setup !!

- Makefile
    - `make venv`
    - if venv exist and you want to reset
        -- `make force_venv`

## Usage
* Run:
    `python3 run.py` 
* Help: 
    - ? for available commands
    - For particular command
      `help command`

* Console is "Case insensitive" place == PlAce == PLACE

* Quit:
    - press `q`
    - press `Ctrl + c`
 

** Any error --> Switch debuging level for logger.

## Test
    `python3 -m unittest tests/test_Robot.py`

