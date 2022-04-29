def subsequence(str1,str2):
    n = len(str2)
    pointer=0
    for a in str1:
        if a == str2[pointer]:
            pointer+=1
        if pointer==n:
            return True
    return False


if __name__ == '__main__':
    str1 = input("enter string 1")
    str2 = input("enter string 2")
    print(subsequence(str1,str2))
