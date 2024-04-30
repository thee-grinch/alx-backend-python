#!/usr/bin/env python3
"""Type-annotated function element_length
that takes a list lst as argument and returns the
length of the list as a tuple."""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Return a tuple of the length of a list and a list of the lengths of each element."""
    return (len(lst), [len(i) for i in lst])
