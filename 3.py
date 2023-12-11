# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    num = {'0' :'a',  '1' :'b', '2' :'c', '3' :'d', '4' :'e', '5' :'f', '6' :'g', '7' :'h', '8' :'i', '9' :'j'}
    #딕셔너리를 이용해 key(숫자)에 대응하는 value값(문자)을 설정해주었다. 
    answer = ' '
   
    for i in str(age):           #str()함수를 이용해 age 숫자를 문자열로 변환하였다. 
        answer = answer + num[i] #변수 i 를 설정해 문자열의 첫번쨰 요소 부터 마지막 요소까지 차례로 변수에 대입 되도록 하였다.
                                 # answer에 num[i]를 차례대로 더하여 key에 대응되는 value값을 반환히도록 하였다. 
       
    return answer


print(solution(23))
print(solution(987))