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

    def add_node(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0  # minimum frequency seen so far
        self.node_map = {}  # dictionary to store key-node mappings
        self.freq_map = {}  # dictionary to store frequency-list mappings

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.update_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.update_node(node)
        else:
            if self.size >= self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                node_to_remove = min_freq_list.tail.prev
                self.remove_node(node_to_remove)
                del self.node_map[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.node_map[key] = new_node

            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size += 1

    def update_node(self, node):
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove_node(node)

        if freq == self.min_freq and freq_list.is_empty():
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_node(node)