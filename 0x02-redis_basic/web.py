#!/usr/bin/env python3
"""Module to test web cache expiry and tracker"""
import requests
import redis
from typing import Callable
from functools import wraps


r = redis.Redis()
r.flushdb()

def cache_page(fn: Callable) -> Callable:
    """"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """"""
        key = f"{fn.__qualname__}:{args}"
        response = r.get(key)
        if response:
            r.incr(f"count:{args}")
            return response
        else:
            response = fn(*args, **kwargs)
            r.setex(key, 10, response)
            # r.incr(f"count:{args}")
            return response
    return wrapper

@cache_page
def get_page(url: str) -> str:
    """Returns HTML content"""
    response = requests.get(url)
    return response.text


def main():
    """Main function"""
    url = "http://slowwly.robertomurray.co.uk"
    get_key = f"{get_page.__qualname__}:('{url}',)"
    count_key = f"count:('{url}',)"
    get_page(url)
    get_page(url)
    get_page(url)
    get_page(url)
    get_page(url)
    get_page(url)
    get_page(url)
    get_page(url)

    print(r.get(get_key).decode('utf-8'))
    print(r.get(count_key).decode('utf-8'))

if __name__ == "__main__":
    main()
