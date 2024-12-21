import requests
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_file(url):
    response = requests.get(url)
    return f"Downloaded {url}, Size: {len(response.content)} bytes"

def save_to_db(data):
    
    return f"Saved to DB: {data}"

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1"
]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_file, url) for url in urls]

    for future in as_completed(futures):
        download_result = future.result() 
        db_result = save_to_db(download_result) 
        print(db_result)