# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

from random import randint

bushes = int (input ("How many bushes grew in the garden?: "))
berries = [randint(1, 10) for _ in range(bushes)]

def NumberOfBerries(arr):
  max = 0
  temp = 0
  for i in range(len(arr) - 2):
    # for k in range(arr):
    temp = arr[i] + arr[i + 1] + arr[i + 2]
    if temp > max:
      max = temp
  return max

result = NumberOfBerries(berries)
print(berries)
print(result)