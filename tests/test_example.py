# -*- coding: utf-8 -*-

""" Example implementation of common calculater functionality to demonstrate TDD. 


SPDX-FileCopyrightText: 2023 Jonas Huber <@jh-RLI>
SPDX-FileCopyrightText: © Reiner Lemoine Institut

SPDX-License-Identifier: MIT
"""

from super_repo.example_calculator import add, subtract, multiply, divide

def test_addition():
    result = add(3, 4)
    assert result == 7

def test_subtraction():
    result = subtract(10, 5)
    assert result == 5

def test_multiplication():
    result = multiply(2, 6)
    assert result == 12

def test_division():
    result = divide(15, 3)
    assert result == 5
