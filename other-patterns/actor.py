import asyncio

class Actor:
    def __init__(self, name):
        self.name = name

    async def receive_message(self, message):
        print(f"{self.name} received: {message}")
        await self.process_message(message)

    async def process_message(self, message):
        print(f"{self.name} is processing: {message}")
        await asyncio.sleep(1)  # Simulate async work
        print(f"{self.name} finished processing: {message}")
        await self.send_message("Reply to " + message)

    async def send_message(self, message):
        print(f"{self.name} is sending: {message}")
        # Here you would normally send the message to another actor

async def main():
    actor1 = Actor("Actor1")
    actor2 = Actor("Actor2")
    
    await asyncio.gather(
        actor1.receive_message("Message 1 for Actor1"),
        actor2.receive_message("Message 2 for Actor2")
    )

if __name__ == "__main__":
    asyncio.run(main())