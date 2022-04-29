def alternateEvenOdd(arr):
    count=1
    maximum=1
    if arr[0]%2==0:
        even=True
    else:
        even=False
    for a in range(1,len(arr)):
        if even and arr[a]%2!=0:
            count+=1
            even=False
        elif not even and arr[a]%2==0:
            count+=1
            even=True
        else:
             maximum = max(maximum,count)
             count=1
    return max(maximum,count)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    res = alternateEvenOdd(arr)
    print(res)
