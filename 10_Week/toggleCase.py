def toggleCase(str) : 
    temp = list(str) #문자열 리스트로 변경
    for i in range(len(temp)):
        temp[i]=chr(ord(str[i])^32) #아스키코드로 변경 후 xor 실행 다시 문자로 변경
    return "".join(temp) #list 를 str로 변경
    
Str = input()

print(toggleCase(Str))
