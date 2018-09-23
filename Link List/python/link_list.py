# Basic Structure


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class link_list:
    def __init__(self):
        self.head = None

# Insertion

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The previous node must in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If not empty
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("\r")

# Deletion
    # Remove the element at first occurance
    def remove(self, key):
        temp = self.head
        # If head holds the key
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        # Else
        while temp is not None:
            if temp.next.data == key:
                prev = temp
                prev.next = temp.next.next
                temp.next = None
                return
            temp = temp.next
        # If value not found
        if temp == None:
            print("Value not found")
            return

    def remove_at(self, position):
        temp = self.head
        if(temp == None):
            print("List is empty")
            return
        while position > 0:
            temp = temp.next
            position -= 1
        prev = temp
        prev.next = temp.next.next

# Find Length
    # Iterative Way
    def length(self):
        count = 0
        temp = self.head
        while(temp != None):
            count += 1
            temp = temp.next

        return count
    # recursive way

    def length_recursive(self, list):
        if list == None:
            return 0
        else:
            return 1 + self.length_recursive(list.next)

# Swap nodes
    def swap_nodes(self, x, y):
        # If x and y are same then return none
        if x == y:
            return
        
        # Search for X
        prevX = None
        currX = self.head

        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        
        # Search for Y
        prevY = None
        currY = self.head

        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        
        if currX == None or currY == None:
            return
        
        # If X is not the head
        if prevX != None:
            prevX.next = currY
        else: # make the y new head
            self.head = currY

        # If Y is not the head
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        # Swap the next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

# Reverse List
    # Iterative method
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

# Add two lists
    def Add(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both lists exist
        while first is not None or second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            fsum = carry + fdata + sdata

            # update carry
            carry = 1 if fsum >= 10 else 0
            fsum = fsum if fsum <10 else fsum % 10

            # Create a node with sum as data
            temp = Node(fsum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            # Move first and second pointer to the next node
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

# Rotate a link list
    def rotate(self,k):
        if k==0:
            return True

        curr = self.head

        count=1
        while count < k and curr.next != None:
            curr = curr.next
            count += 1

        if curr == None:
            return False
        
        kthnode = curr

        while curr.next != None:
            curr = curr.next

        curr.next = self.head

        self.head = kthnode.next
        kthnode.next = None

        
# Merge two link list
def merge_lists(head1, head2):
    temp = None
    # If one head is null
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    # Insert in temorary node in sorted order
    if head1.data <= head2.data:
        temp = head1
        temp.next = merge_lists( head1.next, head2)
    else:
        temp = head2
        temp.next = merge_lists( head1, head2.next)
    
    # return temp
    return temp
# Main
def main():
    llist = link_list()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.append(50)
    llist.print_list()
    llist.rotate(2)
    llist.print_list()

if __name__ == '__main__':
    main()
