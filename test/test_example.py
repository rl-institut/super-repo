"""

Example implementation of common calculater functionality to
demonstrate TDD.

SPDX-FileCopyrightText: 2023 Jonas Huber <https://github.com/jh-rli> © Reiner Lemoine Institut
SPDX-FileCopyrightText: 2023 Ludwig Hülk <https://github.com/Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
SPDX-License-Identifier: MIT
"""

from pytest import raises

from super_repo.example_calculator import add, divide, multiply, subtract


def test_addition():
    """Test addition.

    Test addition function.
    """
    result = add(3, 4)
    assert result == 7


def test_subtraction():
    """Test subtraction.

    Test subtraction function.
    """
    result = subtract(10, 5)
    assert result == 5


def test_multiplication():
    """Test multiplication.

    Test multiplication function.
    """
    result = multiply(2, 6)
    assert result == 12


def test_division():
    """Test division.

    Test division function.
    """
    result = divide(15, 3)
    assert result == 5


def test_division_zero():
    """Test division with zero.

    Test division function fail.
    """
    with raises(ValueError, match=r"Cannot divide by zero"):
        divide(15, 0)
