def checkmap(a):
    hash={}

    for i in a:
        key = "".join(sorted(i))
        if key not in hash:
            hash[key]= [i]
        else:
            hash[key].append(i)
    return list(hash.values())