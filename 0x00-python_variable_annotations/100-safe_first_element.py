#!/usr/bin/env python3
""" Type-annotated `safe_first_element` function """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safely return the first element of `lst` """
    if lst:
        return lst[0]
    else:
        return None
