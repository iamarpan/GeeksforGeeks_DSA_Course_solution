def buyAndSell(arr):
    profit = 0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    print(profit)    

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    buyAndSell(arr)
