from fastapi import FastAPI
import redis
import debugpy

app = FastAPI()

r = redis.Redis(host="redis", port = 6379)

debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
async def root():
    return {"message": "Hello World docker compose1"}

@app.get("/hits")
async def root():
    r.incr("hits")
    value = r.get("hits")
    print("hits count on console:", value.decode())
    return {"num of hits": r.get("hits")}