import asyncio
import time

def say_hello():
    time.sleep(2)
    print("Hello, Async World? (not yet)")

async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async World!")

say_hello()
asyncio.run(say_hello_async())