# test example for testing the example module
import unittest


# example.py - Example module with basic arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def test_example_addition():
    assert 1 + 1 == 2
