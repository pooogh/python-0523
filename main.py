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
# n = int(input())
# lst_5 = [int(input()) for i in range(n)]
# print(len(lst_5))
# print(lst_5[::1])

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
print([1, 2, 3] == [1, 2, 3])
# list({1, 2, 3})

'''
Леонид пошел в боулинг
На дорожке стоит n кеглей (пронумерованы от 1 до n слева направо)
Леонид сделал k бросков
Каждый из бросков сбивает кегли от l до r.
Определите, какие кегли уцелели после нападения Леонида
вход:
n  k
10 3

l  r
8 10
2 5
3 6

выход:
I.....I...
'''

'''
Богдан очень любит загадки
Богдан попросил своего друга Пашу
придумать шифр, чтобы затем его разгадать
Паша решил, что в качестве шифра взял целое
неотрицательное число со следующим свойством:
если выписать три любые идущие подряд цифры числа
то новое число, составленное из них будет делиться на три

Паша записал шифр на бумаге и разрезал на кусочки, в каждом кусочке по одной цифре
Хитрый Паша (хитрый) добавил туда лишние кусочки и перемешал

Богдан в шоке и его цель восстановить число

Вход:
1 2 3 0 0 0 0 0 0
Выход:
21021
'''

def func():
    pass
    # function body

# lambda arg1, arg2: function body
power = lambda x: x ** 2
# arr.map() arr.filter() arr.reduce() - в питоне это лямбда
lst = [1, 12, 56, 34, 128, 37]
new_lst = list(filter(lambda item: item % 2 == 0, lst))
new_lst_2 = list(map(lambda item: item % 2, lst))

from functools import reduce
new_lst_3 = reduce((lambda acc, item: acc + item), lst)

# itertools functools

same_parity = lambda x, y: 'same' if (x + y) % 2 == 0 else 'diff'
print(same_parity(5, 7))

x = lambda x: x.sort()[-1]
y = lambda x, f: sum(x) + f(x)

new_lst_4 = [lambda i = i: i * 10  for i in range(1, 11)]

hello = lambda: 'text'
print(hello())

# напишите функцию, которая принимает на вход координаты двух точек и выводит длину отрезка
# между этими точками

# мн-во хранит уникальные значения
set_1 = [1, 2, 3, 4, 5, 5, 5, 5]
set_1 = set(set_1)
set_1.discard(7)
# set_1.remove(7)
# set_1.pop(7) вернет значение
print(set_1)
print(len(set('qwertyyyyy')))
print('t' not in set('qwertyyyyy'))

set_2 = {1, 2, 3, 4, 5}
set_3 = {3, 4, 5, 6, 7}
set_4 = {2, 3, 5}
print(set_2 | set_3) # a.union(b)
# set_2 |= set_3
# print(set_2)
print(set_2 & set_3)
print(set_2 - set_3)
print(set_2 ^ set_3)
print(set_4 <= set_2)
print(set_4 <= set_3)

# напишите лямбда функцию, которая принимает на вход строку и возвращает количество
# уникальных в ней чисел
count_unique = lambda string: len(set(string.split(' ')))

# напишите функцию, которая принимает на вход строку с числами и для каждого числа определяет
# встречалось ли оно ранее 
# 1 2 3 2 3 4
# N N N Y Y N

# check_in_set = lambda st, x: 'Y' if x in st else 'N' 

# y_or_n = lambda string, f, st={}: ' '.join([f(st, i) for i in string.split(' ')])

# словари
dct = dict()
print(dct)
dct['key'] = 'value'
print(dct)

dct_2 = {'key': 'value'}
dct_3 = dict(key = 'value', key_2 = 'value2')
print(dct_3)
# dct_4 = dict([('k1', 'k2'), ('v1', 'v2')])
dct_4 = dict(zip(['k1', 'k2', 'k3'], ['v1', 'v2', 'v3']))
print(dct_4)
# print(dct_4['k4'])
print(dct_4.get('k4', 'def'))
# del dct_4['k4']
v_1 = dct_4.pop('k4', 'durak')
print(v_1)
print(dct_4)
# try:
#     x = 14
# except:
#     print('durak')
for key in dct_4:
    print(key, dct_4[key])

print(dct_4.keys())
print(dct_4.values())
print(dct_4.items())

# for key, value in dct_4.items():

# print([1, 2] == [1, 2])

'''
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. 
Все слова в словаре различны.
Для слова из словаря, записанного в последней строке, определите его синоним.
вход:
3
Hello Hi
Bye Goodbye
List Array
Goodbye

выход:
Bye
'''
def find():
    dictionary = {key: value for key, value in [input().split() for _ in range(int(input()))]}
    dictionary.update({value: key for key, value in dictionary.items()})
    return dictionary[input()]

# print(find())
'''
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
вход:
1
apple orange banana banana orange
выход: banana
'''
def count_of_words():
    count = int(input())
    dictionary = [i.lower() for i in input().split() for _ in range(count)]
    print(dictionary)

count_of_words()

'''
r - read
w - write
x - execute

на вход указывается количество файлов N
в N строках указывается имя файла + права доступа к нему

затем указывается M - кол-во запросов на доступ к файлам
в M строках указывается имя файла + планируемая операция

вход:
3
main.py rw
maxim.js wx
masha.py rwx
3
read main.py
read maxim.js
read write py.py

выход:
ok
access denied
file is not exist
'''

# all()
# any()

'''
функция принимает на вход нечетное число N
реализуйте вывод снежинки размером NxN по образцу
n = 5
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *

n = 7
* . . * . . *
. * . * . * .
. . * * * . .
* * * * * * *
. . * * * . .
. * . * . * .
* . . * . . *

n = 3
* . *
. * .
* . *
'''
