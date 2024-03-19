#!/usr/bin/env python3
"""A Basic Asynchronous Comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect and return 10 random numbers using an
    async comprehension over async_generator
    """
    comprehension = (n async for n in async_generator())

    numbers = []

    async for n in comprehension:
        numbers.append(n)

    return numbers
