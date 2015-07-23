from hypothesis import given, assume
from importer.fib import fibonacci
import hypothesis.strategies as strategies
import unittest


class FibonacciTest(unittest.TestCase):
