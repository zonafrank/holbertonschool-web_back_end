#!/usr/bin/env python3
"""Module for async_comprehension coroutine"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
    """
    return [val async for val in async_generator()]
