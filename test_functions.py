from function import add, subtract, multiply
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"
