import pytest

# Example list for testing
my_list = [1, 3, 5, 7, 9]

# Write your Python program below
@pytest.fixture
def test_contains_five(test_list):
    assert 5 in test_list
