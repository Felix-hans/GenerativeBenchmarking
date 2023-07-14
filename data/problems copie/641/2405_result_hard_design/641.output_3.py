# @lc app=leetcode id=641 lang=python3
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: ListNode, new_node: ListNode):
        next_node = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)
        self._add_node(self.head, new_node)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value)
        self._add_node(self.tail.prev, new_node)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        front_node = self.head.next
        self._remove_node(front_node)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        last_node = self.tail.prev
        self._remove_node(last_node)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity