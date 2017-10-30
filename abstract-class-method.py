'''
abstract method : do we really need this?

refer https://docs.python.org/2/library/abc.html



This module provides the infrastructure for defining abstract base classes (ABCs) in Python,
as outlined in PEP 3119; see the PEP for why this was added to Python.
(See also PEP 3141 and the numbers module regarding a type hierarchy for numbers based on ABCs.)
'''



from abc import ABCMeta

class MyABC:
    __metaclass__ = ABCMeta

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
