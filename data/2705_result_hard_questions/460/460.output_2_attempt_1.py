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

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self):
        if self.tail.prev != self.head:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node
        else:
            return None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_dll = {}

    def update_frequency(self, node):
        freq = node.freq
        self.freq_to_dll[freq].remove_node(node)

        if freq == self.min_freq and not self.freq_to_dll[freq].head.next:
            self.min_freq += 1

        node.freq += 1
        freq = node.freq
        if freq not in self.freq_to_dll:
            self.freq_to_dll[freq] = DoublyLinkedList()
        self.freq_to_dll[freq].add_node(node)

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.update_frequency(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size == self.capacity:
                min_freq_dll = self.freq_to_dll[self.min_freq]
                evicted_node = min_freq_dll.pop_tail()
                if evicted_node:
                    del self.key_to_node[evicted_node.key]
                    self.size -= 1

            new_node = ListNode(key, value)
            self.key_to_node[key] = new_node

            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].add_node(new_node)

            self.min_freq = 1
            self.size += 1