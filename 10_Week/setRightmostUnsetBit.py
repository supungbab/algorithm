import math # log2를 위한 함수

def getPosOfRightmostSetBit(n) : 
    return int(math.log2((n+1)& ~n)+1)

def setRightmostUnsetBit(n) :
    if n == 0 : # n이 0이면 1 반환
        return 1
    if n&(n+1) == 0 : # 모든 비트가 다 1일 경우 그냥 출력 예) 15 같은 경우 (1111) 인데 이를 16 (10000) 과 비교하면 0이 나옴
        return n
    pos = getPosOfRightmostSetBit(n) # 계산
    return ((1<<(pos-1))|n)
    
n = int(input())

print(setRightmostUnsetBit(n))
