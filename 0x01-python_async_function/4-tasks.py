#!/usr/bin/env python3
"""task waut random"""


task_wait_random = __import__('3-tasks').task_wait_random
async def task_wait_n(n: int, max_delay: int) -> float:
    """takes in 2 int arguments (n and max_delay) and returns a list of delays"""
    import asyncio
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays