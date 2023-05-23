# @lc app=leetcode id=146 lang=python3
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.key_order = []  # Maintain the order of keys based on their recent usage

    def get(self, key: int) -> int:
        if key in self.cache:
            self.key_order.remove(key)  # Remove the key from its current position
            self.key_order.append(key)  # Add the key to the end of the order list
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.key_order.remove(key)  # Remove the key from its current position
        elif len(self.cache) >= self.capacity:
            lru_key = self.key_order.pop(0)  # Remove the least recently used key
            del self.cache[lru_key]

        self.cache[key] = value
        self.key_order.append(key)  # Add the key to the end of the order list