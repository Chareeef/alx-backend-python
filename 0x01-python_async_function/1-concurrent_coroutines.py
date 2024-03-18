#!/usr/bin/env python3
"""Execute multiple coroutines concurrently"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random `n` times with the specified `max_delay`
    wait_n should return the list of all the delays (float values)
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    return delays
