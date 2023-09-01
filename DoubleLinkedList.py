class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None

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

    def _addNodeAtFirst(self, value: any) -> None:
        new_node = ListNode(val=value)

        if self.head == None:
            self.head = new_node
        else:
            head = self.head
            self.head = new_node
            self.head.next = head
            head.prev = self.head

    def _addNodeAtEnd(self, value: any) -> None:
        new_node = ListNode(val=value)

        head = self.head
        if head == None:
            self.head = new_node
        else:
            while head.next != None:
                head = head.next

            end = head
            end.next = new_node
            new_node.prev = end
