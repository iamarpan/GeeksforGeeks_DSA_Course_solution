class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def create(self,data):
        self.head=None
        self.current =None
        self.prev = None
        for element in data:
            node = Node(element)
            if self.head==None:
                self.head = node
                self.prev = node
                self.current = node
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
        self.temp = self.current
        print("reverse list")
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.prev
        print()


    def reverse(self):
        if self.head==None:
            return None
        else:
            self.low= self.head
            self.high = self.current
            while(self.low!=self.high and self.low.next!=self.high.prev):
                self.low.data,self.high.data = self.high.data,self.low.data
                self.low = self.low.next
                self.high = self.high.prev
            self.low.data,self.high.data=self.high.data,self.low.data


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    ll = LinkedList()
    ll.create(arr)
    ll.print()
    ll.reverse()
    ll.print()
