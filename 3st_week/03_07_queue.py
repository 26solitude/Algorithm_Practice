class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "queue is empty!"
        delete_node = self.head
        self.head = self.head.next

        return delete_node.data

    def peek(self):
        if self.is_empty():
            return "queue is empty!"
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
print(queue.peek())
queue.enqueue(1)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
