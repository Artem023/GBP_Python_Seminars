'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
'''

from random import randint

size = int (input ("Type size of array: "))
count_num = int (input("What number do u want to count?: "))
array = []
count = 0

for _ in range(size):
  array.append(randint(1, 10))
array.append(count_num)

for i in array:
  if i == count_num:
    count += 1
    
print(array, count)    