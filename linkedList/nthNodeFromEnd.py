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
                self.head = node
                self.current = node
            else:
                self.current.next = node
                self.current = self.current.next

    def nthFromEnd(self,n):
        self.temp = self.head
        count=0
        while self.temp!=None:
            count+=1
            self.temp = self.temp.next
        kFromStarting = count-n
        if kFromStarting<0:
            return None
        else:
            count=1
            self.temp=self.head
            while count<kFromStarting+1:
                count+=1
                self.temp=self.temp.next
            return self.temp.data


if __name__ == '__main__':
    arr = [int(i) for i in input("enter elements").split()]
    element = int(input("enter n"))
    ll = LinkedList(arr)
    res = ll.nthFromEnd(element)
    if res == None:
        print("None")
    else:
        print(f"The output is {res}")
