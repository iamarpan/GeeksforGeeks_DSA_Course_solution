class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self,arr):
        self.head=None
        self.current = None
        self.prev = None
        for element in arr:
            node = Node(element)
            if self.head==None:
                self.current = node
                self.head=node
                self.prev=node
            else:
                self.current.next = node
                self.current = self.current.next
                self.current.prev = self.prev
                self.prev = self.current

        self.current.next = self.head   
        self.head.prev = self.current

    
    def __str__(self):
        self.temp = self.head
        print(self.temp.data,end=" ")
        self.temp = self.temp.next
        while self.temp!=self.head:
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
        print()
        print("in reverse")
        self.temp= self.current
        print(self.temp.data,end=" ")
        self.temp = self.temp.prev
        while(self.temp!=self.current):
            print(self.temp.data,end=" ")
            self.temp = self.temp.prev
        
        print("checking reverse")
        print(self.current.next.data,self.head.data)
        return  ""
    
if __name__ == '__main__':
    arr = [int(i) for i in input("enter elements").split()]
    ll = LinkedList(arr)
    print(ll)
