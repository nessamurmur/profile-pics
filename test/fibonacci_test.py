from hypothesis import given, assume
from importer.fib import fibonacci
import hypothesis.strategies as strategies
import unittest


class FibonacciTest(unittest.TestCase):
    @given(strategies.integers())
    def test_recursive_fibonacci(self, n):
        assume(n > 0)
        assume(n < 20)
        assert isinstance(fibonacci(n), n.__class__)
