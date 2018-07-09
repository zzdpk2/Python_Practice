# -*- coding: utf-8 -*-
print(100+200)

print('The quick brown for fox', 'jump over', 'the lazy dog')

# name = input()

# print('Hello', name)

print(1024*768)

n = 123

f = 456.789

s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa'''

print(n, f, s1, s2, s3, s4)

age = 22

if age >= 18:
    print('adult')
else:
    print('teenager')

print(10//3)

x1 = 'ABC'
x2 = b' ABC'
print(x1, '\n', x2)

print('ABC'.encode('ascii'))

print(b'ABC'.decode('ascii'))

print('中文')

print('Hi %s, your score is %d.' % ('zzd', 100))


g1 = 72
g2 = 85

r = (g2 - g1) / g1
print('%.2f%%' % (r*100))

classmates = ['Michael', 'Bob', 'Tracy']

print('%s' % classmates)

print('%s' % classmates[0])

classmates.insert(3, 'Jack')

print('%s' % classmates)

classmates.pop()

print('%s' % classmates)

classmates.pop(1)

print('%s' % classmates)

print('%d' % len(classmates))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
] 

# 打印Apple 
print(L[0][0])

birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5

BMI = weight / (weight * weight)

if BMI < 18.5:
    print('Light')
elif BMI >= 18.5 & BMI < 25:
    print('Normal')
elif BMI >= 25 & BMI < 28:
    print('Overweight')
elif BMI >= 28:
    print('Fat')
elif BMI > 32:
    print('severe fat')
else:
    print('Error')

# 把names里面的每个元素带入变量names
names = ['Michael', 'Bob', 'Tracey']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

print(list(range(5)))

sum1 = 0
n = 99 
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print(sum1)

L2 = ['Bart', 'Lisa', 'Adam']

for k in L2:
    print('Hello, %s' % k)

# k1 = -1
# while (k1 != 0):
#     print("1")

