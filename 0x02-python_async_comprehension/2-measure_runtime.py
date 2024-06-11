#!/usr/bin/env python3
""" A coroutine that will execute async_comprehension four times in parallel
using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ The function measures the runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = time.perf_counter()

    # Executing async_comprehension four times in parallel
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
    )

    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
