class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None