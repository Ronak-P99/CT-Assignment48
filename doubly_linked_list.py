import time

# Node class
# Linked List Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def delete(self, data):
        current = self.head # The begininning of our linked list
        while current: # Chance that the data we're looking for doesn't exist
            if current.data == data: # Check current data to data passed in.
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                    return True
            current = current.next
        return False
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def traversal(self):
        print("Linked List elements:")
        for data in self:
            print(data, end=" -> ")
        print("None")

# Measure time for linked list operations
def linked_list_operations():
    linked_list = DoublyLinkedList()
    linked_list.append("Main Street") # O(1)
    linked_list.append("Broadway")
    linked_list.append("Park Avenue")
    linked_list.append("Elm Street")

    # Start measuring time for deletion
    start_time_delete = time.time()
    linked_list.delete("Broadway") # Head that will be an O(1). If a doubly linked list. Tail can be an O(1). Anything else will be an O(n)
    end_time_delete = time.time()
    delete_time = end_time_delete - start_time_delete

    # Start measuring time for traversal
    start_time_traversal = time.time()
    linked_list.traversal() # Looping through our entire list. O(n)
    end_time_traversal= time.time()
    traversal_time = end_time_traversal - start_time_traversal

    return delete_time, traversal_time

# Measure time for linked list operations
delete_time, traversal_time = linked_list_operations()
print("Time taken for deletion:", delete_time, "seconds")
print("Time taken for traversal:", traversal_time, "seconds")