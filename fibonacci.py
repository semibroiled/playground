"""This module contains the functions needed to call the fibonacci sequence
"""


# Define fibonacci function
# Define fibonacci numbers function
def fibonacci(end: int, first: int = 0, second: int = 1) -> list[int]:
    """_summary_

    Args:
        end (int): _description_
        first (int, optional): _description_. Defaults to 0.
        second (int, optional): _description_. Defaults to 1.

    Returns:
        list[int]: _description_
    """
    # Alternatively:
    # lst = [first, second]

    # Initialize list
    lst = []

    # Initialize early numbers
    x_0 = first  # First number
    x_1 = second  # Second number

    # Put early numbers into initialized list
    lst.append(x_0)
    lst.append(x_1)

    # Nth number
    x_n = lambda a, b: a + b  # Consecutive nth number

    while lst[-1] < end:
        lst.append(x_n(lst[-1], lst[-2]))

    return lst
