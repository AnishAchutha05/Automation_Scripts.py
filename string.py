def checkmap(a):
    hash={}

    for i in a:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    for i in range(len(a)):
        char = a[i]
        if hash[char] == 1:
            return i
    return -1

