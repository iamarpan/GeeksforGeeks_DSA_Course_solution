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
    
    def deleteLast(self):
        if self.head==None or self.head.next==None:
            self.head=None
        else:
            self.temp=self.head
            while self.temp.next.next!=None:
                self.temp = self.temp.next
            self.temp.next=None

    def print(self):
        self.temp=self.head
        while(self.temp is not None):
            print(self.temp.data)
            self.temp = self.temp.next

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    ll = LinkedList()
    ll.create(arr)
    ll.deleteLast()
    ll.print()
    
