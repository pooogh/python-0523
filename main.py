# # import math # math.round()
# # from math import ceil as c

# value = 13
# value2 = False

# value = 'text'
# print(value, value2, sep='...')
# print('new print')

# value3 = int(input('Enter age: '))
# print(type(value3))

# if value3 < 18: # if () {body}
#     print('Malish')
# elif 19 <= value3 < 30:
#     print('Middle')
# elif value3 == 35 or value3 == 40:
#     print('35 or 40')
#     # && and
#     # || or
#     # ! not
# else:
#     print('ok')
# # int()
# # float()
# # str()
# # bool()
# '''
# comment
# comment
# '''

# i = 0
# while i <= 3:
#     i += 1
#     print(i)

# text = 'Hello, Pavel!'
# for i in text:
#     print(i)

# # for (let i = 0, i <= 10, i += 1)
# for i in range(10, 2, -2): # range(начало, конец, шаг)
#     print(i)

# def name(x: int, y: int) -> int:
#     """Find a multiply"""
#     return x * y

# print(name(2, 3), name.__doc__)

# def power(x, y):
#     return x ** y

# print(power(y=3, x=2))

# def arrPrint(*args):
#     print(args)

#     def f2():
#         for i in args:
#             print(i ** 2)
#     f2()

# arrPrint(1, 3, 5)

# num1, num2 = 4, 5
# first, *tail = [1, 2, 3]
# print(tail)
# *tail2, last = [6, 7, 8]
# print(last)

# up, down = map(int, input().split())
# print(up)

# # улиточка Ярослав ползет вверх по веточке на n см в день, но ночью Ярослав спит
# # и сплозает вниз по веточке на m см. За сколько суток Ярослав заберется на
# # веточку длиной x см?

# # любитель геометрии Павел загадал Михаилу задачу:
# # - вот тебе бумажка размером n x m
# # - зачем?
# # - посчитай, сколько квадратов со сторой равной минимальной стороне листа, можно вырезать из этого листа?
# # 20х8 -> 8х8(1) 12x8 -> 8x8(2) 4x8 -> 8x8(2) 4x4(1) 4x4 -> 4

# '''
# Людмила плавает в бассейне n x m
# Людмила устала
# До длинного бортика бассейна она на расстоянии х метров
# До короткого на расстоянии у метров
# Какое минимальное расстояние ей нужно проплыть, чтобы не умереть в бассейне?
# '''

# # n 27
# # m 54
# # x 10 x2 17
# # y 12 y2 42
# # ans 10

lst = list()
lst_2 = []
lst_2.append(123)
lst_3 = [1, 2, 3] + [4, 5]
print(lst_3)
lst_4 = [3] * 6
print(lst_4)
lst_5 = [i for i in range(10)]
print(len(lst_5))
print(lst_5[::1])

from random import randrange
lst_6 = [randrange(1, 100) for i in range(12)]
print(lst_6)
# Дан массив.
# Сначала выведите третий элемент этого массива.
print(lst_6[2])
# Во второй строке выведите предпоследний элемент этого массива.
print(lst_6[-2]); print(lst_6[len(lst_6)-2])
# В третьей строке выведите первые пять элементов этого массива.
print(lst_6[:5])
# В четвертой строке выведите весь массив, кроме последних двух элементов.
print(lst_6[:-2])
# В пятой строке выведите все элементы с четными индексами (считая, что индексация начинается с 0, поэтому элементы выводятся начиная с первого).
print(lst_6[::2])
# В шестой строке выведите все элементы с нечетными индексами, то есть начиная со второго элемента массива.
print(lst_6[1::2])
# В седьмой строке выведите все элементы в обратном порядке.
print(lst_6[::-1])
# В восьмой строке выведите все элементы массива через один в обратном порядке, начиная с последнего.
print(lst_6[::-2])
# В девятой строке выведите длину данного массива.
print(len(lst_6))

lst_7 = [1, 2, 3, 2, 7, 5, 12, 4]
# lst_7.insert(5, 'elem')
# lst_7.insert(2, 'elem2')
print(lst_7)
lst_7.remove(2)
print(lst_7)
# lst_7.pop(4)
print(lst_7)
lst_7.reverse()
print(lst_7)
lst_7.sort()
print(lst_7)
sorted(lst_7)
print(min(lst_7), max(lst_7), sum(lst_7))

'''
Илья перевелся в Хекслет колледж
Игорь Андреич на физре построил всех в шеренгу
Илья не знает, что такое шеренга и куда ему встать
Определите, какое. по. счету. место. нужно. занять. Илье. в. шеренге... :(
[154, 168, 192, 205] - на вход
186 - на вход
3 - ответ
'''