from fastapi import FastAPI, Request
import time
import asyncio
import asyncpg
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


app = FastAPI()


async def create_db_connection():
    return await asyncpg.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)

async def aggregate_metrics(url):
    conn = await create_db_connection()

    avg_response_time, request_count = await conn.fetchrow('''
        SELECT AVG(response_time), COUNT(*)
        FROM api_usage_logs
        WHERE url = $1
        ''', url)

    await conn.close()

    print(f"URL:{url}, Average Response Time:{avg_response_time:.2f} seconds, Request Count:{request_count}")

@app.middleware("http")
async def log_api_usage(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    conn = await create_db_connection()
    await conn.execute('''
        INSERT INTO api_usage_logs(url, method, response_time, timestamp)
        VALUES($1, $2, $3, NOW())
        ''', str(request.url), request.method, duration)

    await conn.close()

    asyncio.create_task(aggregate_metrics(str(request.url)))

    return response

@app.get("/")
async def read_root():
    return {"message": "API Usage Monitoring in action"}