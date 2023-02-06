""" 
Найдите сумму цифр любого вещественного или целого числа. 
Можно использовать decimal. 
Через строку решать нельзя. 
"""
from decimal import Decimal as D

num = D('123456.789')
sum = 0
count = 0

while num != int(num):
    num *= 10

while num > 0:
    sum += num % 10
    num //= D('10')
    count += 1
    
print (int(sum))



