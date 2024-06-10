#!/usr/bin/env python3
""" An async function that imports and use regular function syntax."""
import asyncio
import importlib.util
from typing import Coroutine


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Takes in an integer and returns asyncio.Task"""

    # Dynamic import of wait_random from basic_async_syntax.py
    spec = importlib.util.spec_from_file_location(
            "basic_async_syntax", "0-basic_async_syntax.py")
    basic_async_syntax = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(basic_async_syntax)
    wait_random = basic_async_syntax.wait_random

    # Create a coroutine object with the wait_random function
    coroutine = wait_random(max_delay)

    # wrap the coroutine in an asyncio.Task object
    task = asyncio.create_task(coroutine)
    return task
