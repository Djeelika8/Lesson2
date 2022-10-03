# !!!!!!   Системы счисления

def poisk_chisla(n, base):  # ПЕРЕВОД в ДЕСЯТИЧНУЮ
    st = 0  # разряд для возведения в степень
    num = 0  # итоговое число
    while n > 0:
        digit = n % 10  # добыли последнюю цифру
        num = num + (digit * base ** st)
        n //= 10  # отщипнули последнюю цифру
        st += 1
    return num


base = int(input('введите основание введенного числа:  '))  # Когда ЗНАЕМ основание
sm = 0
for i in range(4):
    n = int(input('введите число для перевода его в 10-тичную систему: '))
    num = poisk_chisla(n, base)  # складываем яблоки, груши и т.д.
    print(num)
    sm = sm + num
print(sm)

# ---------------------------------------------------------------------------

def poisk_chisla10(n, base):  # ПЕРЕВОД в ДЕСЯТИЧНУЮ
    st = 0  # разряд для возведения в степень
    num = 0  # итоговое число
    while n > 0:
        digit = n % 10  # добыли последнюю цифру
        num = num + (digit * base ** st)
        n //= 10  # отщипнули последнюю цифру
        st += 1
    return num


spisok = [int(input('введите число для перевода его в 10-тичную систему: ')) for _ in
          range(int(input('сколько чисел? ')))]
rr = int(input('чему должно быть равно?: '))
for base in range(2, 33):  # НЕ знаем основание. Перебираем
    sm = 0
    for j in range(len(spisok)):
        num = poisk_chisla10(int(spisok[j]), base)  # складываем яблоки, груши и т.д.
        sm = sm + num
    if sm == poisk_chisla10(rr, base):  # проверяем равно ли....
        print('Нашли Основание!!!', base)
        break
# ____________________________________________________________________________________________
# !!!!!   Перевод чисел из десятичной системы счисления в ЛЮБУЮ другую

def convert_chisla(n, base):  # ПЕРЕВОД в ЛЮБУЮ систему_ подаем основание числа и число.
    str_num = ''
    s16 = ['A', 'B', 'C', 'D', 'E', 'F']
    while n > 0:
        if 15 >= n % base > 9:
            str_num = str(s16[n % base - 10]) + str_num
        else:
            str_num = str(n % base) + str_num
        n = n // base
    return str_num


chislo = int(input('введите число: '))
base = int(input('в какую систему перевести, введите основание: '))
print(convert_chisla(chislo, base))
# ___________________________________________________________________________________
# ======================================================================================
# !!!     Функция для cоздания МАТРИЦЫ

def create_matrix(rows, cols):  # Создание Матрицы 2x3 [['11', '22', '33'], ['44', '55', '66']]
    return [[input() for _ in range(int(cols))] for _ in range(int(rows))]


def print_matrix(matrix):  # ВЫВОД МАТРИЦЫ поэлементно/построчно
    for row in matrix:
        print(*row)
# или сразу [print(*row) for row in matrix]

n, m = input(), input()
print_matrix(create_matrix(n, m))

# 11 22 33
# 44 55 66
# --------------------------------------------
# Для считывания матрицы из n строк, заполненной числами,
# удобно использовать следующий код:

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

print_matrix(matrix, n)

# ------------------------------------------------------------
# Функция для вывода ЛЮБОЙ МАТРИЦЫ
def print_matrix(matrix, n, m, width=2):
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(width), end=' ')
        print()


print_matrix(matrix, n, m)
# -------------------------------------------------------------