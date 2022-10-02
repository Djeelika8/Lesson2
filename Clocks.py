

from time import sleep

for hours in range(24):                  # в сутках 24 часа
    for minutes in range(60):            # в нутри каждого часа 60 минут
        for seconds in range(60):        # в нутри каждой минуты 60 секунд
            print(hours, ':', minutes, ':', seconds, end='')
            sleep(1)                     # задержка при выводе на 1 секунду
            print(end='\r')              # удаляем предудущий вывод строки
