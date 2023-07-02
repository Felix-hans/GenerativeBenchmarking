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

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

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
        self.key_to_node = {}  # Dictionary to store key-node mapping
        self.freq_to_dll = {}  # Dictionary to store frequency-doubly linked list mapping

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.update(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.update(node)
        else:
            if self.size == self.capacity:
                dll = self.freq_to_dll[self.min_freq]
                node_to_remove = dll.tail.prev
                self.remove_node(node_to_remove)
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            dll = self.freq_to_dll.get(1, DoublyLinkedList())
            dll.insert(new_node)
            self.freq_to_dll[1] = dll
            self.min_freq = 1
            self.size += 1

    def update(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove(node)
        if dll.is_empty() and freq == self.min_freq:
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq
        new_dll = self.freq_to_dll.get(new_freq, DoublyLinkedList())
        new_dll.insert(node)
        self.freq_to_dll[new_freq] = new_dll

    def remove_node(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove(node)
        del self.key_to_node[node.key]
        self.size -= 1