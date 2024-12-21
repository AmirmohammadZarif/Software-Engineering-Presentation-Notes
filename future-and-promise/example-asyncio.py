import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.text()
        return f"Fetched {url}, Length: {len(data)}"

async def process_data(data):
    await asyncio.sleep(1)  
    return f"Processed: {data[:50]}..." 

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    async with aiohttp.ClientSession() as session:
        fetch_futures = [fetch_data(session, url) for url in urls]
        
        fetch_results = await asyncio.gather(*fetch_futures)

        process_futures = [process_data(result) for result in fetch_results]
        process_results = await asyncio.gather(*process_futures)

        for result in process_results:
            print(result)

asyncio.run(main())