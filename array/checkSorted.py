def checkSorted(arr):
    if len(arr)==1:
        return True
    else:
        sorted=True
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                sorted=False
        if(sorted):
            return True
        
        sorted=True
        for i in range(len(arr)-1):
            if(arr[i]<arr[i+1]):
                sorted=False
        return sorted

if __name__ == '__main__':
    arr = [int(a) for a in input("enter array:").split()]
    sorted  = checkSorted(arr)
    if(sorted):
        print("array is sorted")
    else:
        print("array not sorted")
