# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None  # This means we have an empty linked list at the start because the head is pointing to nothing

    def addNodeAtFirst(self):
        # Accept the value and create the node
        inp = input("Enter value: ")
        temp = ListNode(inp)

        # This checks if the linked list is empty or there are nodes
        if self.head == None:
            self.head = temp  # Make the new node the head of the linked list
            temp.next = None  # Make the next of the new node point to nothing
        else:
            # This means there are already other nodes in the linked lilst
            head = self.head
            self.head = temp  # Make the new node the head node
            self.head.next = head  # Make the previous node next to the new node

    def addNodeAtEnd(self):
        # Accept and create the new node
        inp = input("Enter value: ")
        temp = ListNode(inp)
        temp.next = None  # Make the next of the new node nothing

        # This checks if the linked list has already other nodes
        if self.head == None:
            self.head = temp
        else:
            head = self.head
            # Loop until you find the last node, this can be done by running a while loop
            # until you find that the next of the lase node is nothing
            while head.next != None:
                head = head.next

            end = head  # Name the last node 'end' for clarity
            end.next = temp  # Make the new node the last node

    def addNodeAtMiddle(self):
        place = input(
            "Enter after what node value you want insert the new node : ")
        found = self.find(val=place)
        while found == None:
            place = input("Not found, Enter again : ")
            found = self.find(val=place)

        inp = input("Enter the value: ")
        temp = ListNode(inp)

        next_node = found.next
        found.next = temp
        temp.next = next_node

    def find(self, val):
        if self.head == None:
            return None
        else:
            head = self.head
            while head != None and head.val != val:
                head = head.next

        found = head
        return found

    def display(self):
        head = self.head
        if head == None:
            print("End of list")
        else:
            while head != None:
                print(head.val, end=' ')
                head = head.next


def main(linkedList):
    print("\nChoose: \n")
    print("'d' For Display")
    print("1. Create node at first")
    print("2. Create node at the middle")
    print("3. Create node at end")
    choice = input("Your choice: ")
    if choice == 'd':
        linkedList.display()
    elif choice == '1':
        linkedList.addNodeAtFirst()
    elif choice == '2':
        linkedList.addNodeAtMiddle()
    elif choice == '3':
        linkedList.addNodeAtEnd()
    else:
        exit(0)

    # Call it again
    main(linkedList)


list = LinkedList()
main(list)
