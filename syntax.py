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
