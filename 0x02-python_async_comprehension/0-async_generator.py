#!/usr/bin/env python3
""" A coroutine that takes no arg and generate a random number"""
import asyncio
import random


async def async_generator():
    """ takes in one arg and loop 10 times, wait 1 second then yield
    a random number btw 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
