def Solve (N):
    sum = 0
    a = N//2
    for i in range(1 , a+1):
        if N%i == 0:
            sum = sum + i
    if sum == N:
        return "YES"
    else:
        return "NO"
    

T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print (out_)