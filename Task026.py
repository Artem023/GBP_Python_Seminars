""" Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 """

a = int (input("Enter number A: "))
b = int (input ("Enter number B: "))

def square(digit, expo):
  if expo == 1:
    return digit 
  else:
    return digit * square(digit, expo - 1)

print(square(a, b))