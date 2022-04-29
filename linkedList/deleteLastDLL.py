class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class LinkedList:
    def create(self,data):
        self.head=None
        self.current = None
        self.prev = None
        for element in data:
            node = Node(element)
            if self.head==None:
                self.head=node
                self.current = node
                self.prev = node
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
        print("reversed list: ",end=" ")
        self.temp = self.current
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.prev
        print()

    def deleteLast(self):
        if self.head==None or self.head.next==None:
            return None
        else:
            self.prev = self.current.prev
            self.prev.next=None
            self.current = self.current.prev

if __name__ == '__main__':
    arr = [int(i) for i in input("enter elements").split()]
    ll = LinkedList()
    ll.create(arr)
    ll.print()
    ll.deleteLast()
    ll.print() 
