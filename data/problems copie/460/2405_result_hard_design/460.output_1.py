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
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last_node(self):
        if self.tail.prev != self.head:
            self.remove_node(self.tail.prev)
            return self.tail.prev

        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {}  # Stores key-node mapping
        self.freq_map = {}  # Stores frequency-doubly linked list mapping

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.update_node(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.update_node(node)
        else:
            if self.size >= self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                removed_node = min_freq_list.remove_last_node()
                del self.key_map[removed_node.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_map[key] = new_node

            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()

            freq_list = self.freq_map[1]
            freq_list.add_node(new_node)
            self.min_freq = 1
            self.size += 1

    def update_node(self, node):
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove_node(node)

        if freq == self.min_freq and freq_list.head.next == freq_list.tail:
            self.min_freq += 1

        node.freq += 1

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()

        new_freq_list = self.freq_map[node.freq]
        new_freq_list.add_node(node)


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # Output: 1
lfu.put(3, 3)
print(lfu.get(2))  # Output: -1
print(lfu.get(3))  # Output: 3
lfu.put(4, 4)
print(l