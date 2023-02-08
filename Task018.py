'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

from random import randint

size = int (input ("Type size of array: "))
num = int (input("Type a random number: "))
array = []

for _ in range(size):
  array.append(randint(1, 10))
array.append(num)
print(array)

min = array[0]
for i in range(len(array) - 1):
  if num != array[i]:
    res = abs(array[i] - num)
    if res < min - num:
      min = array[i]
  else: continue
print(min)
