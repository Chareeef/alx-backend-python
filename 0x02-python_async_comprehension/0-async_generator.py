#!/usr/bin/env python3
"""A Basic Asynchronous generator"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """10 times sleep and yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
