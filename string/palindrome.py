def palindrome(arr):
    low = 0
    high = len(arr)-1
    while(low<=high):
        if arr[low]!=arr[high]:
            return False
        low+=1
        high-=1
    return True

if __name__ == '__main__':
    arr = input("enter string")
    print(palindrome(arr))
