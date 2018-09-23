class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circular_link_list:
    def __init__(self):
        self.head = None

    # insert at end
    def push(self, val):
        new_node = Node(val)
        ptr = self.head
        new_node.next = self.head

        if ptr is not None:
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_node
        else:
            new_node.next = new_node
            self.head = new_node

    # Insert at beginning
    def add_begin(self, val):
        new_node = Node(val)
        ptr = self.head
        new_node.next = self.head

        if ptr is not None:
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node

    def print_list(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print("%d" % temp.data),
                temp = temp.next
                if (temp == self.head):
                    break

  
    


# Main
def main():
    llist = circular_link_list()
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.add_begin(1)
    llist.push(5)
    llist.push(4)


if __name__ == '__main__':
    main()
