#!/usr/bin/env python3
""" Type-annotated `to_str` function """
from functools import reduce
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ Takes a list input_list of floats as argument
    and returns their sum as a float
    """
    return float(reduce(lambda x, y: x + y, input_list))
