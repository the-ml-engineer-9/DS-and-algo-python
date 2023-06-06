
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        return str(self.data)
        
class LinkedList:
    
    def __init__(self):
        # this is the first node of linked list
        # We can access this node exclusively!!
        self.head = None
        self.num_of_nodes = 0
        
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        # the head is NULL (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        # so this is when the linked list is not empty    
        else:
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node
        
    def insert_end(self, data):
        self.num_of_nodes +=1
        new_node = Node(data)
        
        # check whether linked list is empty
        if self.head is None:
            self.head = new_node
        # when the linked list is not empty    
        else:
            actual_node = self.head
            
            # this is why it has O(N) linear running time 
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            
            # actual_node is the last node: so we insert the new_node
            # right after the actual_node
            actual_node.next_node = new_node
    
    # O(N) linear running time        
    def remove(self, data):
        
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
            
        if actual_node is None:
            return 
        
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node
            
    
    # O(1)
    def size_of_list(self): 
        return self.num_of_nodes
    
    # O(N)
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node
            
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Adam')
    linked_list.insert_start(7.5)
    linked_list.insert_start(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    
        
        
