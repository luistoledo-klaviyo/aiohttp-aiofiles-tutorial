"""Create and execute asynchronous tasks in a loop."""
import asyncio

from asyncio_tutorial.logger import LOGGER

from .coroutines import simple_coroutine
from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_task


async def asyncio_intro_tutorial():
    """Demo of an asynchronous script's lifecycle."""
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    task_list = []
    future = register_future()
    for i in range(3):
        task = await create_task(simple_coroutine(i, delay=1))
        task_list.append(task)
    inspect_event_loop()
    await asyncio.gather(*task_list)
    future.set_result("Done")
