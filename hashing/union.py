def union(arr1,arr2):
    union_set = set()
    for a in arr1:
        union_set.add(a)
    for b in arr2:
        union_set.add(b)
    return len(union_set)


if __name__ == '__main__':
    arr1 = [int(i) for i in input("enter array 1: ").split()]
    arr2 = [int(i) for i in input("enter array 2: ").split()]
    count = union(arr1,arr2)
    print("total distinct elements are {}".format(count))
