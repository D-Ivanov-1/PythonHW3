# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# * Пример:

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input('Введите колличество элементов: '))
list_A = [random.randint(1, 100) for i  in range(N)]
print(list_A)
X = int(input('Введите число х: '))
min = abs(X - list_A[0])
index = 0
for i in range(1, N):
        count = abs(X - list_A[i])
        if count < min:
            min = count
            index = i
print(f'Число {list_A[index]}->самый близкий по величине элемент к заданному числу;')