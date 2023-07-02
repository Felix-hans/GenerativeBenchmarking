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

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get_least_frequent_node(self):
        if self.head.next == self.tail:
            return None
        return self.head.next


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key: Node
        self.freq_map = {}  # frequency: DoublyLinkedList
        self.min_freq = 0

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
                self.evict_least_frequent_node()
            node = Node(key, value)
            self.cache[key] = node
            self.insert_node(node)
            self.size += 1

    def update_node(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)

        if freq == self.min_freq and not self.freq_map[freq].head.next:
            self.min_freq += 1

        node.freq += 1
        freq += 1
        if freq not in self.freq_map:
            self.freq_map[freq] = DoublyLinkedList()
        self.freq_map[freq].insert_after(self.freq_map[freq - 1].tail.prev, node)

    def insert_node(self, node):
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        self.freq_map[1].insert_after(self.freq_map[0].tail.prev, node)
        self.min_freq = 1

    def evict_least_frequent_node(self):
        least_freq_list = self.freq_map[self.min_freq]
        node_to_evict = least_freq_list.get_least_frequent_node()
        least_freq_list.remove_node(node_to_evict)
        del self.cache[node_to_evict.key]
        self.size -= 1