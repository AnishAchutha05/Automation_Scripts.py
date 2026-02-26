def checkmap(s,t):
    hash={}

    for i in range(len(s)):
        char=s[i]
        partner = t[i]
        if char not in hash:
            if partner in hash.values():
                return False
            hash[char] = t[i]
        elif hash[char] != partner:
            return False
        
        
    return True

        
