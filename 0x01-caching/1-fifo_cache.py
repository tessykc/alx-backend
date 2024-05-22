#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and implements a FIFO caching system
    with a limited size.
    """

    def __init__(self):
        """ Initialize the cache data dictionary and FIFO order """
        super().__init__()  # Call parent class constructor
        self.cache_order = []  # List to keep track of insertion order

    def put(self, key, item):
        """
        Adds an item to the cache dictionary, following FIFO eviction.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # FIFO eviction
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.cache_order.append(key)  # Update insertion order

    def get(self, key):
        """
        Retrieves an item from the cache dictionary.
        """
        return self.cache_data.get(key)
