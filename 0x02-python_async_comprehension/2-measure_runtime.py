#!/usr/bin/env python3
"""Measure the runtime of async_comprehension function"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute `async_comprehension` four times concurrently using
    `asyncio.gather`, measure the total runtime and return it
    """
    # Start clock
    start = time.time()

    # Create four tasks
    tasks = []
    for _ in range(4):
        task = asyncio.create_task(async_comprehension())
        tasks.append(task)

    # Execute them
    await asyncio.gather(*tasks)

    # End clock
    end = time.time()

    # Return the runtime
    return end - start
