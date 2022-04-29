def majorityElement(arr):
    count=1
    res=0
    for a in range(1,len(arr)):
        if (arr[res]==arr[a]):
            count+=1
        else:
            count-=1
        if(count==0):
            res=a
            count=1
    count=0
    for a in range(len(arr)):
        if arr[res]==arr[a]:
            count+=1
    n=len(arr)//2
    if (count<=n):
        return -1
    return arr[res]

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    print(majorityElement(arr))
