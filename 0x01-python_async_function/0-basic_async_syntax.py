#!/usr/bin/env python3
"""a function that tasks a random number and waits for it"""
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait_random: async routine that waits for a random delay

    Args:
        max_delay (int): maximum delay in seconds

    Returns:
        float: the random delay
    """
    import random
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
