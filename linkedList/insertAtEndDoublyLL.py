class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def create(self,data):
        self.head=None
        self.current=None
        self.prev=None
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
        print("reversal list")
        self.temp = self.current
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.prev
        print()


    def insertAtLast(self,last):
        self.temp = self.head
        self.prev = None
        node = Node(last)
        if self.head==None:
            self.head=node
        else:
            self.temp =self.head
            while(self.temp.next!=None):
                self.temp = self.temp.next
            self.temp.next=node
            self.prev = self.temp
            self.temp = self.temp.next
            self.temp.prev = self.prev
            self.current = self.temp

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    element = int(input("enter element"))
    ll = LinkedList()
    ll.create(arr)
    ll.print()
    ll.insertAtLast(element)
    ll.print()
