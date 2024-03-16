#!/usr/bin/env python3
"""Doc module"""
from typing import Mapping, Union, Any, TypeVar
"""Import of all modules"""
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
                    -> Union[Any, T]:
    """This function meet with the requirement"""
    if key in dct:
        return dct[key]
    else:
        return default
