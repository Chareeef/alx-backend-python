#!/usr/bin/env python3
""" Type-annotated `element_length` function """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuples (item, item_length) for each `lst`'s item """
    return [(i, len(i)) for i in lst]
