이름 = "김오즈"
나이 = 14
소속 = "마법중"
등급 = 3

print(type(이름))

print(type(float(10)-2))
print(type(3.0 + 7.0))

과일 = 'apple'
print(과일.count('p'))

print(8 == 2 * 4,
    4 != 2 + 2,
    2 * 3 is 3 + 3,
    8 is 4 * 2.0,
    5 is 6 - 1.1)

print('text' and True)

x = int(input())
print(x % sum(int(i) for i in str(x)) == 0)