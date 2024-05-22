#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and implements an LFU caching system
    with a limited size.
    """

    def __init__(self):
        """ Initialize the cache data dictionary, frequency tracker, and usage order """
        super().__init__()  # Call parent class constructor
        self.cache_data = {}  # Key-value pairs
        self.freq_counter = defaultdict(int)  # Tracks access frequency for each key
        self.usage_order = {}  # Ordered dictionary for usage within each frequency level
        for freq in range(1, BaseCaching.MAX_ITEMS + 1):
            self.usage_order[freq] = OrderedDict()  # Separate OrderedDict for each freq

    def put(self, key, item):
        """
        Adds an item to the cache dictionary, following LFU eviction.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Existing key: update frequency and usage order
                self.freq_counter[key] += 1
                self.usage_order[self.freq_counter[key]].move_to_end(key)  # Update usage
            else:
                # New key: check if cache is full
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self.discard_least_frequent()
                self.freq_counter[key] = 1  # Initial frequency is 1
                self.usage_order[1][key] = item  # Add to usage order for frequency 1

            self.cache_data[key] = item  # Update cache data dictionary

    def get(self, key):
        """
        Retrieves an item from the cache dictionary and updates its frequency.
        """
        if key is not None and key in self.cache_data:
            self.freq_counter[key] += 1  # Update access frequency
            self.usage_order[self.freq_counter[key]].move_to_end(key)  # Update usage order
            return self.cache_data[key]
        return None

    def discard_least_frequent(self):
        """
        Discards the least frequently used item (LFU) or least recently used within the least frequency.
        """
        lowest_freq = min(self.freq_counter.keys())
        # Get the least recently used item from the lowest frequency OrderedDict
        discard_key = self.usage_order[lowest_freq].popitem(last=False)[0]
        del self.cache_data[discard_key]
        del self.freq_counter[discard_key]
        print(f"DISCARD: {discard_key}")

