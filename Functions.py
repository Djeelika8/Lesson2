
def is_prime(num):               # Функция Является ли ПРОСТОЕ число
    if num == 1:
        return False
    return len([i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]) == 0



def is_prime_(num):              # Функция  Является ли ПРОСТОЕ число
    if num == 1:
        return False
    elif [i for i in range(2, int(num ** 0.5) + 1) if num % i == 0]:
        return False
    else:
        return True


