def shiftZero(arr):
    pos=0
    for current in range(len(arr)):
        if arr[current]!=0:
            arr[pos],arr[current]=arr[current],arr[pos]
            pos+=1
    print(arr)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter numbers").split()]
    shiftZero(arr)
