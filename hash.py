def  hashing(new):
    hash={}

    for i in new:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    
    return hash
new = str(input("give me a word"))
print(hashing(new))