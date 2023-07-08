import pytest
from typing import Tuple, List
import sys
import os

# Add Root directory to path to import local modules
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_directory)

from fibonacci import fibonacci


# Generate Test Datal
@pytest.fixture
def get_test_fibonacci_data() -> List[Tuple[int, int, int]]:
    return [(10_000, -1, 10_946), (15, -1, 21)]


# Fibonacci function tests
def test_fibonacci(get_test_fibonacci_data):
    for data in get_test_fibonacci_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert fibonacci(num1)[num2] == expected


def test_fibonacci_output_type():
    assert type(fibonacci(10)) is list
    assert type(fibonacci(10)[3]) is int
