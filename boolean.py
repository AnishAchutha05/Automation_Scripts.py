def test(num):
    hash=[]
    for i in str(num):
        if i in hash:
            return True
        else:
            hash.append(i)
            print(hash)
    return False
            
        
        
    
    

num = int(input("Enter a number"))
print(test(num))