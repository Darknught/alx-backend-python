#!/usr/bin/env python3
""" Module that imports async_generator and write another coroutine."""
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine collects 10 random numbers using async comprehension
    over async_generator then returns 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
