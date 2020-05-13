#  variable
a = 123
print(type(a))
a = 'hello world!'
print(type(a))
a = [1, 2, 3]
print(type(a))
a = [1.2, 'Hello World', 'W', 2]
print(type(a))
a = (1.2, 'Hello World', 'W', 2)
print(type(a))
for i, value in enumerate(a):
    print(i, value)


# toan tu so hoc
a = 123
b = '456'

print('cong chuoi: ', str(a) + b)
print('cong hai so nguyen: ', a + int(b))
print('nhan chuoi vs 1 so nguyen: ', b * 2)

# boolean va toan tu logic
a = 2
print('a == 2? ', a == 2)
print('2 <= a < 5? ', 2 <= a < 5)
print('2 > a < 4? ', 2 > a < 4)
print('2 >= a > 3? ', 2 > a > 3)
print('not (2 >= a or a > 3)? ', not(2 >= a or a > 3))

# cau truc dieu kien

if a > 2:
    print('a > 2')
elif a < 2:
    print('a < 2')
else:
    print('a == 2')
