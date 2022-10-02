
def is_prime(num):               # Функция Является ли ПРОСТОЕ число
    if num == 1:
        return False
    return len([i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]) == 0


###-----ИЛИ-----------------------
def is_prime_(num):              # Функция  Является ли ПРОСТОЕ число
    if num == 1:
        return False
    elif [i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]:
        return False
    else:
        return True

###-------по другому------------------------
# объявление функции
def is_prime(num):               # Функция Является ли ПРОСТОЕ число
    if num == 1:
        return False
    elif [i for i in range(2, num // 2 + 1) if num % i == 0]:
        return False
    else:
        return True

# объявление функции
def get_next_prime(n):            # Функция следующее ПРОСТОЕ число
    n = n + 1
    while is_prime(n) == False:
        n = n + 1
    return n

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

### --------------------------------
def is_password_good(password):     # Функция Является ли ХОРОШИЙ ПАРОЛЬ
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

# ПРИ перемножении логики, т.е. ч/з and, то True выйдет, если все показатели будут True
# иначе выйдет False

###### -------------------------------------------------------

# Палиндром – это строка, которая
# читается одинаково в обоих направлениях
#
# При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.


def is_palindrome(text):              # Функция Является ли ПАЛИАНДРОМ
    symbols = '!,./|\\:;@#%()^"\'\{\}\*_-+<> ?$`'
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

##################==============================
#   ------------   ДЕЛИТИЛИ
# Если число очень большое, то лучше проверять половину числа + само число
# А еще лучше корень числа range(1, int(num ** 0.5) + 1)

# объявление функции
def get_factors(num):                 # СПИСОК ДЕЛИТИЛИТЕЛЕЙ
    return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]

def number_of_factors(num):            # количество  ДЕЛИТИЛИТЕЛЕЙ
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
########--------------------------
# Поиск Символа
def find_all(target, symbol):  # ПОИСК ВСЕХ символов
    s = []
    indx = 0
    n = target.count(symbol)  # посчитали сколько всего символов

    for i in range(n):
        x = target.find(symbol, indx)  # начинаем искать с индекса 0
        s.append(x)
        indx = x + 1  # переходим к следующему индексу

    return s

######### =======================================================================

# Правильная скобочная последовательность (Объектное Ориентирование)
#
# Примечание 1. Правильной скобочной последовательностью
# называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка.

import time
start_time = time.time()

# объявление функции
def is_correct_bracket(text):    # СКОБОЧНАЯ ([{)]} последовательность
    steck =[]
    for i in text:
        if i in '([{':
            steck.append(i)
        elif i in ')]}':
            if not steck:       # выйдет True если steck пустой
                return False

            br = steck.pop()     # последний элемент списка steck удаляется и сохраняется в br
            if br == '(' and i == ')':
                continue              # переходим на следующую итерацию for
            if br == '[' and i == ']':
                continue              # переходим на следующую итерацию for
            if br == '{' and i == '}':
                continue              # переходим на следующую итерацию for
            return False
    return not steck             # выйдет True если steck пустой


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

print((time.time() - start_time), 'секунд')
# ======================================================================

#####    Панграммы

# Панграмма – это фраза, содержащая в себе все буквы алфавита.
# Обычно панграммы используют для презентации шрифтов,
# чтобы можно было в одной фразе рассмотреть все глифы.

def is_pangram(text):                         # функция для определения Панграммы
    stek = []
    alfavit = ['32', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122']
    text = text.lower()
    for i in alfavit:                       # перебираем алфавит
        if chr(int(i)) not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

# -----------ИЛИ-----------------------------------------

def is_pangram(text):                     # функция для определения Панграммы
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:                       # перебираем буквы Алфавита
        if i not in text.lower():         # если буква на содержится в Тексте (с нижним регистром)
            return False
    return True

################  ===================================================
# ##     Искомый месяц
#
# Напишите функцию get_month(language, number),
# которая принимает на вход два аргумента
# language – язык ru или en
# number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

# объявление функции
def get_month(language, number):
    daysru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    daysen = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return daysru [number-1]
    return daysen[number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))


# --------или  ЧЕРЕЗ СЛОВАРИ----------------------------

def get_month(language, number):
    d_ru = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
        7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
    d_en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june',
        7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    if language == 'ru':
        return d_ru[number]
    else:
        return d_en[number]

################  ===================================================