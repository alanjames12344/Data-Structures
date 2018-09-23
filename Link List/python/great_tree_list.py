import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    # Constructor for empty doubled linked list
    def __init__(self):
        self.head = None

    # INsert a new node at the beginning of the list
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert after
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous Node cannot be Null")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    # Insert at last
    def push(self,data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        else:
            last = self.head
            while last.next is not None:
                last = last.next

            last.next = new_node
            new_node.prev = last
    
    # Print the list
    def __str__(self):
        node = self.head
        # print ("\nTraversal in forward direction")
        while(node is not None):
            print (node.data , end=" ")
            # last = node
            node = node.next
 
        # print ("\nTraversal in reverse direction")
        # while(last is not None):
        #     print (" % d" %(last.data))
        #     last = last.prev
        
        return ""

    # Reverse a list
    def reverse(self):
        temp = None
        curr = self.head
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp is not None:
           self.head = temp.prev


    # Delete a node
    def __delitem__(self,val):
        temp = self.head
        while temp.data != val and temp.next is not None:
            temp = temp.next
        
        if temp.next is None:
            print("Item not found")
        else:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next

        gc.collect()
        