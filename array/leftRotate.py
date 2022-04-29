def leftRotate(arr):
    start = arr[0]
    for a in range(1,len(arr)):
        arr[a],arr[a-1]=arr[a-1],arr[a]
    arr[-1]=start
    print(arr)


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    leftRotate(arr)
