#!/usr/bin/python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements an MRU caching system
    with a limited size.
    """

    def __init__(self):
        """ Initialize the cache data dictionary and a linked list for usage tracking """
        super().__init__()  # Call parent class constructor
        self.cache_order = collections.OrderedDict()  # Ordered dictionary for MRU tracking

    def put(self, key, item):
        """
        Adds an item to the cache dictionary, following MRU eviction.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move existing key to the front (most recently used)
                self.cache_order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # MRU eviction (remove least recently used)
                    discarded_key = self.cache_order.popitem(last=False)
                    del self.cache_data[discarded_key[0]]
                    print(f"DISCARD: {discarded_key[0]}")
                self.cache_order[key] = item  # Add to ordered dict (most recently used)
                self.cache_data[key] = item  # Add to cache data dictionary

    def get(self, key):
        """
        Retrieves an item from the cache dictionary.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the front (most recently used)
            self.cache_order.move_to_end(key)
            return self.cache_data[key]
        return None
