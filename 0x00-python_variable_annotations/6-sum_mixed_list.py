#!/usr/bin/env python3
"""Import of all modules"""
from typing import List, Union
"""Doc module"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function return the sum of a list of int and float"""
    return sum(mxd_lst)
