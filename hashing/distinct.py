def distinct(arr):
    return len(set(arr))

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    length = distinct(arr)
    print("The number of distinct elements is {}".format(length))
