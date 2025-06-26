
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
from re import match
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

"""

#интерпретатор range (start, stop, end)

for i in range (1,101):
    if i% 10 ==5:
        if i==15:
            continue
        print(i)











