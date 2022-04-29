class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def create(self,data):
        self.head=None
        self.current=None
        self.prev = None
        for element in data:
            node = Node(element)
            if self.head==None:
                self.head=node
                self.current=node
                self.prev=node
            else:
                self.current.next = node
                self.current = self.current.next
                self.current.prev = self.prev
                self.prev = self.current

    def print(self):
        self.temp = self.head
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
        
        print("reverse of list")
        self.temp=self.current
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.prev

    def insertAtBegin(self,data):
        node = Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node




if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    element = int(input("enter element"))
    ll = LinkedList()
    ll.create(arr)
    ll.print()
    ll.insertAtBegin(element)
    print("After inserting")
    ll.print()
