class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data} -> {self.next}"


def make_linked_list(count):

    head = Node(1)
    node = head

    for i in range(2, count):
        node.next = Node(i)
        node = node.next
    # print(head)
    return head


def push_front(value):

    new_node = Node(value)
    head = make_linked_list(4)
    new_node.next = head
    # print(new_node)
    return new_node


def push_back_node(value):

    new_node = Node(value)
    head = make_linked_list(4)
    node = head

    while node.next:
        node = node.next

    node.next = new_node

    return head


def length(head):

    cnt = 0

    while head:
        cnt += 1
        head = head.next
    
    return cnt


def insert_nth(head, index, data):

    if index == 0:
        return Node(data, head)

    if index > 0 and head:
        head.next = insert_nth(head.next, index-1, data)
        return head
    raise ValueError


def sorted_insert(head, data):
    
    if not head or head.data >= data:
        # new = Node(data)
        # new.next = head
        # return new
        return Node(data, head)
    else:
        head.next = sorted_insert(head.next, data)
        return head


def alternating_split(head):
    
    if not head or head.next == None:
        raise ValueError

    orig_a, orig_b = a, b = Node(), Node()

    while head:
        a.next = Node(head.data)
        print(f"a = {a}, a.next = {a.next}")

        a = a.next
        print(f"a = {a}")

        a, b = b, a
        print(f"a = {a}, b = {b}")

        head = head.next
        print('------------------------------------------------')
        
    print(orig_a.next, orig_b.next)

