#!/usr/bin/env python3
"""Execute multiple coroutines concurrently"""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random `n` times with the specified `max_delay`
    wait_n should return the list of all the delays (float values)
    """
    futures = []
    for _ in range(n):
        futures.append(asyncio.create_task(wait_random(max_delay)))

    delays = []

    # Collect delays as soon as thay are ready
    for future in asyncio.as_completed(futures):
        delay = await future
        delays.append(delay)

    return delays
