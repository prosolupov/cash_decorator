import redis.asyncio as redis


class RedisConnector:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.redis = None

    async def connect(self):
        self.redis = await redis.Redis(host=self.host, port=self.port)
        return self.redis

    async def set(self, key: str, value: str):
        self.redis.set(key, value)

    async def get(self, key: str):
        self.redis.get(key)

    async def delete(self, key: str):
        self.redis.delete(key)

    async def disconnect(self):
        self.redis.close()
