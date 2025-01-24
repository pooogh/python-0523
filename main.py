# import math # math.round()
# from math import ceil as c

value = 13
value2 = False

value = 'text'
print(value, value2, sep='...')
print('new print')

value3 = int(input('Enter age: '))
print(type(value3))

if value3 < 18: # if () {body}
    print('Malish')
elif 19 <= value3 < 30:
    print('Middle')
elif value3 == 35 or value3 == 40:
    print('35 or 40')
    # && and
    # || or
    # ! not
else:
    print('ok')
# int()
# float()
# str()
# bool()
'''
comment
comment
'''

i = 0
while i <= 3:
    i += 1
    print(i)

text = 'Hello, Pavel!'
for i in text:
    print(i)

# for (let i = 0, i <= 10, i += 1)
for i in range(10, 2, -2): # range(начало, конец, шаг)
    print(i)

def name(x: int, y: int) -> int:
    """Find a multiply"""
    return x * y

print(name(2, 3), name.__doc__)

def power(x, y):
    return x ** y

print(power(y=3, x=2))

def arrPrint(*args):
    print(args)

    def f2():
        for i in args:
            print(i ** 2)
    f2()

arrPrint(1, 3, 5)

num1, num2 = 4, 5
first, *tail = [1, 2, 3]
print(tail)
*tail2, last = [6, 7, 8]
print(last)

up, down = map(int, input().split())
print(up)

# улиточка Ярослав ползет вверх по веточке на n см в день, но ночью Ярослав спит
# и сплозает вниз по веточке на m см. За сколько суток Ярослав заберется на
# веточку длиной x см?

# любитель геометрии Павел загадал Михаилу задачу:
# - вот тебе бумажка размером n x m
# - зачем?
# - посчитай, сколько квадратов со сторой равной минимальной стороне листа, можно вырезать из этого листа?
# 20х8 -> 8х8(1) 12x8 -> 8x8(2) 4x8 -> 8x8(2) 4x4(1) 4x4 -> 4

'''
Людмила плавает в бассейне n x m
Людмила устала
До длинного бортика бассейна она на расстоянии х метров
До короткого на расстоянии у метров
Какое минимальное расстояние ей нужно проплыть, чтобы не умереть в бассейне?
'''

# n 27
# m 54
# x 10 x2 17
# y 12 y2 42
# ans 10


