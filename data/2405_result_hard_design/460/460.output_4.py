# @lc app=leetcode id=460 lang=python3
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, new_node):
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_dict = {}
        self.freq_dict = {}

    def get(self, key: int) -> int:
        if key not in self.node_dict:
            return -1

        node = self.node_dict[key]
        self.update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size == self.capacity:
                self.evict_least_frequent()

            new_node = ListNode(key, value)
            self.node_dict[key] = new_node
            self.freq_dict.setdefault(1, DoublyLinkedList())
            freq_list = self.freq_dict[1]
            freq_list.insert_after(freq_list.head, new_node)
            self.min_freq = 1
            self.size += 1

    def update_frequency(self, node):
        freq_list = self.freq_dict[node.freq]
        freq_list.remove_node(node)

        if freq_list.is_empty() and self.min_freq == node.freq:
            self.min_freq += 1

        node.freq += 1
        self.freq_dict.setdefault(node.freq, DoublyLinkedList())
        new_freq_list = self.freq_dict[node.freq]
        new_freq_list.insert_after(new_freq_list.head, node)

    def evict_least_frequent(self):
        min_freq_list = self.freq_dict[self.min_freq]
        node_to_evict = min_freq_list.tail.prev
        del self.node_dict[node_to_evict.key]
        min_freq_list.remove_node(node_to_evict)
        self.size -= 1