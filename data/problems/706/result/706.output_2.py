# @lc app=leetcode id=706 lang=python3
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.bucket = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.bucket[index] is None:
            self.bucket[index] = ListNode(key, value)
        else:
            curr = self.bucket[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key):
        index = self._hash(key)
        curr = self.bucket[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key):
        index = self._hash(key)
        curr = prev = self.bucket[index]
        if not curr:
            return
        if curr.key == key:
            self.bucket[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    curr, prev = curr.next, prev.next