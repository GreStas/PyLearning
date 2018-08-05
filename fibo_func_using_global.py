#!/usr/bin/env python3

fibos = [1,1,]

def fibo(n):
    """ Возвращает число Фибоначи по его порядковому номеру (начиная с 1
    Используется шаблон проектирования Singleton для кеширования
    уже посчитанных значений в глобальном списке fibos.
    """
    global fibos
    if n > len(fibos):
        # надо добавить в список новые элементы
        for i in range(len(fibos),n):
            fibos.append(fibos[i-2] + fibos[i-1])
    return fibos[n-1]

for i in range(1,8):
    print("{}/{}:{}".format(i, len(fibos), fibo(i)))

i = 100
print("{1}/{2}:{0}".format(fibo(i), i, len(fibos)))

i = 10;
print("{1}/{2}:{0}".format(fibo(i), i, len(fibos)))

l = len(fibos)
if l < 20:
    print(fibos)
else:
    print("Sorry, list is too long ({}) to print whole.".format(l))

