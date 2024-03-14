#!/usr/bin/env python3
""" Type-annotated `make_multiplier` function """
from typing import Callable


def make_multiplier(multiplier : float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def multiply_func(n: float) -> float:
        return multiplier * n

    return multiply_func
