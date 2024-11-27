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

    def get_length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def get_node(self, index):
        cur_index = 0
        cur = self.head
        while cur_index < index:
            if cur.next is None:
                print("인덱스 범위를 벗어납니다.")
                return
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        length = self.get_length()

        if index < 0 or index > length:
            print("인덱스 범위를 벗어납니다.")
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == length:
            self.append(value)
        else:
            cur = self.get_node(index - 1)
            new_node.next = cur.next
            cur.next = new_node

    # def add_node(self, index, data):
    #     new_node = Node(data)
    #     if index == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         cur_index = 0
    #         cur = self.head
    #
    #         while cur_index < index - 1:
    #             if cur.next is None:
    #                 raise IndexError("인덱스 범위를 초과하였습니다.")
    #             cur = cur.next
    #             cur_index += 1
    #
    #         new_node.next = cur.next
    #         cur.next = new_node
    #     return new_node

    # def add_node(self, index, value):
    #     new_node = Node(value)
    #
    #     if index == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:
    #         prev_node = self.get_node(index - 1)
    #
    #         if prev_node.next is None:
    #             print("인덱스 범위를 벗어납니다.")
    #             return
    #         else:
    #             next_node = prev_node.next
    #
    #         prev_node.next = new_node
    #         new_node.next = next_node



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
linked_list.add_node(8, 133)
linked_list.print_all()
linked_list.add_node(9, 42)
linked_list.print_all()
