# @lc app=leetcode id=460 lang=python3
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}  # Stores key-value pairs
        self.key_to_freq = {}  # Stores key-frequency pairs
        self.freq_to_keys = {}  # Stores frequency-key pairs
        self.min_freq = 0  # Tracks the minimum frequency

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1

        self.freq_to_keys[freq].remove(key)

        if len(self.freq_to_keys[freq]) == 0 and freq == self.min_freq:
            self.min_freq += 1

        if freq + 1 not in self.freq_to_keys:
            self.freq_to_keys[freq + 1] = []
        self.freq_to_keys[freq + 1].append(key)

        return self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_value:
            self.key_to_value[key] = value
            self.get(key)
            return

        if len(self.key_to_value) >= self.capacity:
            evicted_key = self.freq_to_keys[self.min_freq][0]

            del self.key_to_value[evicted_key]
            del self.key_to_freq[evicted_key]
            self.freq_to_keys[self.min_freq].pop(0)

        self.key_to_value[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1] = self.freq_to_keys.get(1, [])
        self.freq_to_keys[1].append(key)

        self.min_freq = 1