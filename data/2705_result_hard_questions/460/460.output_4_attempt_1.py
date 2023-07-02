# @lc app=leetcode id=460 lang=python3
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(None, None)  # dummy head node
        self.tail = ListNode(None, None)  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

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
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_dll = {}

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.update_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.update_node(node)
        else:
            if self.size == self.capacity:
                dll = self.freq_to_dll[self.min_freq]
                node_to_remove = dll.head.next
                dll.remove_node(node_to_remove)
                del self.key_to_node[node_to_remove.key]
                self.size -= 1

            new_node = ListNode(key, value)
            self.key_to_node[key] = new_node
            dll = self.freq_to_dll.get(1, DoublyLinkedList())
            dll.insert_after(dll.head, new_node)
            self.freq_to_dll[1] = dll
            self.min_freq = 1
            self.size += 1

    def update_node(self, node):
        freq = node.freq
        dll = self.freq_to_dll[freq]
        dll.remove_node(node)

        if dll.is_empty() and freq == self.min_freq:
            self.min_freq += 1

        node.freq += 1
        new_dll = self.freq_to_dll.get(node.freq, DoublyLinkedList())
        new_dll.insert_after(new_dll.head, node)
        self.freq_to_dll[node.freq] = new_dll

        self.freq_to_dll[freq] = dll