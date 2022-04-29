def maxCons1(arr):
    count=0
    maximum=0
    for a in arr:
        if a == 1:
            count+=1
            maximum=max(count,maximum)
        else:
            count=0
    print(maximum)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    maxCons1(arr)
