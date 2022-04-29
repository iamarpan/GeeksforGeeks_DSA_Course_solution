class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def create(self,arr):
        self.arr = arr
        self.head=None
        temp=None
        for element in self.arr:
            node = Node(element)
            if self.head==None:
                self.head=node
                temp=self.head
            else:
                node = Node(element)
                temp.next = node
                temp = temp.next
        return self.head

    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next


    def printRecursion(self,head):
        if head is None:
            return
        else:
            print(head.data,end=" ")
            self.printRecursion(head.next)


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    ll = LinkedList()
    head = ll.create(arr)
    ll.printRecursion(head)
    
