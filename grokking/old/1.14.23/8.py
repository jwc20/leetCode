class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head):
    prev, curr = None, head

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
