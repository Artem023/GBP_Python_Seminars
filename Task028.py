# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

a = int (input ("Enter random digit A: "))
b = int (input ("Enter random digit B: ")) 

def sum_dig(num1, num2):
  if num1 == 0:
    return num2 
  return sum_dig(num1 - 1, num2 + 1)
    

result = sum_dig(a, b)
print(result)