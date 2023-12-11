# Q.1 10점
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target): 
    if target in my_string: #if 문을 이용하여 조건문이 참이면 1, 거짓이면 0을 return 하도록 하였다.
        answer = 1          #'in'을 이용하여 조건문을 "target 문자열이  my_string 문자열 안에 있는가?" 로 설정하였다.
    else:                   #target 문자열이 my_string 문자열 안에 있으면 참, 그렇지 않으면 1을 반환한다.
        answer = 0

    return answer


print(solution("final","fi"))  #print 문을 이용하여 함수가 잘 작동하는지 확인해 보았다.
print(solution("final","ab"))