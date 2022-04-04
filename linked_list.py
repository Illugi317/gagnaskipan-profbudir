class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        string = ""
        node = self.head
        while node != None:
            string += str(node.data) + " "
            node = node.next
        return string
    
    def push_back(self, value):
        if self.head == None:
            node = Node(value, None)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
        self.size += 1
    
    def push_front(self, value):
        self.head = Node(value, self.head)
        if self.tail == None:
            self.tail = self.head
        self.size += 1

    def pop_front(self):
        if self.tail == None:
            return self.tail
        value = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = self.head
        self.size -= 1
        return value
    
    def pop_back(self):
        if self.head == None:
            return self.head
        else:
            value = self.tail.data
            node = self.head
            while node.next != None:
                node = node.next
            self.tail = node
            self.tail.next = None 
        self.size -= 1
        return value

    @property
    def size(self):
        return self.size

class Node(object):
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node
    
    def __hash__(self):
        if type(self.key) == int:
            return self.key

        if type(self.key) == str:
            ret_val = 0
            for char in self.key:
                ret_val <<= 7
                ret_val += ord(char)
        
        if type(self.key) == float:
            return int(self.key * 9952)

class Linked_List(object):
    def __init__(self):
        self.head = Node()
        self.size = 0

    def add(self,key,value):
        new_node = Node(key,value,self.head.next)
        self.head.next = new_node
        self.size += 1

    def __iter__(self):
        current = self.head.next
        while current != None:
            yield current
            current = current.next

    def remove(self, key):
        lag = self.head
        for node in iter(self):
            if node.key == key:
                lag.next = lag.next.next
                self.size -=1
            lag = node

