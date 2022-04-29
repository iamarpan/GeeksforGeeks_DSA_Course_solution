def maxDiff(arr):
    minimum=arr[0]
    current=arr[1]
    maxDiff = current-minimum
    for a in range(1,len(arr)):
        if arr[a]-minimum>maxDiff:
            maxDiff=arr[a]-minimum
        if arr[a]<minimum:
            minimum=arr[a]
    return maxDiff        


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    result = maxDiff(arr)
    print(result)
