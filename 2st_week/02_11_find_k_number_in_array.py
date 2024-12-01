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

    # def calc_len(self):
    #     count = 0
    #     cur_node = self.head
    #     while cur_node is not None:
    #         count += 1
    #         cur_node = cur_node.next
    #     return count
    #
    # def get_kth_node_from_last(self, k):
    #     target_index = self.calc_len() - k
    #     target_node = self.head
    #     for i in range(target_index):
    #         target_node = target_node.next
    #
    #     return target_node

    def get_kth_node_from_last(self, k):
        fast_node = self.head
        slow_node = self.head
        for i in range(k):
            fast_node = fast_node.next

        while fast_node is not None:
            fast_node = fast_node.next
            slow_node = slow_node.next

        return slow_node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
