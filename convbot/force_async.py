"""Turn a sync func to async."""
from concurrent.futures import ThreadPoolExecutor
import asyncio
import functools


def force_async(func):
    """Turn a sync func to async.

    Args:
        func: a sync func

    Return:
        async func

    Usage:
        @force_async
        def normal_func():
            ...
        loop = asyncio.get_event_loop()
        #~ tasks = [sync_loop1(1, 5), sync_loop1(2, 10)]
        #~ res = loop.run_until_complete(asyncio.gather(*tasks))  # OK
        res = loop.run_until_complete(
            asyncio.gather(
                *[
                    sync_loop1(1, 7),
                    sync_loop1(2, 6),
                    sync_loop1(2, 6),
                    async_func,
                ]
            )
        )
    """
    # executor = ThreadPoolExecutor()
    # from concurrent.futures import ThreadPoolExecutor
    executor = ThreadPoolExecutor(max_workers=10)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Preserve func info."""
        future = executor.submit(func, *args, **kwargs)
        return asyncio.wrap_future(future)  # make it awaitable

    return wrapper
