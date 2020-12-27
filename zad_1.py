#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
#   Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
#   соединение, строк. В остальных случаях введенные числа суммируются.

if __name__ == '__main__':
    first_number = input('Введите первое число: ')
    second_number = input('Введите второе число: ')
    try:
        if int(first_number) and int(second_number):
            result = int(first_number) + int(second_number)
            print(f"Введены два числа, сумма: {result}")
    except ValueError:
        print(f"Введены не числа, произведена конкатенация, результат: {first_number + second_number}")
