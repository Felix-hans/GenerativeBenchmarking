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
        self.key_node_map = {}  # Key to Node mapping
        self.freq_list_map = {}  # Frequency to DoublyLinkedList mapping

    def get(self, key: int) -> int:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self.update_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self.update_node(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_list_map[self.min_freq]
                node_to_evict = min_freq_list.tail.prev
                del self.key_node_map[node_to_evict.key]
                min_freq_list.remove(node_to_evict)
                self.size -= 1

            new_node = Node(key, value)
            self.key_node_map[key] = new_node

            freq_list = self.freq_list_map.get(1, DoublyLinkedList())
            freq_list.insert_after(freq_list.head, new_node)
            self.freq_list_map[1] = freq_list

            self.min_freq = 1
            self.size += 1

    def update_node(self, node):
        freq = node.freq
        freq_list = self.freq_list_map[freq]
        freq_list.remove(node)

        if freq == self.min_freq and freq_list.is_empty():
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq

        new_freq_list = self.freq_list_map.get(new_freq, DoublyLinkedList())
        new_freq_list.insert_after(new_freq_list.head, node)
        self.freq_list_map[new_freq] = new_freq_list