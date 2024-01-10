#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    Floar arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    # Check if a and b are integers or floats
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    # Return the addition of a and b as an integer
    return (int(a) + int(b))
