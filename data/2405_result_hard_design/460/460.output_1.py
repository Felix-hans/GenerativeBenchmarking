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
        self.head = Node(None, None)  # Dummy head node
        self.tail = Node(None, None)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}  # Key to Node mapping
        self.freq_to_dll = {}  # Frequency to DoublyLinkedList mapping

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size == self.capacity:
                self.evict_least_frequent()

            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.size += 1

            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()

            dll = self.freq_to_dll[1]
            dll.insert_after(dll.head, new_node)
            self.min_freq = 1

    def update_frequency(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove(node)

        if dll.is_empty() and freq == self.min_freq:
            self.min_freq += 1
            del self.freq_to_dll[freq]

        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_dll:
            self.freq_to_dll[new_freq] = DoublyLinkedList()

        new_dll = self.freq_to_dll[new_freq]
        new_dll.insert_after(new_dll.head, node)

    def evict_least_frequent(self):
        dll = self.freq_to_dll[self.min_freq]
        node_to_evict = dll.tail.prev
        del self.key_to_node[node_to_evict.key]
        dll.remove(node_to_evict)
        self.size -= 1