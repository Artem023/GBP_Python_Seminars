# задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int (input ("Type  digit: "))
fib = [0, 1]
sum = 0

def creatFibonacci(count):
  for i in range(2, count + 1):
    sum = fib[i - 2] + fib[i - 1]
    fib.append(sum)
  return fib

def reverseFibonacci(fib):
  new_fib = fib[::-1]
  del new_fib[-1]
  return new_fib

def mergeFibonaccies (fib, new_fib):
  for i in fib:
    new_fib.append(i)
  return new_fib

def printResult (new_fib):
  for i in range (0, int(len(new_fib)/2), 2):
    new_fib[i] *= -1
  print(new_fib)

fibonacci = creatFibonacci(k)
rev_fibonacci = reverseFibonacci(fibonacci)
new_fibonacci = mergeFibonaccies(fibonacci, rev_fibonacci)
printResult(new_fibonacci)