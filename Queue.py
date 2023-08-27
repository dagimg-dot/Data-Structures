from typing import List
from DataStructures import DataStructures


class Queue(DataStructures):
    """
    Queue Implementation
    """

    def __init__(self):
        super().__init__()

    def enqueue(self, value: any) -> None:
        """
        Add value to the start of the queue
        """
        self._addNodeAtFirst(value)

    def dequeue(self) -> any:
        """
        Delete value at the end of the queue
        """
        size = self.size()
        if size == 0:
            raise IndexError("dequeue from empty queue")

        last_node = self._getByIndex(size - 1)
        value = last_node.val
        self._deleteNodeAtEnd()
        return value

    def fromlist(self, python_list: List) -> None:
        """
        Convert a python built-in list to a Queue
        """
        for value in python_list:
            self._addNodeAtEnd(value)
