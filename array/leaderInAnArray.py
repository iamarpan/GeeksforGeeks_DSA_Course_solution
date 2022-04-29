def leader(arr):
    last = len(arr)-2 
    leaderArr = [arr[-1]]
    while(last>=0):
        if arr[last]>leaderArr[-1]:
            leaderArr.append(arr[last])
        last-=1
    low=0
    high = len(leaderArr)-1
    while(low<high):
        print("came here")
        leaderArr[low],leaderArr[high]=leaderArr[high],leaderArr[low]
        low+=1
        high-=1
    print(leaderArr)

if __name__ == '__main__':
    arr = [int(i) for i in input("enter array").split()]
    leader(arr)
