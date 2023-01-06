# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# %X로 출력하면 대문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)
a = input()
n = int(a)
print('%x' % n)

# 16진수를 입력받아 8진수로 출력
a = input()
n = int(a, 16)
print('%o' % n)

# 영문자를 10진수 유니코드로 변환
# n = ord(input()) 입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.
# 실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다.
# ord(c) : 문자 c 를 10진수로 변환한 값
n = ord(input())
print(n)
