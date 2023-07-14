# @lc app=leetcode id=460 lang=python3
from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = {}  # Stores the key-value pairs
        self.key_freq = defaultdict(int)  # Stores the frequency of each key
        self.freq_keys = defaultdict(list)  # Stores keys for each frequency
        self.min_freq = 0  # Tracks the minimum frequency in the cache

    def get(self, key: int) -> int:
        if key not in self.key_value:
            return -1

        value = self.key_value[key]
        self.update_frequency(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_value:
            self.key_value[key] = value
            self.update_frequency(key)
        else:
            if len(self.key_value) >= self.capacity:
                self.evict_least_frequent()

            self.key_value[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1].append(key)
            self.min_freq = 1

    def update_frequency(self, key: int) -> None:
        freq = self.key_freq[key]
        self.key_freq[key] += 1

        self.freq_keys[freq].remove(key)
        if len(self.freq_keys[freq]) == 0 and freq == self.min_freq:
            self.min_freq += 1

        self.freq_keys[freq + 1].append(key)

    def evict_least_frequent(self) -> None:
        keys = self.freq_keys[self.min_freq]
        key_to_evict = keys.pop(0)
        del self.key_value[key_to_evict]
        del self.key_freq[key_to_evict]

    def print_cache_state(self):
        print("Cache State:")
        print("Key-Value:", self.key_value)
        print("Key-Frequency:", dict(self.key_freq))
        print("Frequency-Keys:", dict(self.freq_keys))
        print("Minimum Frequency:", self.min_freq)
        print()

lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # Output: 1
lfu.put(3, 3)
print(lfu.get(2))  # Output: -1
print(lfu.get(3))  # Output: 3
lfu.put(4, 4)
print(lfu.get(1))  # Output: -1
print(lfu.get(3))  # Output: 3
print(lfu.get(4))  # Output: 4