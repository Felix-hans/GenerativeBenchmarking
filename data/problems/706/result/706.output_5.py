# @lc app=leetcode id=706 lang=python3
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        if not self.buckets[hash_key]:
            self.buckets[hash_key] = ListNode(key, value)
        else:
            curr = self.buckets[hash_key]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        curr = self.buckets[hash_key]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        curr = prev = self.buckets[hash_key]
        if not curr:
            return
        if curr.key == key:
            self.buckets[hash_key] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                curr, prev = curr.next, prev.next