""" 2 
10 -> 1 2 4 8
"""
n = int (input ("Type a number: "))
num = 2
k = 0

while num ** k < n:
  result = num ** k
  k += 1
  print(result, end= " ")

