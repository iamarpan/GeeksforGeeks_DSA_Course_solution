def removeDuplicate(arr):
    currentPosition=0
    latestPosition=1
    for ele in range(1,len(arr)):
        if(arr[ele] != arr[currentPosition]):
            currentPosition=ele
            arr[latestPosition]=arr[ele]
            latestPosition+=1
    return latestPosition 

if __name__ == '__main__':
    arr = [int(a) for a in input("enter array").split()]
    position = removeDuplicate(arr)
    for i in range(position):
        print(arr[i],end=" ")
    print("")  
