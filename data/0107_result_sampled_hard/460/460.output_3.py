# @lc app=leetcode id=460 lang=python3
from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequency = {}
        self.freqKeys = defaultdict(list)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self._update_frequency(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            self._update_frequency(key)
        else:
            if len(self.cache) >= self.capacity:
                self._evict_least_frequent()
            self.cache[key] = value
            self.frequency[key] = 1
            self.freqKeys[1].append(key)
            self.minFreq = 1
    
    def _update_frequency(self, key: int) -> None:
        freq = self.frequency[key]
        self.frequency[key] += 1
        self.freqKeys[freq].remove(key)
        self.freqKeys[freq + 1].append(key)
        
        if not self.freqKeys[self.minFreq]:
            self.minFreq += 1
    
    def _evict_least_frequent(self) -> None:
        keys = self.freqKeys[self.minFreq]
        key_to_evict = keys.pop(0)
        del self.cache[key_to_evict]
        del self.frequency[key_to_evict]