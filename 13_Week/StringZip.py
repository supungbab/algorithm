def solution(s) :
    answer = len(s)
    length = len(s) #문자열 길이 저장 
    count = 0 # 카운트
    equ = '' # 비교 변수
    string = '' # 문자열 이어 붙일 변수
    for i in range(1,int(length/2)+1,1) : #최대 반복이 문자열 길이 절반일테니까
        string=''
        for j in range(0,length,i) : # 반복
            if j==0 :
                equ = s[j:j+i] #처음 값
            if s[j:j+i] == equ : #같으면 +1
                count+=1
            else : # 카운트 개수가 한개 이상이라면 문자열 생성 이어붙이기 없으면 그냥 기본만
                if count>1 :
                    string+=str(count)+equ
                else :
                    string+=equ
                equ=s[j:j+i]
                count=1
        if count>1 :
            string+=str(count)+equ
        else :
            string+=equ
        count=0
        if answer>len(string) :
            answer=len(string)
    print(answer)
    
solution("abcabcabcabcdededededede")
