# 문자열 문자, 단어 등으로 구성된 문자들의 집합을 나타냅니다.
# 파이썬에는 4개의 문자열 표현 방법이 존재합니다.

a = "Hello Wolrd" #1
a = 'Hello Python' #2
a = """Python Hello""" #3
a = '''Python String''' #4

# 1. 문자열에 작은 따옴표를 포함시킬경우를 위해 제작
# Python's very good 을문자열로 하기위해서는? a = "Python's very good"

# 2. 위와 같이 문자열에 큰 따옴표를 표함하기위해서 제작되었다
# I want Study "Python" => a = 'I want Study "Python"'

# 3. 파이썬에서 줄바꿈을 위해서는 \n을 삽입하여 처리한다
# 이러한 불편함을 줄이기위해 3,4번을 사용하는데
# multiLine = '''
# Is very
# Simple! '''

# 문자열 처리방법

one = 'this'
two = 'is first'
print(one + two) # this is first
# 일반적인 + 수식을 이용하여 처리하는 문자열 더하기

one = "test"
print(one * 2) # testtest
# 문자열을 곱하면 파이썬은 곱한수만큼의 문자열을 반복한다

one = "I want Study Python..."
print(one[3]) # a
# 문자열 슬라이싱을 배열이 아니더라도 문자를 얻을 수 있다.

print(one[0:5]) # I want
# 문자열 슬라이싱을 [시작번호 : 끝 번호]와 [:끝번호]로 문자를 얻을 수 있다.

# 관련 함수
# count 문자 개수 세기
# count('문자')  문자가 나온 수 출력