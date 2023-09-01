class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def display(self) -> None:
        # TODO: I have to know what "Print the values to a stream" means related to the terminal
        """
        Print the values to a stream
        """
        head = self.head
        if head == None:  # If the head is None then the list is empty
            print("[]")
        else:
            print("[", end='')
            while head != None:  # Loop until the list is over, we know its over when the last node's next is None
                print(head.val, end=', ') if head.next != None else print(
                    head.val, end='')
                head = head.next
            print("]", end='')
            print()

    def _find(self, value: any) -> ListNode:
        head = self.head
        if head == None:  # If the list is empty return None
            return None
        else:
            while head != None and head.val != value:  # Loop until the value is found or the list is over
                head = head.next

        found = head  # This might be the node with the wanted value or None
        return found  # Whenever we use this method we have to handle the error correctly by checking if its a node or None

    def _addNodeAtFirst(self, value: any) -> None:
        new_node = ListNode(val=value)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            head = self.head
            self.head = new_node
            self.tail = head
            self.head.next = head
            head.prev = self.head

    def _addNodeAtEnd(self, value: any) -> None:
        new_node = ListNode(val=value)

        head = self.head
        if head == None:
            self.head = self.tail = new_node
        else:
            tail = self.tail
            tail.next = new_node
            new_node.prev = tail
            self.tail = new_node
