def secondLargest(arr):
    res=-1
    largest=0
    for index,value in enumerate(arr):
        if value>arr[largest]:
            res=largest
            largest=index
        elif value == arr[largest]:
            continue
        else:
            if res==-1:
                res=index
            elif arr[res]<value:
                res=index
            else:
                continue
    return res 


if __name__ == '__main__':
    arr = [int(a) for a in input("enter array").split()]
    max2 = secondLargest(arr)
    if max2==-1:
        print("There is no second largest element")
    else:
        print("second largest is {} at index: {}".format(arr[max2],max2))
