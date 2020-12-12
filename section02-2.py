# Section02-2
# 파이썬 기초코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩(UTF-8)
print(sys.stdin.encoding)
print(sys.stdout.encoding)


# 출력문
print('My name is Goodboy!')

# 변수 선언
myName='Goodboy'

# 조건문 
if myName == 'Goodboy':
    print('Ok') #들여쓰기 indent

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j),i*j)

# 변수 선언(한글)

이름 = "좋은사람"
print(이름)

# 함수 선언
def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))