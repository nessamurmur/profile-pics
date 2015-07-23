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

    @given(strategies.integers(min_value=0, max_value=20))
    def test_fibonacci_sequence(self, n):
        x = fibonacci(n)
        y = fibonacci(n+1)
        z = fibonacci(n+2)
        assert x + y == z
