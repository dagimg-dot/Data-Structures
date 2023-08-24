# Definition for singly-linked list.
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None  # This means we have an empty linked list at the start because the head is pointing to nothing

    def addNodeAtFirst(self):
        # Accept the value and create the node
        inp = input("Enter value: ")
        new_node = ListNode(val=inp)

        # This checks if the linked list is empty or there are nodes
        if self.head == None:
            self.head = new_node  # Make the new node the head of the linked list
            new_node.next = None  # Make the next of the new node point to nothing
        else:
            # This means there are already other nodes in the linked lilst
            head = self.head
            self.head = new_node  # Make the new node the head node
            self.head.next = head  # Make the previous node next to the new node

    def addNodeAtEnd(self):
        # Accept and create the new node
        inp = input("Enter value: ")
        new_node = ListNode(val=inp)
        new_node.next = None  # Make the next of the new node nothing

        head = self.head
        # This checks if the linked list has already other nodes
        if head == None:
            head = new_node
        else:
            # Loop until you find the last node, this can be done by running a while loop
            # until you find that the next of the lase node is nothing
            while head.next != None:
                head = head.next

            end = head  # Name the last node 'end' for clarity
            end.next = new_node  # Make the new node the last node

    def addNodeAtMiddle(self):
        if self.head == None:  # Check if the list is empty then call add node at first method
            self.addNodeAtFirst()
        else:
            # Accept and find the node with the value
            place = input(
                "Enter after what node value you want insert the new node : ")
            found = self.find(val=place)
            while found == None:  # If it's not found ask again
                place = input("Not found, Enter again : ")
                found = self.find(val=place)

            # Accept the value and create a new node
            inp = input("Enter the value: ")
            new_node = ListNode(val=inp)

            next_node = found.next  # Save the node next to the found node for later
            found.next = new_node  # Make the next of the found node the new created node
            new_node.next = next_node  # Make the next of the new node what we saved earlier

    def deleteNodeAtFirst(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def deleteNodeAtEnd(self):
        head = self.head
        if head == None:
            return
        elif head.next == None:
            self.head = None
        else:
            while head.next.next != None:
                head = head.next

            head.next = None

    def find(self, val):
        head = self.head
        if head == None:  # If the list is empty return None
            return None
        else:
            while head != None and head.val != val:  # Loop until the value is found or the list is over
                head = head.next

        found = head  # This might be the node with the wanted value or None
        return found  # Whenever we use this method we have to handle the error correctly by checking if its a node or None

    def display(self):
        head = self.head
        if head == None:  # If the head is None then the list is empty
            print("End of list")
        else:
            while head != None:  # Loop until the list is over, we know its over when the last node's next is None
                print(head.val, end=' ')
                head = head.next


def main(linkedList: LinkedList):
    print("\nChoose: \n")
    print("'d' For Display")
    print("1. Create node at first")
    print("2. Create node at the middle")
    print("3. Create node at the end")
    print("4. Delete node at first")
    print("5. Delete node at the end")
    choice = input("Your choice: ")
    if choice == 'd':
        linkedList.display()
    elif choice == '1':
        linkedList.addNodeAtFirst()
    elif choice == '2':
        linkedList.addNodeAtMiddle()
    elif choice == '3':
        linkedList.addNodeAtEnd()
    elif choice == '4':
        linkedList.deleteNodeAtFirst()
    elif choice == '5':
        linkedList.deleteNodeAtEnd()
    else:
        exit(0)

    # Call it again
    main(linkedList)


list = LinkedList()
if __name__ == '__main__':
    main(list)
