from DataStructures import DataStructures


class Stack(DataStructures):
    def __init__(self):
        super().__init__()

    def push(self, value: any) -> None:
        """
        Push value to the top of the stack
        """
        self._addNodeAtEnd(val=value)

    def pop(self, index=-1) -> any:
        """
        Remove and return item at index (default last)\n\n
        Raises IndexError if Stack is empty or index is out of range
        """
        size = self.size()
        if size == 0:
            raise IndexError

        if index == -1 or index == size - 1:
            last_node = self._getByIndex(size - 1)
            value = last_node.val
            self._deleteNodeAtEnd()
            return value
        else:
            node = self._getByIndex(index)
            value = node.val
            self._deleteNodeAtMiddle(value)
            return value
