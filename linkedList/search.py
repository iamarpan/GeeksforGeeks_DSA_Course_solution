class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def create(self,arr):
        self.head = None
        self.temp = None
        for element in arr:
            node = Node(element)
            if self.head==None:
                self.head = node
                self.temp = self.head
            else:
                self.temp.next = node
                self.temp = self.temp.next

    def print(self):
        self.temp = self.head
        while(self.temp!=None):
            print(self.temp.data,end=" ")
            self.temp = self.temp.next

    def search(self,element):
        pos=1
        self.temp = self.head
        while(self.temp!=None):
            if self.temp.data == element:
                print(f'element found at position {pos}')
                return
            self.temp = self.temp.next
            pos+=1
        print("Not found")
        return  


if __name__ == '__main__':
    arr = [int(i) for i in input("enter elements").split()]
    element = int(input("enter element to search"))
    ll = LinkedList()
    ll.create(arr)
    ll.search(element)
