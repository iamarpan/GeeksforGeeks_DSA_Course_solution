def freqInSortedArray(arr):
    count=1
    for a in range(len(arr)-1):
        if arr[a]==arr[a+1]:
            count+=1
        else:
            print(arr[a],count)
            count=1
    if arr[-2]==arr[-1]:
        print(arr[-1],count)
    else:
        print(arr[-1],count)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    freqInSortedArray(arr)
