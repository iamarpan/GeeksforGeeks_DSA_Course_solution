def subArray(arr):
    maxEnding = arr[0]
    res = arr[0]
    for a in range(1,len(arr)):
        maxEnding = max(arr[a]+maxEnding,arr[a])
        res = max(res,maxEnding)
    minEnding = arr[0]
    res2 = arr[0]
    for a in range(1,len(arr)):
        minEnding = min(arr[a]+minEnding,arr[a])
        res2 = min(minEnding,res2)
    circular = sum(arr)-res2
    return max(circular,res)
        

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    maxSum = subArray(arr)
    print(maxSum)
