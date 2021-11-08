def isEven(N) : 
    if (N^1) == (N+1): #만약 N이 10일 경우 1과 xor 시 11이 된다. 즉 N+1 과 비교했을 때 짝수라는 것이 증명됨.
        return 1
    else:
        return 0

N = int(input())

if isEven(N) == 1:
    print("Even")
else:
    print("Odd")
