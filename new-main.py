# value_1 = 10; value_2 = 13
# import math
from math import ceil as c

value_1 = 10
value_2 = 13
print(type(value_2))
print(c(value_1 / value_2))
print(value_1 // value_2)
print(value_1 % value_2)

print('13' == 13) #False
value_2 = str(value_2)
print(type(value_2))

# str()
# int()
# float()
# bool() False True
print(f'text {value_2}')
print('13' + '23', end='; ')
print('13', 23)
print('13' + "23")

value_3 = float(input('Enter your data: '))
print(type(value_3), value_3)

if value_3 % 2 == 0:
    print('chetnoe')
elif value_1 < 20 and value_3 >= 15:
    print(not(value_2 == 13))
    print(value_2 == 12 or value_3 % 3 == 0)
else:
    print('else')

print('end of if')

i = 0
while i <= 3:
    print(i)
    i += 1

value_4 = 'Hello, Mark!'
for i in value_4:
    print(i)

# for (let i = 0, i <= 10, i += 1)
for i in range(5): # от 1 до 4 включительно
    print(i)

for i in range(3, 9): # от 3 до 8 вкл
    print(i)

for i in range(5, 21, 2): # от 5 до 20 вкл каждое 2 число
    print(i)

for i in range(20, -5, 2):
    print(i)

# # улиточка Ярослав ползет вверх по веточке на n см в день, но ночью Ярослав спит
# # и сплозает вниз по веточке на m см. За сколько суток Ярослав заберется на
# # веточку длиной x см?

# # любитель геометрии Павел загадал Михаилу задачу:
# # - вот тебе бумажка размером n x m
# # - зачем?
# # - посчитай, сколько квадратов со сторой равной минимальной стороне листа, можно вырезать из этого листа?
# # 20х8 -> 8х8(1) 12x8 -> 8x8(2) 4x8 -> 8x8(2) 4x4(1) 4x4 -> 4
