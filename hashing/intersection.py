def intersection(arr1,arr2):
    count=0
    arr2_set = set(arr2)
    for a in arr1:
        if a in arr2_set:
            count+=1
            arr2_set.remove(a)
    return count


if __name__ == '__main__':
    arr1 = [int(i) for i in input("enter array").split()]
    arr2 = [int(i) for i in input("enter array 2").split()]
    count = intersection(arr1,arr2)
    print(count)
