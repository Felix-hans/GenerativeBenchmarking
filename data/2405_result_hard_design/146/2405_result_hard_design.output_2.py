# @lc app=leetcode id=2405_result_hard_design lang=python3
class LRUCache:
    class ListNode:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.ListNode()
        self.tail = self.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict_least_recent()
            new_node = self.ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _evict_least_recent(self):
        node_to_remove = self.tail.prev
        self._remove_node(node_to_remove)
        del self.cache[node_to_remove.key]