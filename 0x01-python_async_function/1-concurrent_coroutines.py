#!/usr/bin/env python3
"""a function that tasks a random number and waits for i"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments (n and max_delay)
    and returns a list of delays"""
    import asyncio
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
