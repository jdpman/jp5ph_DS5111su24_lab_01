# test_fail.py

import pytest

@pytest.mark.xfail()
def test_fail_on_purpose():
    expected = 1
    actual = 2
    assert actual == expected, f"Expected {expected}, but got {actual}"

@pytest.mark.xfail()
def test_fail_integration():
    expected = "hello"
    actual = "world"
    assert actual == expected, f"Expected '{expected}', but got '{actual}'"

