#!/usr/bin/env python3
from typing import Callable
"""Doc module"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function"""
    def fun(x: float) -> float:
        """A callable function"""
        return x * multiplier
    return fun
