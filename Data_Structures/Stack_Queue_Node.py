class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        result = self.top.value
        self.top = self.top.next
        return result

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def print_stack(self):
        current = self.top
        print("Top ->", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next 
        print("None")

# Test pour Stack
stack = Stack()
print("Stack after pushing 1, 2, 3:")
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()

print("Peeking top:", stack.peek())
stack.print_stack()

print("Popping top:")
stack.pop()
stack.print_stack()

print("Popping top:")
stack.pop()
stack.print_stack()

print("Is stack empty?", stack.is_empty())


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        result = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return result

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.value
    
    def print_queue(self):
        current = self.front
        print("Front ->", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("Rear")

# Test pour Queue
queue = Queue()
print("Queue after enqueuing 1, 2, 3:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()

print("Peeking front:", queue.peek())
queue.print_queue()

print("Dequeuing front:")
queue.dequeue()
queue.print_queue()

print("Dequeuing front:")
queue.dequeue()
queue.print_queue()

print("Is queue empty?", queue.is_empty())

