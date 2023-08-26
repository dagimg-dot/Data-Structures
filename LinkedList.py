from DataStructures import DataStructures


class LinkedList(DataStructures):
    """ 
    LinkedList implementation 
    """

    def __init__(self):
        # This means we have an empty linked list at the start because the head is pointing to nothing
        super().__init__()

    def append(self, value: any) -> None:
        """
        Append value to the end of the LinkedList
        """
        self._addNodeAtEnd(val=value)

    def index(self, value: any) -> int:
        """
        Return first index of value\n\n
        Raises ValueError if the value is not present
        """
        pos = 0
        head = self.head
        if head == None:
            raise ValueError("value not found")

        while head != None and head.val != value:
            pos += 1
            head = head.next

        if pos == self.size():
            raise ValueError("value not found")

        return pos

    def get(self, index: int) -> any:
        """
        Return the value found in the index\n\n
        Raises IndexError if index not found
        """
        node = self._getByIndex(idx=index)

        return node.val

    def insert(self, index: int, value: any) -> None:
        """
        Insert object after index\n\n
        Raises IndexError if index not found
        """
        if self.size() == 0:
            self._addNodeAtFirst(val=value)
        else:
            node = self._getByIndex(index)
            self._addNodeAtMiddle(pos=node.val, val=value)

    def reverse(self) -> None:
        """
        Reverse the LinkedList
        """
        head = self.head
        if head == None or head.next == None:
            return
        else:
            temp = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node

            self.head = temp

    def remove(self, value: any) -> None:
        """
        Remove first occurence of value\n\n
        Raises ValueError if value is not present
        """
        self._deleteNodeAtMiddle(val=value)

    def count(self, value: any) -> int:
        """
        Return number of occurences of value
        """
        count = 0
        head = self.head
        while head != None:
            if head.val == value:
                count += 1
            head = head.next

        return count
