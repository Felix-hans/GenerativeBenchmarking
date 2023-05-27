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
        self.head = Node(None, None)  # dummy head node
        self.tail = Node(None, None)  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_least_frequent(self):
        if self.head.next == self.tail:
            return None
        least_freq_node = self.head.next
        self.remove(least_freq_node)
        return least_freq_node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key: node
        self.freq_map = {}  # freq: doubly linked list

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.update_frequency(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size == self.capacity:
                self.evict_least_frequent()
            node = Node(key, value)
            self.cache[key] = node
            self.freq_map.setdefault(1, DoublyLinkedList()).append(node)
            self.size += 1

    def update_frequency(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)
        if len(self.freq_map[freq]) == 0:
            del self.freq_map[freq]
        node.freq += 1
        self.freq_map.setdefault(node.freq, DoublyLinkedList()).append(node)

    def evict_least_frequent(self):
        least_freq_list = self.freq_map[min(self.freq_map)]
        least_freq_node = least_freq_list.pop_least_frequent()
        del self.cache[least_freq_node.key]
        self.size -= 1