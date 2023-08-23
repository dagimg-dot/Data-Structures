# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None # This means we have an empty linked list at the start because the head is pointing to nothing

    def addNodeAtFirst(self):
        # Accept the value and create the node
        inp = input("Enter value: ")
        temp = ListNode(inp)

        # This checks if the linked list is empty or there are nodes
        if self.head == None:
            self.head = temp # Make the new node the head of the linked list
            temp.next = None # Make the next of the new node point to nothing
        else:
            # This means there are already other nodes in the linked lilst
            head = self.head
            self.head = temp # Make the new node the head node
            self.head.next = head # Make the previous node next to the new node

    def addNodeAtEnd(self):
        # Accept and create the new node
        inp = input("Enter value: ")
        temp = ListNode(inp)
        temp.next = None # Make the next of the new node nothing

        # This checks if the linked list has already other nodes
        if self.head == None:
            self.head = temp
        else:
            head = self.head
            # Loop until you find the last node, this can be done by running a while loop 
            # until you find that the next of the lase node is nothing
            while head.next != None:
                head = head.next

            head.next = temp # Make the new node the last node

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
    print("1. Create node at first")
    print("2. Display")
    print("3. Creat node at end")
    choice = input("Your choice: ")
    if choice == '1':
        linkedList.addNodeAtFirst()
    elif choice == '2':
        linkedList.display()
    elif choice == '3':
        linkedList.addNodeAtEnd()
    else:
        exit(0)

    # Call it again
    main(linkedList)


list = LinkedList()
main(list)
