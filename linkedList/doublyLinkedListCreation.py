class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def create(self,arr):
        self.head = None
        self.current=None
        self.prev = None
        for element in arr:
            node = Node(element)
            if self.head==None:
                self.head=node
                self.current = self.head
                self.current.prev=self.prev
                self.prev=self.current
            else:
                self.current.next = node
                self.current = self.current.next
                self.current.prev = self.prev
                self.prev = self.current 
    
    def print(self):
        self.temp = self.head
        while(self.temp!=None):
            print(self.temp.data)
            self.temp = self.temp.next
        print("reverse list")
        
        self.temp = self.current        
        while(self.temp!=None):
            print(self.temp.data)
            self.temp = self.temp.prev

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    ll=LinkedList()
    ll.create(arr)
    ll.print()
    
