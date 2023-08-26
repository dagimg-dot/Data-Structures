from DataStructures import DataStructures


class LinkedList(DataStructures):
    def __init__(self):
        # This means we have an empty linked list at the start because the head is pointing to nothing
        super().__init__()

    def append(self, val):
        self._addNodeAtEnd(val=val)

    def index(self, val):
        pos = 0
        head = self.head
        if head == None:
            raise ValueError

        while head != None and head.val != val:
            pos += 1
            head = head.next

        if pos == self.size():
            raise ValueError

        return pos

    def get(self, idx):
        count = 0
        head = self.head
        while head != None and count != idx:
            head = head.next
            count += 1
        if count == self.size():
            raise IndexError

        return head.val

    def insert(self, pos, val):
        if pos == 0:
            self._addNodeAtFirst(val=val)
        else:
            value = self.get(pos)
            self._addNodeAtMiddle(pos=value, val=val)

    def clear(self):
        self.head = None

    def size(self):
        head = self.head
        count = 0
        while head != None:
            head = head.next
            count += 1

        return count

    def reverse(self):
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
