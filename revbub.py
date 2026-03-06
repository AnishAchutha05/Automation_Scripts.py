A = [64, 34, 25, 12, 22, 11, 90]

def bubble(A):
    n= len(A)
    flag= True
    while flag:
        flag = False
        for i in range(1,n):
            if A[i-1] < A[i]:
                flag = True
                A[i-1], A[i] = A[i], A[i-1]
    
bubble(A)
print(A)
    
    
