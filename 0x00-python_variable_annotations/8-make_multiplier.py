#!/usr/bin/env python3
'''create multiplier closure and return it
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Create a multiplier function.
    '''
    return lambda x: x * multiplier
