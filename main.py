
"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


print ('Вне условий')



promt = ('Витязь на распутье')
'Налево (L) пойдешь, вольну-волю обретешь...'
'Направо (R) пойдешь, коня потеряешь...'
'Прямо (F) пойдешь, сыт и весел будешь...'
print (promt)
choice = input('Куда идем (L, R или F): ')
if choice == 'L' or choice == 'l':
    print ('Поздравляю свободного гражданина!')
elif choice == 'R' or choice == 'r':
    print ('Мне жаль Вашего коня, рыцарь!')
elif choice == 'F' or choice == 'f':
    print('Раз пошла такая пьянка, режь последний огурец!')
else:
    print('Давай уже куда-нибудь пойдем!')

hour = 13 # 0 - 213
# если время между 7 и 11 утра, то доброе утро
# если время между 12 и 17 дня, то добрый день
# если время между 18 и 22 вечера, то добрый вечер
# иначе - доброй ночи

hour = input('Сколько ейчас времени?  ')
hour = int(hour)
if hour > 23:
    hour = 23
if hour < 0:
    hour = 0 # проверка корректности4
# if hour >= 7 and hour < 12:
if  7 >= hour < 12: # упрошенное
     print ('Доброе утро!')
elif hour >= 12 and hour < 17:
    print ('Добрый день!')
elif hour >= 17 and hour < 23:
    print ('Добрый вечер!')
else:
    print ('Доброй ночи!')


a = 3
b = 5

print ('До:')
print ('a = ', a, 'b = ', b)

a, b = b, a # swap

print ('После:')
print ('a = ', a, 'b = ', b)

# Iterable object
# len() - сколько элементов в объекте

a = 123456

length = len (str(a))
print (length)


word = input('Введите слово: ')

lenth = len (str(word))

if lenth > 3:
    print ('Ваше слово ','"'+word+'"', 'больше 4 символов')  #через запятую с пробелом, через "плюс" без пробела
else:
    print ('Ваше слово ',word, 'меньше 4 символов')

"""
from collections import defaultdict
from itertools import count
from re import match
from selectors import SelectSelector
from tkinter.font import names

word1 = 'пришел'
word2 = 'увидел'
word3 = 'победил'
word4 = '27\xb0C' #ASCII 16-ричный код символа

# Help on built-in function print in module builtins:
# print(*args, sep=' ', end='\n', file=None, flush=False)

# Формат вывода
# \  -  начало "escape sequence"
# \n -  перевод строки
# \t - табуляция
# \xFF -  #ASCII 16-ричный код символа
# \u - вывод символа по 4-знакоместам символам unicode

print ("Концерт группы \"Кино\"") #экранирование символа ["]
print ('Путь к файлу C:\\Program Files\\Users') #экранирование символа [\]

print (word1, word2, word3, sep=', ')
       #end=' -> ')

"""

# Формат вывода 2
name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
weight =90.366666


# 1 способ (плейсхолдеры)
print ('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

# %s -symbol
# %d -digit
# %f -float


# 2 способ
print ('Имя: {}, E-mail: {}, Возраст: {}' .format (name, email, age))



# 3 способ
print(f'Имя; {name} ,E-mail: {email}, Возраст: {age}, вес: {weight:.3f}')
#print(f'Имя: {name}, E-mail: {email}, Возраст: {age}, Вес: {weight.3f}')

# 1 способ (плейсхолдеры)
print ('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

# %s -symbol
# %d -digit
# %f -float


# Формат вывода 2
name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32
weight = 92.633366254

# 1 способ (плейсхолдеры)
# %s - string
# %d - digit (целое число)
# %f - float
print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

# 2 способ
print('Имя: {}, E-mail: {}, Возраст: {}'.format(name, email, age))

# 3 способ (самый популярный с версии 3.6)
print(f'Имя: {name}, E-mail: {email}, Возраст: {age}, Вес: {weight:.3f}')



 # решить квадратное уравнение

# ах + bx +c = 0
# Определить коэффициенты a, b,c

a = float(input('введите a:  ')),
b = float(input('введите b:  ')),
с = float(input('введите c:  '))


if a != 0:
    # Дискриминант

    d = b ** 2 - 4 * a * c
    # Вычисление корней
    if d < 0:
        print('Уравнение не имеет корней!')
    elif d == 0:
        x = -b / (2 * a)
        print(f'Корень уравнения: {x:.2f}')
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        print(f'Корни уравнения:\n\t\tx1 = {x1:.2f}\n\t\tx2 = {x2:.2f}')
else:
    print('По условию a не равно нулю!')



# Циклы
# while
# for
counter = 0 # обнуляем счетчик

# цикл изх пяти итераций

while counter < 5:
    print (f'Итерация номер: {counter +1}')
    counter +=1 #инкремент в краткой записи
    print(f'Итго в коунтер уже {counter}')

print ('обратный отчет')


counter = 5 # выставляем счетчик

while 0 < counter <= 5:
    print (f'Итерация номер: {counter -1}')
    counter -=1 #инкремент в краткой записи
    print(f'Итго в коунтер уже {counter}')



# Циклы:

# word =''
# := [моржовый оператор] присваивает в тип в контексте

while len(word := input('Введите слово не короче трех символов: ')) <= 3:
    print(f'Слово: "{word}" слишком короткое.')
print (f'Вы ввели слово: "{word}"')

# Цикл до ввода пустой строки
# без "моржа" -  :=

word =input('Введите слово: ')
while word != '':
    print(f'Слово: "{word}"')
    word = input('Введите слово: ')
print ('Пустая строка введена')



while (word := input('Введите слово: ')) !='':
    print(f'Вы ввели слово: "{word}"')
print ('Вы не ввели слово')



# num = 3 # число, которое нужно угадать
num = 3
flag = True
var = ''

while flag:
    var = int(input('Ваше значение: '))
    if var == num:
        print('Ура, угадал!')
        flag = not flag
    elif var > num:
        print ('Число больше загадонного!')
    else:
        print ('Число меньше загадонного')
print ('Приходи еще!')




# подбираем кандидата по росту

height = int(input('Введите рост: '))

while (150 >= height <= 180):
    print(f'Рост кандидата {height} не подходит')
    height = int  (input('Введите рост'))
print ('Кандидат выбран')



# match - case (3.10 >)

print ('Возможные ходы: \n\tL - влево\n\tR - вправо\n\tF - прямо, \n\tQ -выход')

while True:
    ch = input ('Ваш выбор:')
    match ch:
        case 'L' | 'l' | 'Д' |'д':
            print ('Свернули налево')
        case 'R' | 'r' | 'К' |'к':
            print ('Свернули направо')
        case 'F' | 'f' | 'А' |'а':
            print ('Пошли прямо')
        case 'Q' | 'q' | 'Й' |'й':
            print ('До свидания!')
            break


# ключевое слово in

word = 'поток'

if 'ток' in word:
    print ('есть!')

# цикл for (для итерируемых объектов)
# for <переменная> in intertable
# команды

# word ='поток'

# for ch in word:
#    print(ch)

for i in range(2, 13, 2):
    print(i)



#интерпретатор range (start, stop, end)

for i in range (1,101):
    if i% 10 ==5:
        if i==15:
            continue
        print(i)


# min, max, average, sum
N = 5
total = 0
min_val = float ('inf') # + бесконечность
max_val = float ('-inf') # - бесконечность
prod = 1

for _ in range(10):
    num = int(input('Введите число:  '))
    if num < min_val:
        min_val = num
    if num >max_val:
        max_val = num
    total +=num
    prod *= num
    average = total / N

print(f'Сумма: {total}')
print(f'Ср. арифметическое: {average}')
print(f'Произведение: {prod}')
print(f'Минимум: {min_val}')
print(f'Максимум: {max_val}')
120
#factorial

N=3

fact = 1
for i in range(1, N+1):
    fact *= i
print (fact)


# Вложенные циклы

for i in range (1, 10):
    for j in range (1, 10):
        print (f'{i}*{j} = {i*10}', end='\t')
    print()



# подбираем кандидата по росту

height = int(input('Введите рост: '))

while (150 >= height <= 180):
    print(f'Рост кандидата {height} не подходит')
    height = int  (input('Введите рост'))
print ('Кандидат выбран')



# min, max, average, sum
N = 5
total = 0
min_val = float ('inf') # + бесконечность
max_val = float ('-inf') # - бесконечность
prod = 1

for _ in range(10):
    num = int(input('Введите число:  '))
    if num < min_val:
        min_val = num
    if num >max_val:
        max_val = num
    total +=num
    prod *= num
    average = total / N

print(f'Сумма: {total}')
print(f'Ср. арифметическое: {average}')
print(f'Произведение: {prod}')
print(f'Минимум: {min_val}')
print(f'Максимум: {max_val}')



#  Подбор кндидатов по росту от 150 до 180, сигналом остановки является ввод - 1

total_people = 0
success_people = 0
min_val = float('inf')
max_val = float('-inf')

while (num :=input('Введите рост: ')) !=-1:
    if 150 <= int(num) <= 180:
        success_people +=1
        if (num) < min_val:
            min_val = num
        if (num) > max_val:
            max_val = num
total_people +=1




#  Коллекции  (set, list, dict, tuple)
#  Множества

s = set() #пустое множество

s = {3, 5, 7}
print(type(s)) #класс

print(s) # неупорядоченное множество (произвольный порядок вывода, исключаются повторения)

for item in s:
    print(item)

print (f'Число элементов в: S = {len(s)}')



if '3' in s:
    print('Присутствует число 3')
else:
    print('не присутствует')



s = set() #пустое множество

s = {'3', '5', '7'}
print(type(s)) #класс

print(s) # неупорядоченное множество (произвольный порядок вывода, исключаются повторения)



# удаление из множества

s.add ('3')
print(s)
s.remove('5')
print(s)
s.discard ('7')
print(s)
temp = s.pop
print(temp)
#s.clear

print (dir(s))

# игра в "города"
s = set()

city = input('Назовите город')

while (city :=input('Назовите город: ')) !="":
    if city in s:
        print('Такой город уже был')
    else:
        s.add(city)
print(f'Итого было названо: {len(s)} городов:')
for item in s:
    print('\t', item)



# Сдаем карты

cards = {3, 7, 'туз', 'король', 'дама','валет'}

while cards: # пока в колоде есть карты
   print(cards.pop())

# for item in cards:
#     if item !=""

# операции над картами

a = {1, 2, 3}
b = {1, 2, 4,}

# объединение множеств
#  c = a.union(b)
c = a | b
print(c)

# персечение

# c = a.intersection(b)
c = a & b
print (c)


# PEP8 - правила именования
# переменные используются только строчные, английские, можно использовать нижнее подчеркивание,
# не использовать c, l, O, I (из за схожести с другими символами)

c = b.difference(a)
c = b - a
print (c)

# симметричная разность

c = b.symmetric_difference(b)
c = b ^ a
print (c)

# Строки (итерируемый объект, "коллекция" (помним, что Python нетипизированный язык)

# ch ='а' эквивалентно ch ="а"

s = ''

s += 'Привет'

print(s)
print(id(s))
print(s)
print(id(s))

s += ', Дмитрий'
print(s)
print(id(s))




# индекс строки
s = 'Python'
print(s[0])

# s[3] = 'у' - error (immutable)

print(s[-5])
# индекс может быть отрицательным (с конца)

print(f'Длина слова: {len(s)}')
print(s[-1])

# Задача: посчитать гласные в строке

s = 'Язык python'

v = 0 # число гласных

for ch in s:

   #if ch in {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'Я', 'o','y'}:
   if ch in 'аеёиоуыэюяЯyo':
        v +=1

print(f'Число гласных в строке: "{s}" = {v}')


# Задача: исправить букву в слове "сабака"
s = 'сабака'

res = ''

for i in range(len(s)):
    if i == 1: # я знаю, что по индексу 1 надо написать 'o'
        res += 'о'
    else:
       res += s[i]

print (res)

# две удобные функции
# ord (символ) - возврвращает код символа в unicode
# chr (код) - возвращает символ Unicode по коду

# таблица символов '°, ○'

u = '\u2603'

print(u)

print(chr(9731))

print(chr(10000))

print(chr(128514))
print(chr(9760))
print(chr(128077))
print(chr(128586))
#ord(☠)
#ord(👍)
#ord(🙊)


s = set()
word = input ('Введите фразу для шифрования: ')

for ch in word:
    s.add(ord(ch))

print(s)

#Расшифровываем

###

print(dir(s))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop','remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

phrase = input('Введите фразу: ')

print(phrase.lower())
print(phrase.upper())
print(phrase.capitalize())
print(phrase.title())

print('Ура! ' *3)
print('Телевизор'.count('е'))
print('Pytyhon'.index('h'))  



word = input ('Введите фразу для модификации: ')




for i in range (len(word)):
    print(word[i -1] * (i), end='')


print('\t')

for ch in word:
    i = word.index(ch) + 1
    print (ch * i, end='')

print('\t')

print(word.strip('р'))



# 30/06/2025


# Строки (immutable, iterable)
# Шифр Цезаря

# создаем алфавит
alphabet = 'абвгдеёжхзийклмнопрстуфчцчшщъыьюя'
## alphabet_up += alphabet.upper()

# Получачем входеные данные
message = input ('Введите строку: ').strip()#.lower() # цепочка вызова методов
key =int(input('Введите ключ: '))
# инициализируем пустую строку для результата
encrypted = ''

# перебираем каждый символ в сообщении
for letter in message:
    # проверяем является ли символ буквой из алфавита
    if letter in alphabet:
        # находим место буквы в алфавите
        t = alphabet.index(letter)
        # Вычисляем новую позицию с учетом сдвига
        new_key = (t + key) % len(alphabet)
        # добавляем зашифрованный символш
        encrypted += alphabet[new_key]
    else:
        # если символ не буква, оставляем без изменений
        encrypted += letter

print('Зашифрованное сообщение: ', encrypted)

print(dir(message))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
# 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

s = 'смотреть'

if s.lower().startswith('смо'):
    print('Да')


if s.endswith('еть'):
    print('Да')

# 1 метод find ("подстрока")
# 2 метод find ("подстрока",  стартовая позиция)
# 3 метод find ("подстрока", от [позиция] до [позиция])

ss = 'Смотреть, вертеть, видеть'

index = ss.find('ь') # ищем сначала строки
print(index)
index = ss.find('ь', __start = 10)  # ищем с позиции 10
print(index)



s = 'синхрофазотрон'

# сколько букв "о" и их позиция

if ch in s:
    count = s.count(ch)
    print (f'Буква {ch} встречается в слове "{s}" {count} раз')
    print ('Её позиция/позиции:', end = '  ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        
        

else:
    print(f'Буквы {ch} нет в слове "{s}"')

# метод replace ('что' на 'что') - полная замена


s = 'тиливизор'

print (s.replace('и', 'е',2))


# split и join - важные методы

#slice  Срез (у строки и других коллекций, кроме set)
#[начало:окончание:шаг]

s = 'добрый день'

print (s[:6]) # print (s[0:6:1]) от начала и до заданного индекса (не включая)
print (s[7:]) # print (s[7:11:1]) от указанного индекса и до конца
print (s[3:8]) # от и до
print (s[:-6]) # c начала и до 6 позиции от конца
print (s[::-1]) # в обратную сторону

s = input('Введите строку: ') #потоп

if s.lower() == s[::-1].lower():
    print(f'Строка "{s}" - палиндром!')
else:
    print(f'Строка "{s}" - не палиндром!')

a = 'Python'

print(a[:522])


s = 'Дорог Рим город или дорог Миргород' # + U *
# Миргород нам дорог ....

print(f'{s[26:50]} нам {s[20:26]}... {s[20:26]}...')

temp =s.lower()
city = temp[:5][::-1]
res = city + '' + temp[6:][::-1] +  city

print(res.title())




# Списки (list)

s = {'3','4','5'}

lst1 = list(s)

print(lst1)

lst2 = list(range(1,11))

print(lst2)

#lst = [] # пустой список
# lst = list() # можно так

lst = list ('Python')
print(lst)


lst = lst*3
print(type(lst))
print(lst)

lst = ['s']*10
print(lst)

lst =[1, 2 ,3]
print(lst[:2])

# Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
# dir([])
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



s1 = [1, 2, 3]
s2 = [4, 5, 6]
print(s1+s2)

s1[1] = 22
s2[0] = 44
print(s1+s2)

lst = list(range(10))

print(lst)

slice = lst[:: 2] #slice = lst[:len(lst): 2]
print(slice)
for item in lst:
    print(item, '-', item ** 2)

for item in range(0, len(lst), 2):
    print(list[item], '-', lst[item] ** 2)

lst = [1, 7, 3, 5, 6, 4, 2]
lst.sort
# lst.reverse()

print(lst)


a = ['a', 'b', 'c']
b = a
b.append('d')  # b += ['d']

print(id(a))
print(id(b))
print(a)
print(b)

# потому, что b ссылка на a, но

a = ['a', 'b', 'c']
b = a.copy()
b.append('d')  # b += ['d']

print(id(a))
print(id(b))
print(a)
print(b)




lst = []

while (item := input('Введите название ингридиента:  ')) !='':
    lst.append(item)

print(f'У нас есть {len(lst)} ингридиентов: ')
lst.sort()
for i in range(len(lst)):
     print(f'\t{i +1}. {lst[i]}')




# имитация стека

N = 5 #глубина стека

lst = []
for i in range(N):
    print(f' Кладем книгу {i + 1} в стопку.')
    lst.append( i + 1)

print('---')

while lst:
    item = lst.pop()
    print(f'Берем книгу {item} из стопки.')



#Списки
#Создание абревиатур

lst =[]

while (word:= input('Введите слово: ').strip()) !='':  #.capitalize(): или upper ниже
    lst.append(word[0].upper())

print(lst)

print('Получилась аббревиатура', end =': ')
print (*lst[:10], sep='') # только первые 10 букв




# Корртеж (tuple, immutable)

BLACK = (0, 0, 0)
empty = () # tuple()
one =(1,) #добавить единицу в кортеж, запятая после символа обязательна
temper = 36, 6 #кортеж
s = 'Python'
t = tuple(s) + ('.',)
print(t)

# dir(())
#['count', 'index']

cards = [(7, 'червей'), ('туз', 'пик')]
print((1, 2) < (1, 3))

a = 3
b = 4
a, b = b, a


channels = ['red', 'green', 'blue']

r, g, b =channels #распаковка

print (r, g, b)

r, *g = channels # частичная распаковка

print (r, g)

r, *channels = channels

print(channels)

a, b = input(), input()
print(a, b)




# Студент и средний балл

N = 3
students = []

for i in range(N):
    student, average = input('ФИО: '), float(input('Ср. балл: '))
    students.append((student, average))

for st in students:
    student, average = st #  распаковка
    print('Студент: ', student)
    print('Средний балл: ', average)
    


# help(sorted)
# Help on built-in function sorted in module builtins:
# sorted(iterable, /, *, key=None, reverse=False)
#    Return a new list containing all items from the iterable in ascending order.
#    A custom key function can be supplied to customize the sort order, and the
#    reverse flag can be set to request the result in descending order.

s = {'Крутов', 'Селезнев', 'Митрофанов',}
r = True

# 1- способ
lst = list(s)
lst.sort()

print(*lst, sep=', ')


# 2-й способ
lst = sorted(s, reverse=r)
print(*lst, sep=', ')

# help(enumerate)
# Help on class enumerate in module builtins:
# class enumerate(object)
#  |  enumerate(iterable, start=0)
#  |
#  |  Return an enumerate object.
#  |
#  |    iterable
#  |      an object supporting iteration
#  |
#  |  The enumerate object yields pairs containing a count (from start, which
#  |  defaults to zero) and a value yielded by the iterable argument.
#  |
#  |  enumerate is useful for obtaining an indexed list:
#  |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |
#  |  __class_getitem__(...)
#  |      See PEP 585
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs)
#  |      Create and return a new object.  See help(type) for accurate signature.

fio = {'Крутов', 'Селезнев', 'Митрофанов',}


for item in enumerate (fio):
    print (item)

for i, v in enumerate (fio): #распаковка функции enumerate
    print ((f'{i+1}. {v}.'))




#Методы строки - split() и join()
# только со строками!

text = 'один два три четыре'

lst = text.split()

print(lst)

ip = '192.168.1.31'
lst = ip.split('.')
print(lst)

text2 = ' - и так же: '.join(lst)
print(text2)

# убрать все пробелы
text = '   P   y        t h    o n     '
res = ''.join(text.split())
print(res)



# Домашнее задание

stop_list = []

# убррать из исходного текста стоп - слова
# отсортировать и пронумеровать, вывести в колонку разрешенные слова

stop_words = ['ну', 'типо', 'короче', ]
temp = set()
res = []
message = input('Введите сообщение: ')
lst = message.split() #все слова
for item in lst:
    if item not in stop_words:
        temp.add(item)
res + sorted (temp)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')



# Фраза: ну?, я типо, вообще: короче, не понимаю этот язык!
commas = (',', '!', '.', '?', '-', ':')
stop_words = {'ну', 'типо', 'короче', 'не'}
message = input('Введите сообщение: ')
for z in commas:
    message = message.replace(z, '')
lst = message.split()  # все слова
res = sorted(set(lst) - stop_words)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')



#Списочные выражения (list comprehension)

squares = []
for i in range(10):
    squares.append(i**2)

print(*squares,sep=', ')

# короткий вариант

squares = [i ** 2 for i in range(10)]  #всё в одну строку, 1. - ЧТО попадет в список, 2. - ПО КАКОЙ ЗАКОНОМЕРНОСТИ

print(*squares,sep=', ')


squares = [i ** 2 for i in range(10) if i % 2 == 0]  #всё в одну строку, 1. - ЧТО попадет в список, 2. - ПО КАКОЙ ЗАКОНОМЕРНОСТИ, 3. отбор условий (только четные)

print(*squares,sep=', ')

# произведение i и j

print([i * j for i in range(3) for j in range(3)])


n = '500 600 700 800 900 1000'
approved =[500, 800]
a = ([int(i)  for i in n.split() if int(i) in approved])
# действия со списком а
print(a)

text = 'Списочные выражения (list comprehensions) в Python действительно могут повысить эффективность кода при создании новых списков, особенно по сравнению с традиционными циклами. Они обеспечивают более компактный и, часто, более быстрый способ генерации списков'

res = (a for a in text.split() if (text.index(a) +1) % 3 ==0) # в квадратных скобках - list comprehension, в круглых - tuple!
print(res)

res = [a for a in text.split() [2::3]]
print(res)

# Вложенные списки

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9], # в последней строке "висячая запятая" считается хорошим тоном в программировании
]
print(matrix)

for row in range(3):
    for col in range(3):
        print(matrix[row][col])

for row in range(len(matrix)):              # обход 2-мерного списка произвольного размера (матрицы)
    for col in range(len(matrix[row])):
        print(matrix[row][col])

matrix = [[1] * 3 for _ in range(3)]        # _ перед in, необъявленная переменная (нигде более не используется)
print(matrix)

count = 1
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row][col] = count
        count += 1
print(matrix)

start = 1
N = 4

for i in range(N):
    table = []
    for j in range(start, start +N):
        table.append(j)
    matrix.append(table)
    start += N

print(matrix)


matrix = [[i+j for j in range(N)] for i in range(1, 10, 3)]

print(matrix)



# словари
# нет индекса, но есть ключ

# пустой словарь
# 1. d = {}
# 2. d = dict()

d = {                           #можно в одну строку, но неудобно когда много значений
    'table': ['таблица', 'стол'],
    'well': ['хорошо','колодец','скважина'],
    'chair': 'кресло',
    'apple': 'яблоко',
    1: 'один',                  # к ключу нет требований типизации, может быть любым  int, str, float, complex
    (55.75, 37.5): 'Москва'
}

print(d['table'])
print(d['well'][0])

print(d[(55.75, 37.5)])

# добавление ключа и значения
d['plum'] = 'слива'
print(d['plum'])

# удаление ключа
del d['plum']

# добавление ключа и значения - списка, чтобы можно было добавить еще
d['plum'] = ['слива']
print(d['plum'])

d['plum'].append('красная слива')
print(d['plum'])

# добавление значения в существующий ключ (проверка наличия ключа)
if type(d['well']) == list:
    d['well'].append('буровая скважина')
print(d)

for key in d:
    print(key, '-->', d[key])

# dir({})
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


deleted_item =d.pop('apple')
print('Удалили элеменет словаря ', deleted_item)


for key in d.keys(): #d.keys()
    print(key, '-->', d[key])


# перебор всех значений
for value in d.items():
    print(value)

print(d.keys())  # список ключей
print(d.values()) #список значений

# перебор всех пар "ключ, значение"
# for k, v in d.items():
#    print(k, v)

print('Есть ли стул в словаре')
if 'стул' in d.values():
    print('Да есть')
else:
    print('Стула нет!')

print('Доступ к несуществующему ключу без "исключений"')
pear = d.get('pear', 'Груши нет')
# if pear - дальнейшая обработка события
print('Где груша: ', pear)

"""

# Словари
# Частотный анализ

text ="""Две экзопланеты превзошли Землю по жизнепригодности.
Астрономы сравнили далекие миры с нашей планетой по разным критериям и сделали неожиданное открытие.
Две экзопланеты превосходят Землю по степени пригодности для жизни, рассказали астрономы в своей недавней статье.
Они разработали специальный метод оценки миров и применили его для сравнения множества известных примеров. Напомним,
открыто уже без малого 6 тысяч миров в других звездных системах.
"""
res ={}
commas = (',', '!', '.', '?', '-', ':' )

for x in commas:
   text = text.replace(x, '')

lst = text.lower().split()

for item in lst:
    if item in res:
        res[item] +=1
    else:
        res[item] = 1
print(res)
print('Частотный анализ слов текста')
for k, v in res.items():
    print(k, v)




