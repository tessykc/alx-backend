#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements an LRU caching system
    with a limited size.
    """

    def __init__(self):
        """ Initialize the cache data dictionary and a dictionary for usage tracking """
        super().__init__()  # Call parent class constructor
        self.cache_order = {}  # Track key usage order (key: access timestamp)

    def put(self, key, item):
        """
        Adds an item to the cache dictionary, following LRU eviction.
        """
        if key is not None and item is not None:
            self.cache_order[key] = self.get_current_time()  # Update usage timestamp
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU eviction
                discarded_key = self.find_least_recently_used()
                del self.cache_data[discarded_key]
                del self.cache_order[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache dictionary, updating its usage timestamp.
        """
        if key is not None and key in self.cache_data:
            self.cache_order[key] = self.get_current_time()  # Update usage timestamp
            return self.cache_data[key]
        return None

    def find_least_recently_used(self):
        """
        Finds the least recently used key based on the usage timestamps.
        """
        least_recent_key = min(self.cache_order, key=self.cache_order.get)
        return least_recent_key

    @staticmethod
    def get_current_time():
        """
        Provides a mechanism to get the current time for usage tracking.
        This can be replaced with a more robust method (e.g., using time.time()).
        """
        return 1  # Placeholder for current time

