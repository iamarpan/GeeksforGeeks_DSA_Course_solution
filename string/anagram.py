def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    freq = {}
    for char in str1:
        freq[char] = freq.get(char,0)+1
    for char in str2:
        if char not in freq:
            return False
        freq[char]-=1
        if freq[char]==0:
            del freq[char]
    if len(freq.keys())==0:
        return True
    return False


if __name__ == '__main__':
    str1 = input("enter string 1: ")
    str2 = input("enter string 2: ")
    print(anagram(str1,str2))
