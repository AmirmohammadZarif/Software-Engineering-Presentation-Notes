from fastapi import FastAPI
import asyncio

app = FastAPI()

async def get_user_data(user_id: int):
    await asyncio.sleep(1)  
    return {"user_id": user_id, "name": f"User {user_id}", "role": "Admin"}

@app.get("/user/{user_id}")
async def fetch_user(user_id: int):
    user_data = await get_user_data(user_id)
    return {"status": "success", "data": user_data}


@app.get("/users/")
async def fetch_users(user_ids: str):
    ids = list(map(int, user_ids.split(","))) 
    tasks = [get_user_data(user_id) for user_id in ids]
    results = await asyncio.gather(*tasks) 
    return {"status": "success", "data": results}