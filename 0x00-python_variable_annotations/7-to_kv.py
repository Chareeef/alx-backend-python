#!/usr/bin/env python3
""" Type-annotated `to_kv` function """
from functools import reduce
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Take a string k and an int OR float v  and returns a tuple """
    return (k, v ** 2)
