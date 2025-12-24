class Node:
    def __init__(self,data):
        self.dat=data
        self.ref=None

class Linked_list:
    def __init__(self,head):
        self.head=None

    def add_node(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            print("not empty")

    def add_beg(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.ref:
            temp=temp.ref
        temp.ref = new_node

    def add_pos(self,data,pos):
        new_node = Node(data)
        temp = self.head
        if pos == 0:
          new_node.ref = self.head
          self.head = new_node
          return
        for _ in range(pos - 1):
            if temp is None:
                print("out of bound")
                return
            temp = temp.ref
            
        if temp is None:
            print("out of bounds")
        else:
            new_node.ref = temp.ref
            temp.ref = new_node
    def delete_beg(self):
        if             