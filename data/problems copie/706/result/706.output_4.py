# @lc app=leetcode id=706 lang=python3
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        if self.buckets[hash_value] is None:
            self.buckets[hash_value] = ListNode(key, value)
        else:
            curr = self.buckets[hash_value]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key):
        hash_value = self._hash(key)
        curr = self.buckets[hash_value]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key):
        hash_value = self._hash(key)
        curr = prev = self.buckets[hash_value]
        if not curr:
            return
        if curr.key == key:
            self.buckets[hash_value] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                curr, prev = curr.next, prev.next