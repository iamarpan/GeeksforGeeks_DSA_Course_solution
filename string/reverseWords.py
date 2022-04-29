def reverseWords(str1):
    words = str1.split()
    low=0
    high=len(words)-1
    while(low<=high):
        words[low],words[high]=words[high],words[low]
        low+=1
        high-=1
    str1 = " ".join(words)
    return str1

if __name__ == '__main__':
    str1 = input("enter string")
    print(reverseWords(str1))
