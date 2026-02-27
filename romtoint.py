def romanhash(s):
    hash={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0

 
    for i in range(len(s)):
        if i+1 < len(s):
            char = s[i]
            next = s[i+1]
              
            if hash[char] >= hash[next]:
                total += hash[char]
            else:
                total -= hash[char]
        else:
            total += hash[char]
    return total
        