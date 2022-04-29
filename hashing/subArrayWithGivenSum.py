def checkSum(arr,number):
    sum_set = set()
    current_sum = 0
    for a in arr:
        current_sum+=a
        if (current_sum-number) in sum_set or current_sum==number:
            return True
        sum_set.add(current_sum)
    return False

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array: ").split()]
    number = int(input("enter number"))
    print(checkSum(arr,number))
