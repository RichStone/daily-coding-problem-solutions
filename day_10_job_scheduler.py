"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
from time import sleep


def scheduler(f, ms):
    sleep(ms / 1000)
    f()


def fun():
    print('guu')


scheduler(fun, 1000)
