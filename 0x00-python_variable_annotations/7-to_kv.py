#!/usr/bin/env python3
"""Import of all the modules"""
from typing import Union, Tuple
"""Doc module"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2)
