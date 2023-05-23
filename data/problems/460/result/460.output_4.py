# @lc app=leetcode id=460 lang=python3
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {}  # Stores key-value pairs
        self.freq_map = {}  # Stores frequency nodes

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, freq_node = self.cache[key]
        self.update_frequency(key, freq_node)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            freq_node = self.cache[key][1]
            self.cache[key] = (value, freq_node)
            self.update_frequency(key, freq_node)
        else:
            if self.size == self.capacity:
                self.evict()

            freq_node = self.freq_map.get(1, None)
            if freq_node is None:
                freq_node = Node(1)
                freq_node.next = self.freq_map.get(2, None)
                if freq_node.next is not None:
                    freq_node.next.prev = freq_node
                self.freq_map[1] = freq_node

            freq_node.keys.add(key)
            self.cache[key] = (value, freq_node)
            self.min_freq = 1
            self.size += 1

    def update_frequency(self, key, freq_node):
        freq_node.keys.remove(key)

        if freq_node.next is None:
            next_freq = freq_node.freq + 1
            next_freq_node = Node(next_freq)
            next_freq_node.prev = freq_node
            freq_node.next = next_freq_node
            if next_freq_node.next is not None:
                next_freq_node.next.prev = next_freq_node
            self.freq_map[next_freq] = next_freq_node
        else:
            next_freq = freq_node.next.freq

        next_freq_node = freq_node.next
        next_freq_node.keys.add(key)

        if len(freq_node.keys) == 0:
            if freq_node.freq == self.min_freq:
                self.min_freq = next_freq
            if freq_node.prev is not None:
                freq_node.prev.next = next_freq_node
            if next_freq_node.next is not None:
                next_freq_node.next.prev = freq_node

            del self.freq_map[freq_node.freq]

    def evict(self):
        freq_node = self.freq_map[self.min_freq]
        key_to_evict = next(iter(freq_node.keys))
        freq_node.keys.remove(key_to_evict)
        del self.cache[key_to_evict]
        self.size -= 1

        if len(freq_node.keys) == 0:
            if freq_node.prev is not None:
                freq_node.prev.next = freq_node.next
            if freq_node.next is not None:
                freq_node.next.prev = freq_node.prev
            del self.freq_map[freq_node.freq]