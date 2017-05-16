#!/bin/python

# TailCall
#
# Takes a closure over function and creates a
# callable object. The closure object is not executed on its own,
# unless it is used as the the return value of a TailCallable object
class TailCall:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args):
        return self.fn(*args)

# TailCallable
#
# Takes a function which returns a TailCall, and 
# creates a callable object which mimics
# a tail call optimized function.
    
class TailCallable:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args):
        acc = self.fn(*args)
        while (isinstance(acc, TailCall)):
            acc = acc()
        return acc
