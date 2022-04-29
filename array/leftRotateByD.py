def reverse(arr,low,high):
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

def leftRotate(arr,d):
    n=len(arr)
    arr = reverse(arr,0,d-1)    
    arr = reverse(arr,d,n-1)
    arr = reverse(arr,0,n-1)
    print(arr)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    d = int(input("rotate by"))
    leftRotate(arr,d)
