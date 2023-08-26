from DataStructures import DataStructures


class LinkedList(DataStructures):
    def __init__(self):
        # This means we have an empty linked list at the start because the head is pointing to nothing
        super().__init__()

    def append(self, value: object) -> None:
        """
        Append on object to the end of the LinkedList\n
        Usage: \n
        list = LinkedList \n
        list.append(26)
        """
        self._addNodeAtEnd(val=value)

    def index(self, value: object) -> int:
        """
        Return first index of value\n\n
        Raises ValueError if the value is not present
        """
        pos = 0
        head = self.head
        if head == None:
            raise ValueError

        while head != None and head.val != value:
            pos += 1
            head = head.next

        if pos == self.size():
            raise ValueError

        return pos

    def get(self, index: int) -> any:
        """
        Return the value found in the index\n\n
        Raises IndexError if index not found
        """
        count = 0
        head = self.head
        while head != None and count != index:
            head = head.next
            count += 1
        if count == self.size():
            raise IndexError

        return head.val

    def insert(self, index: int, value: object) -> None:
        """
        Insert object after index\n\n
        Raises IndexError if index not found
        """
        if index == 0:
            self._addNodeAtFirst(val=value)
        else:
            value = self.get(index)
            self._addNodeAtMiddle(pos=value, val=value)

    def clear(self) -> None:
        """
        Clear the LinkedList
        """
        self.head = None

    def size(self) -> int:
        """
        Return the size the LinkedList
        """
        head = self.head
        count = 0
        while head != None:
            head = head.next
            count += 1

        return count

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
