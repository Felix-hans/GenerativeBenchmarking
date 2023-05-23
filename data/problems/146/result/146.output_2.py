# @lc app=leetcode id=146 lang=python3
class LRUCacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = LRUCacheNode(None, None)  # Dummy head node
        self.tail = LRUCacheNode(None, None)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)  # Move the accessed node to the front
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value  # Update the value of an existing key
            self._move_to_front(node)  # Move the updated node to the front
        else:
            if len(self.cache) >= self.capacity:
                self._evict_lru_node()  # Evict the least recently used node
            new_node = LRUCacheNode(key, value)
            self._add_node(new_node)  # Add the new node to the cache
            self.cache[key] = new_node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _evict_lru_node(self):
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]