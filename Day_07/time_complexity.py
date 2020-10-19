a = 0
n = 100
while a < n:
    a += 1


a = 0
b = 0
c = 1
n = 2
while a < n:
    while b < n:
        c = (c + 1) ** 2
        b += 1
    a += 1

print(c)

