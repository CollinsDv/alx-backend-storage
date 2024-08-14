import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any

class Cache:
    """A class initializing a Redis instance"""
    def __init__(self) -> None:
        """Creates a Redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store input data in Redis with a random key
        Args:
            data (str, bytes, int, float): Data to be stored

        Returns:
            str: The random key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Gets key's value from redis and converts
            result byte  into correct data type
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers
        """
        return int(data)
