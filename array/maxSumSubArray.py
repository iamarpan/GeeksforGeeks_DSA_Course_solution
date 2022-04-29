def maxSumSubArray(arr):
    res=arr[0]
    maxEnding = arr[0]
    for a in range(1,len(arr)):
        maxEnding = max(maxEnding+arr[a],arr[a])
        res = max(maxEnding,res)
    return res

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    res = maxSumSubArray(arr)
    print(res)
