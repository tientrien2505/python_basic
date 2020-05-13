#  variable
print('#  variable')
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
print('# toan tu so hoc')
a = 123
b = '456'

print('cong chuoi: ', str(a) + b)
print('cong hai so nguyen: ', a + int(b))
print('nhan chuoi vs 1 so nguyen: ', b * 2)

# boolean va toan tu logic
print('# boolean va toan tu logic')
a = 2
print('a == 2? ', a == 2)
print('2 <= a < 5? ', 2 <= a < 5)
print('2 > a < 4? ', 2 > a < 4)
print('2 >= a > 3? ', 2 > a > 3)
print('not (2 >= a or a > 3)? ', not(2 >= a or a > 3))

# cau truc dieu kien
print('# cau truc dieu kien')

if a > 2:
    print('a > 2')
elif a < 2:
    print('a < 2')
else:
    print('a == 2')

# khong co cau truc switch case
print('# khong co cau truc switch case')

# for .. in ..
print('# for .. in ..')
for letter in "hello world":
    print('current letter: ', letter)
fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    print('current fruit: ', fruit)
for index, value in enumerate(fruits):
    print('ith, value: ', index, value)
print('print from 0 to 9:')
for i in range(10):
    print('ith: ', i)

# While
print('# While')
count = 0
while count < 10:
    print('count is: ', count)
    count += 1

# function

print('# function')
def name_function(param1, param2):
    print(param1, param2)

name_function('hello', "Truong Dao")

def sum(a, b):
    return 'a = ' + str(a) + ', b = ' + str(b) + ', a + b = ' + str(a + b)
def plus(a, b = 10):
    return a + b
# def plus(a = 10, b): => error: non-default argument not allow follow default argument
print('sum(1, 2): ', sum(1, 2))
print('plus(1): ', plus(1))
print('sum(b = 2, a = 1): ', sum(b = 2, a = 1))
print('plus(1, 2): ', plus(2, 1))
print('plus(b = 2, a = 1): ', plus(b = 2, a = 1))

def foo(f):
    return f(1, 2)
print('function have param is fuction: ', foo(sum))

print('type of function: ', type(foo))

def printListFruits(listFruits):
    for i, value in enumerate(listFruits):
        print(i, 'th fruit: ', value)

printListFruits(fruits)
# variable-length arguments
print('# variable-length arguments')
def func(*names, **addresses):
    print(names, type(names), addresses, type(addresses))
    for name in names:
        print(name)
    for key_item in addresses.keys():
        print(key_item)
    for value_item in addresses.values():
        print(value_item)
    for item in addresses.items():
        print(item)
func('chien', 'truong', hue = 'yen loi', chieu = 'yen dong')

# string processing
print('# string processing')
str1 = 'Hello'
str2 = 'World'
str3 = list()
str3.append(str1)
str3.append(str2)
print(str3)
paragraph = """this is line 1
this is line 2
this is line 3"""
print(paragraph)
subStr = paragraph[::-1]
print('this is subString: ', subStr, paragraph)
print(paragraph.split(sep = ' ', maxsplit=1))
# some functions process string
# find, replace, strip, split, splitlines, isnumeric, lower, upper
print(len('hello'))
print('vi tri \'l\' trong  \'hello\' tu phai qua trai', str1.rfind('l'))
print(' '.join(str3))
# List
numbers = [1, 2, 3]
names = ['Chien', 'Truong']
print(names[-1])
print(len(names))

print('Chien' in names)
print(1 >> 2)

s = str1.replace('l', 'n', 1)
list.append(names, 'Hue')
print(s)
print(names)

# del names[0]
print(names)
print(numbers + names)
def functonForName(e):
    return len(e)
list.sort(names, key=lambda name : len(name), reverse=True)
print(names)