n = int(input())

A = []

for i in range(n) : 
    x, y = map(int, input().split())
    A.append((x,y))
    
A.sort(key = lambda x : (x[1],x[0]))
    
for i in range(n) : 
    print(A[i][0], A[i][1])