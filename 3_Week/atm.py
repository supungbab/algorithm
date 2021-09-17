n, P = int(input()), sorted(list(map(int,input().split())))
for i in range(1,n):
    P[i] += P[i-1]
print(sum(P))
