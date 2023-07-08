"""This module contains the functions needed to call the fibonacci sequence
"""
import logging
from functools import lru_cache
from typing import List
from perf_timer import run_time

# Setup Module Level Logging for our Running Module

# Set Instance of Logging for file
log = logging.getLogger(__name__)

# Set Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "", "%"
)

# Set Stream Handler instance and add formatter
# This outputs text to the terminal
sh = logging.StreamHandler()
sh.setFormatter(formatter)
# sh.setLevel(logging.DEBUG)
log.addHandler(sh)

# Set Filehandler instance and formatter
# This creates a file where the logged data is stored
# By default, mode is a, encoding is None, delay is False
fh = logging.FileHandler(f"{__name__}_data.log", mode="a")
fh.setFormatter(formatter)
# fh.setLevel(logging.DEBUG)
log.addHandler(fh)

# Set Logging Level
log.setLevel(logging.DEBUG)


# Define fibonacci function
# Define fibonacci numbers function
# @run_time
@lru_cache(maxsize=10)
def fibonacci(end: int, first: int = 0, second: int = 1) -> List[int]:
    """_summary_
    Return a list of fibonacci sequence upto a maximum number

    Args:
        end (int): _description_
        first (int, optional): _description_. Defaults to 0.
        second (int, optional): _description_. Defaults to 1.

    Returns:
        list[int]: _description_
    """
    # Alternatively:
    # lst = [first, second]
    log.info(f"Passed argument is {end}")
    # Initialize list
    lst = []
    log.info(f"List is {lst} - initializing function")

    # Initialize early numbers
    x_0 = first  # First number
    x_1 = second  # Second number
    log.info(f"x_0 and x_1 are {x_0},{x_1} - initializing function")

    # Put early numbers into initialized list
    lst.append(x_0)
    lst.append(x_1)

    log.info(f"List is {lst} - initializing function")

    # Nth number
    x_n = lambda a, b: a + b  # Consecutive nth number

    while lst[-1] <= end:
        lst.append(x_n(lst[-1], lst[-2]))
        log.info(f"List is {lst} - running function...")

        if lst[-1] > end:
            lst.pop(-1)
            break

    return lst
