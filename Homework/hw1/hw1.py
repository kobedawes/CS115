############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# CS115 Hw1
############################################################

from functools import reduce


def mult(x, y):
    """a function that multiplies two variables together"""
    return x*y


def factorial(n):
    """a function that returns 1 if 0 is, and returns the factorial up to the indicated integer"""
    if n == 0:
        fnumber = 1
    else:
        fnumber = reduce(mult, range(1, int(n)+1))

    return fnumber


def sum(x, y):
    """adds two varioables together"""
    return x+y


def mean(l):
    """finds the mean by dividing the list sum by lsit count"""
    listcount = len(l)
    listtotal = reduce(sum, l)
    return float(listtotal/listcount)


