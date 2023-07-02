# @lc app=leetcode id=460 lang=python3
class Node:
    def __init__(self, key=None, value=None, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

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
        self.key_map = {}
        self.freq_map = defaultdict(DoublyLinkedList)

    def update_frequency(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if self.min_freq == freq and self.freq_map[freq].is_empty():
            self.min_freq += 1

        node.freq += 1
        freq = node.freq
        self.freq_map[freq].append(node)

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.update_frequency(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.update_frequency(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                node_to_remove = min_freq_list.head.next
                min_freq_list.remove(node_to_remove)
                del self.key_map[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].append(new_node)
            self.min_freq = 1
            self.size += 1