# Section04 -2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()

print(len(str1), len(str2),len(str3),len(str4))


escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\t"
print(escape_str2)

#Raw String
row_s1 = r'C:\Programs\Test\Bin'
print(row_s1)
row_s2 = r"\\a\a"
print(row_s2)

#멀티라인 \다음에 문자열 연결
multi =  \
"""  문자열 
멀티라인 
테스트 """

print(multi)

#문자열 연산
str_o1='*'
str_o2='abc'
str_o3='def'
str_o4="Niceman"

print(str_o1*100)
print(str_o2+str_o3)
print(str_o1*3)
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형변환
print(str(77)+'a')
print(str(10.4))

# 문자열 함수

# a='niceman'
# b='orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice','good'))
# print(list(reversed(b)))


a='niceman'
b='orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])
















