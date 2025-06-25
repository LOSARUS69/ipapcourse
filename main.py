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
"""
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



