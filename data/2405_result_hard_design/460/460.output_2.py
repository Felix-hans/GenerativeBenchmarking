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
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_node_map = {}
        self.freq_list_map = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self._update_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self._update_node(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_list_map[self.min_freq]
                node_to_remove = min_freq_list.head.next
                min_freq_list.remove_node(node_to_remove)
                del self.key_node_map[node_to_remove.key]
                self.size -= 1

            new_node = ListNode(key, value)
            self.key_node_map[key] = new_node
            freq_list = self.freq_list_map[1]
            freq_list.insert_after(freq_list.head, new_node)
            self.min_freq = 1
            self.size += 1

    def _update_node(self, node):
        freq = node.freq
        freq_list = self.freq_list_map[freq]
        freq_list.remove_node(node)

        if freq == self.min_freq and freq_list.is_empty():
            self.min_freq += 1

        node.freq += 1
        new_freq_list = self.freq_list_map[node.freq]
        new_freq_list.insert_after(new_freq_list.head, node)