#!/usr/bin/env python3
from typing import List
"""Doc module"""


def sum_list(input_list: List[float]) -> float:
    """This function return the sum of list of float"""
    result: float = 0.0
    for item in input_list:
        result += item
    return (result)
