class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,arr):
        self.head=None
        self.current = None
        for element in arr:
            node = Node(element)
            if self.head==None:
                self.head=node
                self.current = node
            else:
                self.current.next = node
                self.current = self.current.next
        
        self.current.next=self.head

    def find(self,k):
        counter=1
        self.temp = self.head
        while(k>counter):
            self.temp=self.temp.next
            counter+=1
        print(self.temp.data)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    kth = int(input("enter kth element"))
    ll = LinkedList(arr)
    ll.find(kth)
