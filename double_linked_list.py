#TODO: implement sorts in ddl
class Node:
    def __init__(self, data = None, prev = None, next_val = None):
        self.data = data
        self.prev = prev
        self.next = next_val

class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None) 
        self.current = self.tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def next_node(self,node):
        return node.next
    
    def prev_node(self,node):
        return node.prev

    def insert_between(self, data, prev, next_node):
        new = Node(data, prev, next_node)
        prev.next = new
        next_node.prev = new
        self.size += 1
        return new

    def insert(self, data):
        self.current = self.insert_between(data, self.current.prev, self.current)

    def remove_helper(self, node):
        rem = node.data
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return rem

    def remove(self):
        if self.current.data is self.tail.data:
            return
        if self.current is self.head:
            return
        if self.size == 0:
            return
        self.current = self.next_node(self.current)
        return self.remove_helper(self.prev_node(self.current))

    def get_value(self):
        return self.current.data

    def move_to_next(self):
        if self.current == self.tail:
            return
        
        self.current = self.next_node(self.current)

    def move_to_prev(self):
        if self.current == self.next_node(self.head):
            return
        
        self.current = self.prev_node(self.current)

    def move_to_pos(self, pos):
        if 0 > pos or pos > self.size:
            return
        count = 0
        walk = self.next_node(self.head)
        while walk != self.next_node(self.tail):
            if count == pos:
                self.current = walk
                return
            count += 1
            walk = self.next_node(walk)

    def clear(self):
        self.__init__()

    def get_first_node(self):
        if self.head.next != None:
            return self.head.next
        else:
            return None

    def get_last_node(self):
        if self.tail.prev != None:
            return self.tail.prev
        else:
            return None

    def _swap(self, node1, node2):
        #Swap the data of two nodes
        temp = node1.data
        node1.data = node2.data
        node2.data = temp
        
    def partition(self, l, h):
    # set pivot as h element
        x = h.data;
        # similar to i = l-1 for array implementation
        i = l.prev;
        j = l
        # Similar to "for (int j = l; j <= h- 1; j++)"
        while(j != h):
            if(j.data <= x):
                # Similar to i++ for array
                i = l if(i == None) else i.next;
                temp = i.data;
                i.data = j.data;
                j.data = temp;
            j = j.next
        i = l if (i == None) else i.next;  # Similar to i++
        temp = i.data;
        i.data = h.data;
        h.data = temp;
        return i;
    
    def _sort(self, l, h):
        if(h != None and l != h and l != h.next):
                temp = self.partition(l, h);
                self._sort(l,temp.prev);
                self._sort(temp.next, h);
        
    def sort(self):
        self._sort(self.head, self.head)    
    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        next_node = self.next_node(self.head)
        while next_node != self.tail:
            ret_str += str(next_node.data) + " "
            next_node = self.next_node(next_node)
        return ret_str


if __name__ == "__main__":
    #create tests here if you want
    a = DLL()
    a.insert(3)
    a.insert(4)
    a.insert(3)
    a.insert(2)
    a.insert(5)
    a.insert(6)
    print(a)
    a.sort()
    print(a)
    print("wtf")
