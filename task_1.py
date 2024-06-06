class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head_node = None

    def add_to_start(self, value):
        new_node = ListNode(value)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def add_to_end(self, value):
        new_node = ListNode(value)
        if not self.head_node:
            self.head_node = new_node
            return
        current_node = self.head_node
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def add_after(self, prev_node, value):
        if not prev_node:
            print("Попереднього вузла не існує.")
            return
        new_node = ListNode(value)
        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

    def remove_node(self, value):
        current_node = self.head_node
        if current_node and current_node.value == value:
            self.head_node = current_node.next_node
            return
        prev_node = None
        while current_node and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next_node
        if not current_node:
            return
        prev_node.next_node = current_node.next_node

    def find_node(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node
        return None

    def display(self):
        current_node = self.head_node
        if not current_node:
            print("Список порожній")
            return
        while current_node:
            print(current_node.value)
            current_node = current_node.next_node

    def reverse(self):
        previous_node = None
        current_node = self.head_node
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head_node = previous_node
        return self

    def insertion_sort(self):
        if not self.head_node or not self.head_node.next_node:
            return self
        sorted_list = SinglyLinkedList()
        current_node = self.head_node
        while current_node:
            next_node = current_node.next_node
            if not sorted_list.head_node or sorted_list.head_node.value >= current_node.value:
                current_node.next_node = sorted_list.head_node
                sorted_list.head_node = current_node
            else:
                prev_node = sorted_list.head_node
                while prev_node.next_node and prev_node.next_node.value < current_node.value:
                    prev_node = prev_node.next_node
                current_node.next_node = prev_node.next_node
                prev_node.next_node = current_node
            current_node = next_node
        self.head_node = sorted_list.head_node
        return self

    def merge_sort(self, node=None):
        if node is None:
            node = self.head_node
        if not node or not node.next_node:
            return node
        middle_node = self.find_middle(node)
        next_to_middle = middle_node.next_node
        middle_node.next_node = None
        left_half = self.merge_sort(node)
        right_half = self.merge_sort(next_to_middle)
        return self.merge_sorted_lists(left_half, right_half)

    def find_middle(self, node):
        if not node:
            return node
        slow = node
        fast = node
        while fast.next_node and fast.next_node.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node
        return slow

    def merge_sorted_lists(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.value < right.value:
            left.next_node = self.merge_sorted_lists(left.next_node, right)
            return left
        else:
            right.next_node = self.merge_sorted_lists(left, right.next_node)
            return right

    def start_merge_sort(self):
        self.head_node = self.merge_sort()
        return self

    def combine_sorted_lists(self, another_list):
        dummy_node = ListNode()
        tail = dummy_node
        l1, l2 = self.head_node, another_list.head_node
        while l1 and l2:
            if l1.value < l2.value:
                tail.next_node = l1
                l1 = l1.next_node
            else:
                tail.next_node = l2
                l2 = l2.next_node
            tail = tail.next_node
        tail.next_node = l1 if l1 else l2
        self.head_node = dummy_node.next_node
        return self


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    # Додавання на початок списку
    list1.add_to_start(13)
    list1.add_to_start(6)

    # Додавання в кінець списку
    list1.add_to_end(10)
    list1.add_to_end(15)
    list1.add_to_end(17)
    
    # Вивід списку
    print("Список: ")
    list1.display()

    print("\nРеверс: ")
    list1.reverse().display()

    print("\nCортування вставками: ")
    list1.insertion_sort().display()

    # Створення другого списку
    list2 = SinglyLinkedList()
    list2.add_to_end(30)
    list2.add_to_end(20)
    list2.add_to_end(13)
    list2.add_to_end(50)
    list2.add_to_end(45)

    print("\nДругий сортування злиттям:")
    list2.start_merge_sort().display()

    print("\nОб'єднаний в один:")
    list1.combine_sorted_lists(list2).display()
