def solution(n, arr1, arr2) :
    answer = [''] * n # 입력 배열 크기만큼 키워준다.
    for i in range(n) :
        row = arr1[i]|arr2[i] # OR 논리연산자로 계산
        
        for j in range(n-1,-1,-1) :
            if(((row>>j)&1)==1) : # 비트연산자로 맨 앞자리 수를 구한다.
                answer[i]+='#'
            else :
                answer[i]+=' '
        print(answer[i])
        
        
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
