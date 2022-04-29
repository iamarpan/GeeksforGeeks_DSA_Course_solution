def leftmost(str1):
    arr = [-1]*26
    str1 = str1.lower()
    for char in str1:
        arr[ord(char)-97]+=1
    for a in arr:
        if a == 0:
            char = chr(97+a)
    return -1

if __name__ == '__main__':
    str1 = input("enter string")
    print(leftmost(str1))
