import asyncio

async def first_coroutine():
    print("Starting first coroutine")
    await asyncio.sleep(2)  # Simulate I/O-bound operation
    print("First coroutine finished")

async def second_coroutine():
    print("Starting second coroutine")
    await asyncio.sleep(1)
    print("Second coroutine finished")

async def main():
    await asyncio.gather(first_coroutine(), second_coroutine())

if __name__ == "__main__":
    asyncio.run(main())