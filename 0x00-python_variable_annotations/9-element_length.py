#!/usr/bin/env python3
"""Doc module"""
from typing import Iterable, Sequence, List, Tuple
"""Import of all modules"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function return the length of an element"""
    return [(i, len(i)) for i in lst]
