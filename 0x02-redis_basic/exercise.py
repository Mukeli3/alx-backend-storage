#!/usr/bin/env python3
"""
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self.redis = redis.Redis()
        self._redis.flushdb()  # clear the Redis database

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uui.uuid4())  # generate a random key
        self._redis.set(key, data)  # store data in Redis
        return key  # return key
