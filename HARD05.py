# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек.
# A(x1, y1) B(x2, y2)
# d = sqrt(x2 - x1)**2 + (y2 - y1)**2

import math

try:
  n = int (input ("В каком пространстве нужно вычислить расстояние?: "))
  result = 0
  coordinates = []
  
  for _ in range (n * 2):
    number = int (input ("Вводите координаты вида A(x1, y1) B(x2, y2): "))
    coordinates.append(number)
  
  for i in range (n):
    result += math.pow(coordinates[i + n] - coordinates[i], 2)
  
  result = round(math.sqrt(result), 2)
  
  print(result)

except:
  print("Что-то полшло не так. Попробуйте еще раз!")