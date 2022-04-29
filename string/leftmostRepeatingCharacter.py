def leftmost(str):
    freq = {}
    for index,value in enumerate(str):
        if value not in freq:
            freq[value]=[index]
        else:
            freq[value].append(index)
    minimum=len(str)
    for key,value in freq.items():
        if len(value)>1 and value[0]<minimum:
            minimum=value[0]
    if minimum==len(str):
        return -1
    return minimum
            
if __name__ == '__main__':
    str = input("enter string")
    print(leftmost(str))
