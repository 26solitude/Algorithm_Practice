class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return new_node.data

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "Stack is Empty"

    def is_empty(self):
        return self.head is None


stack = Stack()

# Test is_empty
print("스택이 비었는가? ", stack.is_empty())  # True

# Test push
stack.push(10)
stack.push(20)
stack.push(30)

# Test peek
print("스택의 최상위 요소: ", stack.peek())  # 30

# Test pop
print("팝: ", stack.pop())  # 30
print("팝: ", stack.pop())  # 20

# Test is_empty
print("스택이 비었는가? ", stack.is_empty())  # False

# Test pop until empty
print("팝: ", stack.pop())  # 10
print("팝: ", stack.pop())  # Stack is Empty
