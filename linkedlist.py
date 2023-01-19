class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

#LinkedList Class
class LinkedList():
    def __init__(self):
        self.head = None #front of the list, beginning
    

    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    
    def insert_after(self, prev_node, new_value):
        if prev_node is None:
            print("The given node must not be empty.")
            return
        else:
            new_node = Node(new_value)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
        

    def append_(self, new_value):
        new_node = Node(new_value)
        
        if self.head == None:
            self.head = new_node
            
        last = self.head
        
        while last.next:
            last = last.next
        
        last.next = new_node
    

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print('...get ready for a happy new year!')


#set of commands to create months linked list

months_of_the_year = LinkedList()
months_of_the_year.push_on('January')
months_of_the_year.append_('February')
months_of_the_year.append_('April')
months_of_the_year.append_('May')
months_of_the_year.append_('June')
months_of_the_year.append_('July')
months_of_the_year.append_('August')
months_of_the_year.append_('September')
months_of_the_year.append_('October')
months_of_the_year.append_('November')
months_of_the_year.append_('December')
months_of_the_year.insert_after(months_of_the_year.head.next , 'March')
months_of_the_year.traverse()
