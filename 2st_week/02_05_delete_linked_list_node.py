class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            cur_node = prev_node.next
            prev_node.next = cur_node.next
            cur_node.next = None


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(3)
linked_list.append(2)

linked_list.print_all()
linked_list.add_node(5, 13)
linked_list.print_all()
linked_list.add_node(2, 1)
linked_list.print_all()
linked_list.add_node(3, 4)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()
linked_list.delete_node(5)
linked_list.print_all()
linked_list.delete_node(2)
linked_list.print_all()
linked_list.delete_node(1)
linked_list.print_all()
