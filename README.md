
# toy-robot


Toy Robot Code Challenge
Which I wrote for some firm in Melbourne, The final response was a no :), it seems that I was a "product of my environment" (Don't know what it means) and they wanted some "out of the box" guy. 

Feel free to use the code abuse the code. (this code is an overkill anyways for the kind of work it is doing). 
Suggestions to make it more over engineered are welcome. ;) ... happy coding

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

