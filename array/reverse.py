if __name__ == '__main__':
    arr = [int(a) for a in input("enter array").split()]
    mid = (len(arr)-1)//2
    length= len(arr)-1
    for index in range(mid+1):
        arr[index],arr[length-index] = arr[length-index],arr[index]
    print("swapped array is {}".format(arr))
