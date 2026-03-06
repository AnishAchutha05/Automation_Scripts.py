A = [3, 1, 2, 4, 7]

def evod(A):
    n=len(A)
    flag=True
    while flag:
        flag = False
        for i in range(1,n):
            if A[i-1]%2!=0 and A[i]%2 == 0:
                flag= True
                A[i-1], A[i] = A[i], A[i-1]
evod(A)
print(A)