class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,arr):
        self.head=None
        self.current=None
        for element in arr:
            node = Node(element)
            if self.head==None:
                self.head=node
                self.current = node
            else:
                self.current.next = node
                self.current = node

    def __str__(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
        return ""

    def middle(self):
        if self.head==None:
            print("None")
        elif self.head.next==None:
            print(self.head.data)
        else:
            self.fast=self.head
            self.slow=self.head
            while self.fast!=None and self.fast.next!=None:
                self.slow = self.slow.next
                self.fast = self.fast.next.next
            print(self.slow.data)
            
if __name__ == '__main__':
    arr = [int(i) for i in input("enter data").split()]
    ll = LinkedList(arr)
    print(ll)
    ll.middle()
