# @lc app=leetcode id=460 lang=python3
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # dummy head
        self.tail = Node(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.head.next == self.tail

    def get_least_recently_used_node(self):
        if self.is_empty():
            return None
        return self.head.next

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key-value pairs
        self.freq = {}  # frequency of each key
        self.freq_keys = {}  # keys with the same frequency
        self.min_freq = 0  # minimum frequency
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.update_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_node(node)
        else:
            if self.size == self.capacity:
                self.remove_least_frequently_used_key()

            node = Node(key, value)
            self.cache[key] = node
            self.update_node(node)
            self.size += 1

    def update_node(self, node):
        freq = node.freq

        if freq in self.freq_keys:
            self.freq_keys[freq].remove_node(node)
            if self.freq_keys[freq].is_empty():
                if freq == self.min_freq:
                    self.min_freq += 1
                del self.freq_keys[freq]

        freq += 1
        node.freq = freq

        if freq not in self.freq_keys:
            self.freq_keys[freq] = DoublyLinkedList()
        self.freq_keys[freq].add_node(node)
        self.freq[node.key] = freq

    def remove_least_frequently_used_key(self):
        if self.min_freq in self.freq_keys:
            node =