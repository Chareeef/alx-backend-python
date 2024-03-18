#!/usr/bin/env python3
"""Measure execution time"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    Returns (total_time / n)
    """
    # Get event loop
    loop = asyncio.get_event_loop()

    # Start clock
    start = time.time()

    # Run wait_n until completion
    loop.run_until_complete(wait_n(n, max_delay))

    # Stop clock and get total_time
    end = time.time()
    total_time = end - start

    # Close loop
    loop.close()

    return total_time / n
