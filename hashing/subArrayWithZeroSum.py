def zeroSum(arr):
    sum_set = set()
    current_sum=0
    for a in arr:
        if a not in sum_set:
            current_sum+=a
            if current_sum==0 or a==0:
                return True
            sum_set.add(current_sum)
        else:
            return True
    return False


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    print(zeroSum(arr))
