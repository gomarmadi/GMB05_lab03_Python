#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m=8, max_value=21):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-10) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(-10, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%5.1f\t" % j, end='')
        print()


# функция для нахождения элементов условия (в этом случае максимум и минимум,
# может быть количество нулей, количество отрицательных числе и т.д.)
def counting(array):
    print()
    # как начальное значение для макс/мин берется первый элемент массива
    max_value = array[0][0]
    min_value = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] > max_value:
                max_value = array[i][j]
                max_i = i
                max_j = j
            if array[i][j] < min_value:
                min_value = array[i][j]
                min_i = i
                min_j = j
    print("Максимум: %d[%d][%d], минимум: %d[%d][%d]" % (
    max_value, max_i + 1, max_j + 1, min_value, min_i + 1, min_j + 1))
    print()
    return max_value, min_value, max_i, max_j, min_i, min_j


def main():
    rowCount = 4
    colCount = 5
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(rowCount, colCount)  # можно изменить размер
    print("Условие задания:\n"
          "Если максимальный элемент в таблице расположен после минимального,\n"
          "то поменять значение максимального и минимального на 1,\n"
          "а остальное на 0")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    max_value, min_value, max_i, max_j, min_i, min_j = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(rowCount, colCount)
            print_array(array)
            max_value, min_value, max_i, max_j, min_i, min_j = counting(array)
        elif key == '2':
            max_value, min_value, max_i, max_j, min_i, min_j = counting(array)
            for i in range(len(array)):
                for j in range(len(array[i])):
                    k = array[i][j]
                    if k != min_value or k != max_value:
                        array[i][j] = 0
                    if max_i > min_i or max_j > min_j:
                        array[max_i][max_j] = 1
                        array[min_i][min_j] = 1
            print("Макс. и мин. элемент таблицы были изменены на 1.")
            print("Остальные числа были изменены на 0.")
            print_array(array)
            break  # выход из цикла


        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()