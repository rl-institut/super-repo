# -*- coding: utf-8 -*-

""" Example implementation of test for the calculater functionality to demonstrate TDD. 


SPDX-FileCopyrightText: 2023 Jonas Huber <@jh-RLI>
SPDX-FileCopyrightText: © Reiner Lemoine Institut

SPDX-License-Identifier: MIT
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
