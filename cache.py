import redis
from dotenv import load_dotenv
import os
from redis.cache import CacheConfig

puerto_pc = int(os.environ.get("PORT", 5000))

load_dotenv()

r = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    username=os.getenv('REDIS_USERNAME'),
    password=os.getenv('REDIS_PASSWORD'),
    ssl=False,
    protocol=3,
    cache_config=CacheConfig(),
    decode_responses=True
)

if r.ping():
    print("Conexión a Redis establecida")
    