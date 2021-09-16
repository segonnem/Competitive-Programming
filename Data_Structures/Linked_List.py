class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()



class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append an item to the end of the list """
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        """ Prepend an item to the beginning of the list """
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """ Delete a node by value (key) """
        current = self.head
        while current:
            if current.data == key and current == self.head:
                # Case: node to be deleted is the head
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                    next_node = current.next
                    next_node.prev = None
                    self.head = next_node
                    current = None
                    return
            elif current.data == key:
                # Case: node to be deleted is not the head
                if current.next:
                    next_node = current.next
                    prev_node = current.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current = None
                    return
                else:
                    # Case: node to be deleted is the last node
                    prev_node = current.prev
                    prev_node.next = None
                    current = None
                    return
            current = current.next

    def search(self, key):
        """ Search the list for a node containing the key """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def insert_after(self, target, data):
        """ Insert a new node after the node containing 'target' """
        current = self.head
        while current:
            if current.data == target:
                new_node = DoubleNode(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def reverse(self):
        """ Reverse the linked list """
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def print_list(self):
        """ Print all elements in the list """
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


#Famous algorithm to find cycle
def has_cycle(head):
    tortoise = hare = head
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True
    return False



# Example Usage
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.prepend(0)
dllist.insert_after(1, 1.5)
dllist.delete(3)
dllist.reverse()
dllist.print_list()

cycle_list = LinkedList()
cycle_list.append(1)
cycle_list.append(2)
cycle_list.append(3)
node = cycle_list.head
while node.next:
    node = node.next
node.next = cycle_list.head  # creating a cycle
print("Has Cycle:", has_cycle(cycle_list.head))
