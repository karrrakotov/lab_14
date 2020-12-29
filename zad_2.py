#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

#   Напишите программу, которая будет генерировать матрицу из
#   случайных целых чисел. Пользователь может указать число строк и столбцов, а также
#   диапазон целых чисел. Произведите обработку ошибок ввода пользователя.

if __name__ == '__main__':
    try:
        import random
        strings = int(input("Введите кол-во строк: "))
        columns = int(input("Введите кол-во столбцов: "))
        start_range = int(input("Введите начало диапазона целых чисел: "))
        final_range = int(input("Введите конец диапазона целых чисел: "))

        lst = [[randint(start_range, final_range) for i in range(strings)] for j in range(columns)]
        for i in lst:
            print()
            for j in i:
                print(j, end=" ")
    except ValueError:
        print("Ошибка, повторите снова!")
