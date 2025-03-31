class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkedList:
#     def __init__(self, value):
#         self.head = Node(value)
#
#     def append(self, value):
#         cur = self.head
#
#         while cur.next is not None:
#             cur = cur.next
#
#         cur.next = Node(value)
#
#     def print(self):
#         temp = self.head
#         while temp.next is not None:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print(temp.data)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


linked_list = LinkedList(5)
linked_list.append(3)
linked_list.append(2)
linked_list.append(7)
linked_list.print()
