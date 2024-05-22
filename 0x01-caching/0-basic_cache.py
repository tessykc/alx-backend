#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and implements a basic caching system
    without size limits.
    """

    def __init__(self):
        """ Initialize the cache data dictionary """
        super().__init__()  # Call parent class constructor

    def put(self, key, item):
        """
        Adds an item to the cache dictionary.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache dictionary.
        """
        return self.cache_data.get(key)
