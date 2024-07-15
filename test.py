import pytest
from main import count_vowels

def test_vowels_only():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3
    assert count_vowels("PYTHON programming") == 4

@pytest.mark.parametrize("input_string, expected_count", [
    ("aeiou", 5),
    ("AEIOU", 5),
    ("bcdfg", 0),
    ("BCDFG", 0),
    ("Hello World", 3),
    ("PYTHON programming", 4),
])
def test_parametrized(input_string, expected_count):
    assert count_vowels(input_string) == expected_count
