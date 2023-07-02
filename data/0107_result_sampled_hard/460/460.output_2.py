# @lc app=leetcode id=460 lang=python3
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_map = {}
        self.freq_map = defaultdict(LinkedList)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self._update_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update_node(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                evict_node = min_freq_list.head.next
                del self.node_map[evict_node.key]
                min_freq_list.remove(evict_node)
                self.size -= 1
            
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].append(new_node)
            self.min_freq = 1
            self.size += 1

    def _update_node(self, node):
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove(node)

        if freq == self.min_freq and freq_list.head.next == freq_list.tail:
            self.min_freq += 1
        
        node.freq += 1
        new_freq = node.freq
        new_freq_list = self.freq_map[new_freq]
        new_freq_list.append(node)