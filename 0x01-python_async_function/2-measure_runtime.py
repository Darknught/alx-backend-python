#!/usr/bin/env python3
""" Function that measures total execution time."""
import time
import asyncio
from typing import List
import importlib.util


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
    """
    # Dynamic import of wait_n from 1-concurrent_coroutines.py
    spec = importlib.util.spec_from_file_location(
            "concurrent_coroutines", "1-concurrent_coroutines.py")
    concurrent_coroutines = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(concurrent_coroutines)
    wait_n = concurrent_coroutines.wait_n

    start_time = time.time()

    # Run the wait_n function
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
