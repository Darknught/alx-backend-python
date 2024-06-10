#!/usr/bin/env python3
""" Module that defines an Asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function Takes in an integer argument with default val of 10
    then waits for a random delay btw 0 and max_delay seconds and
    eventually returns it.
    """
    sleep_time = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
