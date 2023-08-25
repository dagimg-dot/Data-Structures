class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None  # This means we have an empty linked list at the start because the head is pointing to nothing

    def append(self, val):
        self.__addNodeAtEnd(val=val)

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
        value = self.get(pos)
        self.__addNodeAtMiddle(pos=value, val=val)

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

    def display(self):
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

    def __find(self, val):
        head = self.head
        if head == None:  # If the list is empty return None
            return None
        else:
            while head != None and head.val != val:  # Loop until the value is found or the list is over
                head = head.next

        found = head  # This might be the node with the wanted value or None
        return found  # Whenever we use this method we have to handle the error correctly by checking if its a node or None

    def __addNodeAtFirst(self, val):
        new_node = ListNode(val=val)

        # This checks if the linked list is empty or there are nodes
        if self.head == None:
            self.head = new_node  # Make the new node the head of the linked list
            new_node.next = None  # Make the next of the new node point to nothing
        else:
            # This means there are already other nodes in the linked lilst
            head = self.head
            self.head = new_node  # Make the new node the head node
            self.head.next = head  # Make the previous node next to the new node

    def __addNodeAtEnd(self, val):
        new_node = ListNode(val=val)
        new_node.next = None  # Make the next of the new node nothing

        head = self.head
        # This checks if the linked list has already other nodes
        if head == None:
            self.head = new_node
        else:
            # Loop until you find the last node, this can be done by running a while loop
            # until you find that the next of the lase node is nothing
            while head.next != None:
                head = head.next

            end = head  # Name the last node 'end' for clarity
            end.next = new_node  # Make the new node the last node

    def __addNodeAtMiddle(self, pos, val):
        if self.head == None:  # Check if the list is empty then call add node at first method
            self.__addNodeAtFirst(val=val)
        else:
            found = self.__find(val=pos)
            if found == None:
                raise ValueError

            new_node = ListNode(val=val)

            next_node = found.next  # Save the node next to the found node for later
            found.next = new_node  # Make the next of the found node the new created node
            new_node.next = next_node  # Make the next of the new node what we saved earlier

    def __deleteNodeAtFirst(self):
        if self.head == None:  # Nothing to delete here because the list is empty
            return
        else:
            self.head = self.head.next  # Make the next of the head the head

    def __deleteNodeAtEnd(self):
        head = self.head
        if head == None:  # Nothing to delte here because the list is empty
            return
        elif head.next == None:  # Only one member is on the list, so make the head None
            self.head = None
        else:
            while head.next.next != None:  # Loop until the node that is before the last node is found
                head = head.next

            head.next = None  # Make the next of this node None

    def __deleteNodeAtMiddle(self):
        head = self.head
        if head == None:  # Nothing to delete because the list it empty
            return
        elif head.next == None:  # Only one member is no the list, so call the deleteAtFirst method
            self.head = None
        else:
            # Accept and find the node with the value
            place = input(
                "Enter the value of the node you want to delete : ")
            found = self.find(val=place)
            while found == None:  # If it's not found ask again
                place = input("Not found, Enter again : ")
                found = self.find(val=place)

            while head.next != found:  # Loop until you find the node before the node you want to delete
                head = head.next

            # Make the next of this node the next of the node you want to delete
            head.next = found.next
