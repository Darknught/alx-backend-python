#!/usr/bin/env python3
""" Module that imports an async function and handles multiple."""
import asyncio
import importlib.util
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Takes in two int args and spawn wait_random n times with a specified
    max_delay.
    Returns a list of all the delays(float) and should be in ascending order
    """
    # Dynamic import of wait_random from basic_async_syntax.py
    spec = importlib.util.spec_from_file_location(
            "basic_async_syntax", "0-basic_async_syntax.py")
    basic_async_syntax = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(basic_async_syntax)
    wait_random = basic_async_syntax.wait_random

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Sorts the list without using sort()
    sorted_delays = []
    while delays:
        minimum_delay = min(delays)
        delays.remove(minimum_delay)
        sorted_delays.append(minimum_delay)

    return sorted_delays
