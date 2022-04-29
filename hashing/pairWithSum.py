def checksum(arr,number):
    sum_set = set()
    for a in arr:
        if number-a not in sum_set:
            sum_set.add(a)
        else:
            return True
    return False


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    number = int(input("enter number"))
    print(checksum(arr,number))
