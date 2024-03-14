#!/usr/bin/env python3
""" Type-annotated `to_str` function """
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """ Takes a list input_list of floats as argument
    and returns their sum as a float
    """
    return reduce(lambda x, y: x + y, input_list)
