# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def addNodeAtFirst(self):
        inp = input("Enter value: ")
        if self.head == None:
            temp = ListNode(inp)
            self.head = temp
            temp.next = None
        else:
            head = self.head
            self.head = ListNode(inp)
            self.head.next = head

    def display(self):
        temp = self.head
        if temp == None:
            print("End of list")
        else:
            while temp != None:
                print(temp.val, end=' ')
                temp = temp.next


def main(linkedList):
    print("\nChoose: \n")
    print("1. Create node at first")
    print("2. Display")
    choice = input("Your choice: ")
    if choice == '1':
        linkedList.addNodeAtFirst()
    elif choice == '2':
        linkedList.display()
    else:
        exit(0)
    
    # Call it again
    main(linkedList)


list = LinkedList()
main(list)
