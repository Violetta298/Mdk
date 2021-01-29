
a = 5
b = 10
b = (a + b) - b
a = a + b
print(a, b)

a = int(input()) # 123

sum = 0

a = str(a) # '123'
for i in a:
    i = int(i)
    sum += i
print(sum)

import math
a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x_one = (-b + math.sqrt(D)) / (2 * a)
    x_two = (-b - math.sqrt(D)) / (2 * a)
    print(x_one, x_two)
elif D == 0:
    x = (-b) / (2 * a)
    print(x)
else:
    print('Discriminant menshe 0')


