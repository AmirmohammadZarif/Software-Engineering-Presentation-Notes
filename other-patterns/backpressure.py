import asyncio

class Producer:
    def __init__(self, queue):
        self.queue = queue

    async def produce(self):
        for i in range(5):
            await self.queue.put(i)
            print(f"Produced {i}")
            await asyncio.sleep(1)  # Simulate work

class Consumer:
    def __init__(self, queue):
        self.queue = queue

    async def consume(self):
        while True:
            item = await self.queue.get()
            if item is None:
                break
            print(f"Consumed {item}")
            await asyncio.sleep(2)  # Simulate work

async def main():
    queue = asyncio.Queue(maxsize=3)  # Backpressure with max size
    producer = Producer(queue)
    consumer = Consumer(queue)

    # Run producer and consumer concurrently
    await asyncio.gather(producer.produce(), consumer.consume())

if __name__ == "__main__":
    asyncio.run(main())