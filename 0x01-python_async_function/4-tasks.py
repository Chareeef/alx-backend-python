#!/usr/bin/env python3
"""Execute multiple coroutines (tasks)concurrently"""
import asyncio
import typing


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn and run task_wait_random `n` times with the specified `max_delay`
    wait_n should return the list of all the delays (float values)
    """
    futures = []
    for _ in range(n):
        futures.append(task_wait_random(max_delay))

    delays = []

    # Collect delays as soon as thay are ready
    for future in asyncio.as_completed(futures):
        delay = await future
        delays.append(delay)

    return delays
