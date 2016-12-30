class Node(object):
    def __init__(self):
        self.data = None
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.first = None
        
    def newNode(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.first
        self.first = new_node
        
    def print_list(self):
        iterator = self.first
        while iterator:
            print iterator.data
            iterator = iterator.next
        
        
my_list = LinkedList()
my_list.newNode(1)
my_list.newNode(2)
my_list.newNode(3)
my_list.newNode(4)
my_list.newNode(5)
my_list.print_list()
  
    