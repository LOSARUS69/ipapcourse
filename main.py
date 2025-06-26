# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""

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

print (word1, word2, word3, sep=', ', end=' -> ')

"""

# Формат вывода 2
name: str = 'Игорь'
email: str = 'aaa@bbb.ru'
age: int = 32
weight: float = 90.366666


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