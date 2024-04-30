#!/usr/bin/env python3
"""Type-annotated function element_length
that takes a list lst as argument and returns the
length of the list as a tuple."""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]