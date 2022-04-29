class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def create(self,data):
        self.head=None
        self.temp = None
        for a in data:
            node = Node(a)
            if self.head==None:
                self.head=node
                self.temp=self.head
            else:
                self.temp.next = node
                self.temp = self.temp.next
        return self.head

    def insertAtEnd(self,element,pos):
        self.temp = self.head
        count=1
        while(count<pos-1):
            self.temp = self.temp.next
            if self.temp==None:
                return 
            count+=1
        node = Node(element)
        node.next = self.temp.next
        self.temp.next = node
    

    def print(self):
        self.temp=self.head
        while(self.temp is not None):
            print(self.temp.data)
            self.temp = self.temp.next



if __name__ == '__main__':
    arr = [int(i) for i in input("enter elements").split()]
    element = int(input("enter element to insert"))
    pos = int(input("enter position to insert at"))
    ll = LinkedList()
    ll.create(arr)
    ll.insertAtEnd(element,pos)
    ll.print()
    
