n, k = map(int, input().split())

Coins = []
for i in range(n) : Coins.append(int(input()))


answer = 0
while k > 0 :
    coin = Coins.pop()
    answer += k // coin
    k %= coin

print(answer)
