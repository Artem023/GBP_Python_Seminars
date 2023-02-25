# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

from random import randint

size1 = int (input("Enter the size of the first array: "))
size2 = int (input("Enter the size of the second array: "))
array1 = [randint(1, 50) for _ in range(size1)]
array2 = [randint(1, 50) for _ in range(size2)]

def SortArray(arr):
  k = 1
  for i in range(len(arr)):
    for k in range(len(arr)):
      if arr[i] < arr[k]:
        arr[i], arr[k] = arr[k], arr[i]
  return arr

array1 = SortArray(array1)
array2 = SortArray(array2)
print(f"{array1} \n{array2}")
        
for i in array1:
  for j in array2:
    if i == j:
      print(i, end=" ")