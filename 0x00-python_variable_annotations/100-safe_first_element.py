#!/usr/bin/env python3
"""Doc module"""
from typing import Sequence, Any, Union
"""Import all the need modules"""


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function return the rigth"""
    if lst:
        return lst[0]
    else:
        return None
