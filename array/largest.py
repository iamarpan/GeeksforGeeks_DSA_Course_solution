def largest(arr):
    maximum =arr[0]
    for ele in arr:
        if ele>maximum:
            maximum=ele
    return maximum

if __name__ == '__main__':
    arr = [int(a) for a in input("enter array").split()]
    max = largest(arr)
    print("max is {}".format(max))
