"""Custom math functions"""

from math import (
    pow,
    sqrt,
)


def cross(a, b):
    """return a x b"""
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c


def length(vect):
    return sqrt(pow(vect[0],2) + pow(vect[1],2) + pow(vect[2],2))