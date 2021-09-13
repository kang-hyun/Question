import random

f = open('Electric Machinery1.txt', mode='r', encoding='utf-8')
z = f.read()
f.close()
y = z.split('Q')
y.remove('')
random.shuffle(y)
a = y[0]
b = a.split('\n')
c = b[1]
d = b[2]
e = b[3]
print (c)
