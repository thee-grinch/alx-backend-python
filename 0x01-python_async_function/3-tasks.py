#!/usr/bin/env python3
"""module that takes an returns a asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task that
    waits for a random number of seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task object that
          the asynchronous task.

    """
    return asyncio.create_task(wait_random(max_delay))
