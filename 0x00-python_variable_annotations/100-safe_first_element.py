#!/usr/bin/env python3
"""
define a function safe_first_element a duck typed function
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck typed function"""
    if lst:
        return lst[0]
    else:
        return None
