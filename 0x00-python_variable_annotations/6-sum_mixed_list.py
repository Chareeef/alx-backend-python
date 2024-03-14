#!/usr/bin/env python3
""" Type-annotated `sum_mixed_list` function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Takes a list mxd_lst of floats OR integers as argument
    and returns their sum as a float
    """
    result: float = 0

    for n in mxd_lst:
        result += n

    return float(result)
