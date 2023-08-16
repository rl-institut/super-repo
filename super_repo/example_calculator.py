# -*- coding: utf-8 -*-

"""
Example implementation of test for the calculater functionality
to demonstrate TDD.


SPDX-FileCopyrightText: 2023 Jonas Huber <@jh-RLI>
SPDX-FileCopyrightText: © Reiner Lemoine Institut

SPDX-License-Identifier: MIT
"""


def add(a, b):
    """
    Add two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The result of subtracting b from a.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The product of the two numbers.
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    :param a: The numerator.
    :param b: The denominator.
    :return: The result of dividing a by b.
    :raises ValueError: If division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
