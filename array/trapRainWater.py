def trapRainWater(arr):
    left=[arr[0]]
    right=[arr[-1]]
    maximum=arr[0]
    for a in arr:
        if a > maximum:
            maximum=a
        left.append(maximum)
    maximum=arr[-1]
    for a in arr[::-1]:
        if a > maximum:
            maximum=a
        right.append(maximum)

    count=0
    for a in range(1,len(arr)-1):
        count += min(right[a],left[a])-arr[a]
    print(count)


if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    trapRainWater(arr)
