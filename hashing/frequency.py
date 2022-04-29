def frequency(arr):
    count={}
    for a in arr:
        count[a]= count.get(a,0)+1
    return count

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    array_frequency = frequency(arr)
    for key,value in array_frequency.items():
        print(key,value)
