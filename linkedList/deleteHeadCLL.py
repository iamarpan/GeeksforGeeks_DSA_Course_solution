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
                self.current=node
            else:
                self.current.next = node
                self.current = self.current.next

        self.current.next = self.head

    def delete(self):
        if self.head == None or self.head.next == self.head:
            self.head=None
        else:
            self.current.next = self.head.next
            self.head= self.head.next


    def __str__(self):
        if self.head==None:
            return ""
        self.temp = self.head
        print(self.temp.data,end=" ")
        self.temp = self.temp.next
        while(self.temp!=self.head):
            print(self.temp.data,end=" ")
            self.temp = self.temp.next
        return ""

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    ll = LinkedList(arr)
    ll.delete()
    print(ll)    
